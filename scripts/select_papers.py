"""Resolve the curated paper list to arXiv IDs via OpenAlex.

Runs at a polite rate; writes work/selected_papers.tsv with
source, title, year, arxiv_id, arxiv_url, matched_title.
"""

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

WORK = Path(__file__).resolve().parent
UA = "paper-skill-corpus/0.1 (local research corpus build)"
# the local proxy exit IP is rate-limited by OpenAlex, so bypass proxies entirely
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))

# title -> provenance
PAPERS: list[tuple[str, str]] = [
    # --- LLM core / reasoning / alignment ---
    ("Attention Is All You Need", "PD"),
    ("Language Models are Few-Shot Learners", "PD"),
    ("Training Language Models to Follow Instructions with Human Feedback", "PD"),
    ("Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "PD"),
    ("Self-Consistency Improves Chain of Thought Reasoning in Language Models", "PD"),
    ("Tree of Thoughts: Deliberate Problem Solving with Large Language Models", "PD"),
    ("ReAct: Synergizing Reasoning and Acting in Language Models", "PD"),
    ("Large Language Models Are Zero-Shot Reasoners", "PD"),
    ("Let's Verify Step by Step", "PD"),
    ("Direct Preference Optimization: Your Language Model is Secretly a Reward Model", "PD"),
    ("LoRA: Low-Rank Adaptation of Large Language Models", "PD"),
    ("QLoRA: Efficient Finetuning of Quantized LLMs", "PD"),
    ("Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", "PD"),
    ("Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection", "PD"),
    ("FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", "PD"),
    ("FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning", "PD"),
    ("SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", "PD"),
    ("LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code", "PD"),
    ("DeepSeek-R1", "ML"),
    ("DAPO: An Open-Source LLM Reinforcement Learning System at Scale", "PD"),
    ("Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity", "ML"),
    ("LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens", "ML"),
    # --- pretraining / encoders ---
    ("BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "ML"),
    ("RoBERTa: A Robustly Optimized BERT Pretraining Approach", "ML"),
    ("ALBERT: A Lite BERT for Self-supervised Learning of Language Representations", "ML"),
    ("ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators", "ML"),
    ("XLNet: Generalized Autoregressive Pretraining for Language Understanding", "ML"),
    ("BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension", "ML"),
    ("Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "ML"),
    ("Language Models are Unsupervised Multitask Learners", "ML"),
    # --- benchmarks ---
    ("GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding", "PD"),
    ("Measuring Massive Multitask Language Understanding", "PD"),
    # --- multimodal / VLM ---
    ("An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", "PD"),
    ("Learning Transferable Visual Models From Natural Language Supervision", "PD"),
    ("BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation", "PD"),
    ("BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models", "PD"),
    ("Flamingo: a Visual Language Model for Few-Shot Learning", "PD"),
    ("MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models", "PD"),
    ("Visual Instruction Tuning", "PD"),
    ("LAION-5B: An open large-scale dataset for training next generation image-text models", "PD"),
    ("Show-o: One Single Transformer to Unify Multimodal Understanding and Generation", "PD"),
    ("Qwen2 Technical Report", "ML"),
    ("ModernBERT", "ML"),
    ("Large Concept Models: Language Modeling in a Sentence Representation Space", "ML"),
    # --- vision backbones / self-supervised ---
    ("Emerging Properties in Self-Supervised Vision Transformers", "ML"),
    ("DINOv2: Learning Robust Visual Features without Supervision", "ML"),
    ("Swin Transformer: Hierarchical Vision Transformer using Shifted Windows", "ML"),
    ("A ConvNet for the 2020s", "ML"),
    ("End-to-End Object Detection with Transformers", "PD"),
    ("SAM 2: Segment Anything in Images and Videos", "PD"),
    # --- generative / diffusion ---
    ("Denoising Diffusion Probabilistic Models", "PD"),
    ("Denoising Diffusion Implicit Models", "PD"),
    ("Score-Based Generative Modeling through Stochastic Differential Equations", "PD"),
    ("Diffusion Models Beat GANs on Image Synthesis", "PD"),
    ("GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models", "PD"),
    ("Zero-Shot Text-to-Image Generation", "PD"),
    ("Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding", "PD"),
    ("High-Resolution Image Synthesis with Latent Diffusion Models", "ML"),
    ("SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis", "PD"),
    ("Scaling Rectified Flow Transformers for High-Resolution Image Synthesis", "PD"),
    ("CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer", "PD"),
    ("WorldSimBench: Towards Video Generation Models as World Simulators", "PD"),
    ("DreamFusion: Text-to-3D using 2D Diffusion", "PD"),
]


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def openalex_lookup(title: str) -> dict | None:
    query = urllib.parse.urlencode(
        {
            "search": title,
            "per-page": "5",
            "select": "id,display_name,publication_year,doi,locations",
        }
    )
    url = f"https://api.openalex.org/works?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with OPENER.open(req, timeout=45) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    target = normalize(title)
    best = None
    best_score = 0.0
    for item in data.get("results", []):
        name = item.get("display_name") or ""
        cand = normalize(name)
        if not cand:
            continue
        # cheap containment score, good enough for title matching
        score = 1.0 if cand == target else 0.0
        if not score:
            shorter, longer = sorted((cand, target), key=len)
            if len(shorter) >= 18 and shorter in longer:
                score = 0.8
        if score > best_score:
            best_score, best = score, item
    if not best or best_score < 0.8:
        return None
    arxiv_id = ""
    for loc in best.get("locations") or []:
        for key in ("landing_page_url", "pdf_url"):
            url_value = loc.get(key) or ""
            match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url_value)
            if match:
                arxiv_id = match.group(1)
                break
        if arxiv_id:
            break
    return {
        "matched_title": best.get("display_name", ""),
        "year": best.get("publication_year", ""),
        "arxiv_id": arxiv_id,
        "doi": best.get("doi", "") or "",
    }


def main() -> None:
    rows = []
    missing = []
    for index, (title, source) in enumerate(PAPERS, 1):
        info = None
        for attempt in range(3):
            try:
                info = openalex_lookup(title)
                break
            except Exception as exc:  # transient rate limit / network hiccup
                wait = 4 * (attempt + 1)
                print(f"[{index:02d}] retry{attempt + 1} {title[:50]} -> {exc} (wait {wait}s)")
                time.sleep(wait)
        if not info or not info["arxiv_id"]:
            missing.append((source, title))
            print(f"[{index:02d}] no-arxiv  {title[:70]}")
        else:
            rows.append((source, title, info["year"], info["arxiv_id"], info["matched_title"]))
            print(f"[{index:02d}] {info['arxiv_id']}  {title[:66]}")
        time.sleep(0.8)

    out = WORK / "selected_papers.tsv"
    out.write_text(
        "\n".join("\t".join(str(c) for c in row) for row in rows),
        encoding="utf-8",
    )
    print(f"\nresolved={len(rows)} missing={len(missing)} -> {out}")
    if missing:
        (WORK / "selected_missing.txt").write_text(
            "\n".join(f"{s}\t{t}" for s, t in missing), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
