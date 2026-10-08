---
name: ai-paper-writing
description: "写 LLM/VLM 论文时使用。"
---

# AI 论文写作（LLM / VLM）

正文按模块生成：Introduction、Related Work、Method、Conclusion、Abstract 必选；Preliminaries 只在新符号、新定义或新形式化出现时单列；Discussion 按需，可与 Conclusion 合并。参考文献条目、附录、图表、致谢不在生成范围内。

## 语料怎么取用

语料按模块放在 `references/`，每个片段前面有三行浅标签：

```
@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Introduction
```

先检索定位，再读局部，不要整文件读入：

- 缺口与动机：`rg -n "however|remains|challeng|gap|in this paper" references/01-introduction.md`
- 差异与定位：`rg -n "in contrast|unlike|orthogonal|while .* focus" references/02-related-work.md`
- 方法与设计动机：`rg -n "motivat|key insight|we design|to address" references/04-method.md`
- 局限与影响：`rg -n "limitation|broader impact|future work" references/05-discussion.md`
- 结论与展望：`rg -n "in summary|we hope|future work" references/06-conclusion.md`
- 摘要骨架：读 2–3 篇同方向条目的 `@section Abstract` 片段作模板

命中后读该处前后 5–8 行；必要时用 `@src` 回原论文核对上下文。

## 生成顺序

1. 事实清点：向用户取四类输入——方法、实验与结果、**动机与缺口**、目标会议与篇幅。缺口信息缺失时先追问，不要用"现有方法存在不足"这类空话填充；其余缺失信息留 `[RESULT]` / `[GAP]` 占位，不得编造。
2. 贡献定稿：三条贡献＋与已有工作的差异，作为后续所有章节的基准。
3. Method（同时判定是否单列 Preliminaries）。
4. Related Work。
5. Introduction（回填贡献与定位）。
6. Discussion（可选）。
7. Conclusion。
8. Abstract 最后生成，只做全文提炼。

## 硬规则

- Abstract 必须最后生成，不引入正文之外的新信息。
- 不生成参考文献条目、附录、图表、致谢；引用写 `[CITE: 主题]`，图表写 `[FIG-k]` 或 `[TAB-k]` 占位。
- 不编造数字、数据集、基线、指标；缺失即留占位并标注。
- Preliminaries 仅在有新符号、新定义或新形式化时单列，否则并入 Method。
- Discussion 可省略或与 Conclusion 合并。
- 目标会议与篇幅：用户未声明时由你自行决定，并在文首注明假设（会议、正文页数、目标字数）。
- 术语首次出现给全称与缩写，后文统一。
