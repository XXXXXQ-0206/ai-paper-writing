"""Verify arXiv IDs by reading the title on each abs page."""

import html
import re
import time
import urllib.request
from pathlib import Path

WORK = Path(__file__).resolve().parent
UA = "Mozilla/5.0 (compatible; paper-skill-corpus/0.1)"

CHECKS = [
    ("2203.02155", "Training language models to follow instructions with human feedback"),
    ("2201.11903", "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"),
    ("2106.09685", "LoRA: Low-Rank Adaptation of Large Language Models"),
    ("2310.06770", "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"),
    ("2501.12948", "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"),
    ("2412.13663", "Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder"),
    ("2503.18352", "? check what this actually is (suspicious latent-diffusion match)"),
    ("2112.10752", "High-Resolution Image Synthesis with Latent Diffusion Models"),
]


def abs_title(arxiv_id: str) -> str:
    req = urllib.request.Request(
        f"https://arxiv.org/abs/{arxiv_id}", headers={"User-Agent": UA}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        page = resp.read().decode("utf-8", errors="replace")
    match = re.search(
        r'<h1 class="title mathjax">(.*?)</h1>', page, flags=re.S
    )
    if not match:
        return "(no title found)"
    raw = html.unescape(re.sub(r"<[^>]+>", " ", match.group(1)))
    return " ".join(raw.split()).replace("Title:", "").strip()


def main() -> None:
    lines = []
    for arxiv_id, expected in CHECKS:
        try:
            title = abs_title(arxiv_id)
        except Exception as exc:
            title = f"ERR {exc}"
        lines.append(f"{arxiv_id}\t{title}")
        print(f"{arxiv_id}  {title[:100]}", flush=True)
        time.sleep(3.2)
    (WORK / "verified_ids.txt").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
