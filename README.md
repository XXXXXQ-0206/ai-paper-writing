# ai-paper-writing

A writing skill for AI coding agents that produce LLM / VLM research papers. The skill ships a corpus built from 64 AI papers: LaTeX sources are downloaded, reduced to plain prose (figures, tables, equations, citations and bibliography removed), and grouped by paper module.

## Contents

```
ai-paper-writing/
├── SKILL.md                 # generation order + retrieval protocol + hard rules
├── agents/openai.yaml       # Codex desktop UI metadata
├── references/              # the seven module corpora (~1.17 MB)
│   ├── 01-introduction.md
│   ├── 02-related-work.md
│   ├── 03-preliminaries.md
│   ├── 04-method.md
│   ├── 05-discussion.md
│   ├── 06-conclusion.md
│   └── 07-abstract.md
├── papers.tsv               # the 64 selected papers: list, title, year, arXiv ID
└── scripts/                 # reproducible pipeline
    ├── select_papers.py         # build the candidate list
    ├── resolve_missing.py       # fallback resolution
    ├── resolve_search.py        # fallback resolution (search page)
    ├── verify_ids.py            # check every title against its abs page
    ├── add_embodied.py          # append RT-1 / RT-2
    ├── finalize_selection.py    # write papers.tsv and the link list
    ├── fetch_corpus.py          # download LaTeX sources, reduce to plain text
    ├── fetch_meta.py            # fetch titles, authors, abstracts
    └── build_clusters.py        # slice sections into the seven modules
```

Every corpus entry carries light tags so it can be located with `rg`:

```
@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Introduction
```

## Install

Drop the whole folder into your skills root, keeping the folder name:

```
~/.codex/skills/ai-paper-writing/        # Codex
~/.dsh/skills/ai-paper-writing/          # DSH (DeepSeek Harness)
```

DSH accepts an optional frontmatter field:

```yaml
whenToUse: "Writing an academic paper on LLM/VLM/multimodal/AI topics"
```

## Scope of the selection

The 64 papers come from two public reading lists — Paper Digest's *100 Must-Read Machine Learning Papers of the Past 10 Years (2016–2025)* and ML-Digest's *Influential AI/ML Papers* — filtered to LLM, VLM and generative-model directions, plus two foundational embodied-AI papers (RT-1, RT-2). Each entry was checked against its arXiv `abs` page before it was written into `papers.tsv`.

Coverage: LLM cores and reasoning/alignment, pretrained encoders, evaluation benchmarks, multimodal VLMs, vision backbones and self-supervised models, generative and diffusion models, video and world models, embodied AI.

## Rebuilding the corpus

```bash
python scripts/finalize_selection.py     # write papers.tsv
python scripts/fetch_corpus.py           # download and clean (4 s per paper)
python scripts/fetch_meta.py             # titles, authors, abstracts
python scripts/build_clusters.py         # slice into the seven modules
```

The fetch scripts request one paper every 3–4 seconds to follow arXiv's crawling guidance; a full rebuild takes roughly 15–20 minutes.

## Languages

- English: this file
- 中文: README.zh-CN.md
