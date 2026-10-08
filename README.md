# ai-paper-writing

写作 LLM / VLM 论文时给 AI 代理用的 skill。技能本体是一份按论文模块分簇的语料：从 64 篇 AI 论文的 LaTeX 源码里抽出正文、剥掉图表公式与引用，按 Introduction / Related Work / Preliminaries / Method / Discussion / Conclusion / Abstract 七个模块归堆。

## 结构

```
ai-paper-writing/
├── SKILL.md                 # 技能入口：生成流程 + 检索协议 + 硬规则
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
    ├── select_papers.py         # 初始选目 → OpenAlex 解析 arXiv ID
    ├── resolve_missing.py       # 兜底：arXiv API 解析
    ├── resolve_search.py        # 兜底：arXiv 检索页解析
    ├── verify_ids.py            # 逐篇抓 abs 页面核对标题
    ├── add_embodied.py          # 追加 RT-1 / RT-2
    ├── finalize_selection.py    # 生成 papers.tsv 与链接列表
    ├── fetch_corpus.py          # 下载 LaTeX 源码并清洗为纯正文
    ├── fetch_meta.py            # 抓标题 / 作者 / 摘要元数据
    └── build_clusters.py        # 按章节名切分到七个模块
```

语料片段带浅标签，便于检索：

```
@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Introduction
```

## 安装

放在技能根目录下，目录名与技能名一致。

```
# Codex
~/.codex/skills/ai-paper-writing/

# DSH（DeepSeek Harness）
~/.dsh/skills/ai-paper-writing/
```

DSH 的 frontmatter 支持可选字段 `whenToUse`，可补一行：

```yaml
whenToUse: "写 LLM/VLM/多模态/AI 方向的学术论文时"
```

## 选目

64 篇的来源：Paper Digest《100 must-read ML papers 2016–2025》与 ML-Digest《influential AI/ML papers》两个榜单的并集，按 LLM / VLM / 生成模型方向筛选，另补两篇具身智能奠基工作 RT-1、RT-2。每一条都抓过 arXiv `abs` 页面核对标题；期间纠正过一处错配（Latent Diffusion 曾被解析成 `2503.18352`，实为 Diffusion-4K，已改回 `2112.10752`），并剔除了不在 arXiv 上的 GPT-2 技术报告。

## 重建语料

```bash
python scripts/finalize_selection.py     # 生成 papers.tsv
python scripts/fetch_corpus.py           # 下载并清洗（每篇间隔 4 秒）
python scripts/fetch_meta.py             # 标题 / 摘要元数据
python scripts/build_clusters.py         # 切分为七个模块
```

注意两点：`fetch_corpus.py` 与 `fetch_meta.py` 会访问 arxiv.org，脚本里已按每篇 3–4 秒的节奏限速；若本机走代理导致 `export.arxiv.org` 返回 429，改用 arXiv 检索页或直连 OpenAlex（脚本内已做无代理处理）。
