"""Merge verified stragglers, fix the mismatched latent-diffusion row,
and emit the arXiv link list.
"""

import re
from pathlib import Path

WORK = Path(__file__).resolve().parent
OUT = Path(r"C:\Users\熊骞\Documents\Codex\2026-10-08\x\outputs")
TSV = WORK / "selected_papers.tsv"

VERIFIED = [
    ("PD", "Training Language Models to Follow Instructions with Human Feedback", "2022",
     "2203.02155", "Training language models to follow instructions with human feedback"),
    ("PD", "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "2022",
     "2201.11903", "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"),
    ("PD", "LoRA: Low-Rank Adaptation of Large Language Models", "2021",
     "2106.09685", "LoRA: Low-Rank Adaptation of Large Language Models"),
    ("PD", "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", "2023",
     "2310.06770", "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"),
    ("ML", "DeepSeek-R1", "2025",
     "2501.12948", "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"),
    ("ML", "ModernBERT", "2024",
     "2412.13663", "Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder"),
]

DROP_TITLES = {"Language Models are Unsupervised Multitask Learners"}
FIX = {
    "High-Resolution Image Synthesis with Latent Diffusion Models": (
        "2112.10752",
        "High-Resolution Image Synthesis with Latent Diffusion Models",
    )
}


def main() -> None:
    rows = [
        line.split("\t")
        for line in TSV.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    # fix the mismatched latent-diffusion row
    for row in rows:
        if row[1] in FIX:
            row[3], row[4] = FIX[row[1]]
    # append verified stragglers that are not present yet
    have = {row[1] for row in rows}
    for source, title, year, arxiv_id, matched in VERIFIED:
        if title not in have:
            rows.append([source, title, year, arxiv_id, matched])
    # drop entries that are not on arXiv
    rows = [row for row in rows if row[1] not in DROP_TITLES]
    # dedupe by arXiv id, keep first occurrence
    seen = set()
    unique = []
    for row in rows:
        if row[3] in seen:
            continue
        seen.add(row[3])
        unique.append(row)
    unique.sort(key=lambda r: r[3])

    TSV.write_text("\n".join("\t".join(r) for r in unique), encoding="utf-8")

    md = [
        "# AI 论文写作 skill · 语料选目",
        "",
        f"共 {len(unique)} 篇，全部经 arXiv 页面或检索结果核对标题。",
        "来源标记：PD = Paper Digest 100 must-read（2016–2025）；ML = ML-Digest influential AI/ML papers。",
        "",
        "| # | arXiv | 年份 | 标题 | 来源 |",
        "|---|---|---|---|---|",
    ]
    for index, (source, title, year, arxiv_id, _matched) in enumerate(unique, 1):
        md.append(
            f"| {index} | https://arxiv.org/abs/{arxiv_id} | {year} | {title} | {source} |"
        )
    (OUT / "AI论文写作skill_选目.md").write_text("\n".join(md), encoding="utf-8")

    links = "\n".join(
        f"https://arxiv.org/abs/{row[3]}" for row in unique
    )
    (OUT / "AI论文写作skill_arxiv链接.txt").write_text(links, encoding="utf-8")
    print(f"papers={len(unique)}")
    for row in unique:
        print(f"{row[3]}\t{row[1][:70]}")


if __name__ == "__main__":
    main()
