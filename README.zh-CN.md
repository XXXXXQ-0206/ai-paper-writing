# ai-paper-writing

给 AI 代理用的 LLM / VLM 论文写作用 skill。技能本体是一份按论文模块分簇的语料：抓取 64 篇 AI 论文的 LaTeX 源码，抽出正文并去掉图表、公式、引用与参考文献，按写作模块归堆。

## 内容

```
ai-paper-writing/
├── SKILL.md                 # 生成流程 + 检索协议 + 硬规则
├── agents/openai.yaml       # Codex 桌面端界面元数据
├── references/              # 七个写作模块的语料（约 1.17 MB）
│   ├── 01-introduction.md
│   ├── 02-related-work.md
│   ├── 03-preliminaries.md
│   ├── 04-method.md
│   ├── 05-discussion.md
│   ├── 06-conclusion.md
│   └── 07-abstract.md
├── papers.tsv               # 64 篇选目：来源、标题、年份、arXiv ID
└── scripts/                 # 可复现流水线
    ├── select_papers.py         # 选目解析
    ├── resolve_missing.py       # 兜底解析
    ├── resolve_search.py        # 兜底解析（检索页）
    ├── verify_ids.py            # 逐篇核对标题
    ├── add_embodied.py          # 追加 RT-1 / RT-2
    ├── finalize_selection.py    # 生成 papers.tsv 与链接列表
    ├── fetch_corpus.py          # 下载 LaTeX 源码并清洗为纯正文
    ├── fetch_meta.py            # 抓标题 / 作者 / 摘要元数据
    └── build_clusters.py        # 按章节名切分到七个写作模块
```

语料片段带浅标签，便于检索定位：

```
@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Introduction
```

## 安装

把整个目录放进技能根目录，目录名与技能名保持一致：

```
~/.codex/skills/ai-paper-writing/        # Codex
~/.dsh/skills/ai-paper-writing/          # DSH（DeepSeek Harness）
```

DSH 支持可选字段 `whenToUse`，可补一行：

```yaml
whenToUse: "Writing an academic paper on LLM/VLM/multimodal/AI topics"
```

## 选目范围

64 篇取自两份公开阅读清单的交集与并集筛选：Paper Digest《100 Must-Read Machine Learning Papers of the Past 10 Years (2016–2025)》与 ML-Digest《Influential AI/ML Papers》，方向限定在 LLM / VLM / 生成模型，另补两篇具身智能奠基工作 RT-1 与 RT-2。每条选目在写入 `papers.tsv` 前都对照 arXiv `abs` 页面核对过标题。

覆盖范围：LLM 核心与推理对齐、预训练编码器、评测基准、多模态 VLM、视觉骨干与自监督、生成与扩散、视频与世界模型、具身智能。

## 重建语料

```bash
python scripts/finalize_selection.py     # 生成 papers.tsv
python scripts/fetch_corpus.py           # 下载并清洗（每篇间隔 4 秒）
python scripts/fetch_meta.py             # 标题 / 作者 / 摘要元数据
python scripts/build_clusters.py         # 切分为七个写作模块
```

抓取脚本按每篇 3–4 秒的节奏请求 arXiv，遵循其爬取建议，全量重建约需 15–20 分钟。

## 语言

- 中文：本文件
- English: README.md
