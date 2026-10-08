"""Slice the cleaned papers into writing-module clusters.

Clusters: introduction, related-work, preliminaries, method, discussion,
conclusion, abstract. Experiments/results and appendix material are collected
separately and are not part of the writing modules.
"""

import json
import re
from pathlib import Path

WORK = Path(__file__).resolve().parent
CLEAN = WORK / "clean"
CORPUS = WORK / "corpus"

CLUSTER_TITLES = {
    "introduction": "01-introduction.md",
    "related-work": "02-related-work.md",
    "preliminaries": "03-preliminaries.md",
    "method": "04-method.md",
    "discussion": "05-discussion.md",
    "conclusion": "06-conclusion.md",
    "abstract": "07-abstract.md",
    "experiments": "90-experiments-not-a-module.md",
    "other": "91-other-not-a-module.md",
}

SECTION_RULES = [
    ("preliminaries", r"preliminar|notation|problem (formulation|setup|definition|statement)|task (formulation|definition)|background and (notation|preliminar)"),
    ("conclusion", r"^\s*(conclusion|conclusions|concluding|summary|conclusion and|conclusions and|conclusion &)"),
    ("discussion", r"discussion|limitation|broader impact|ethical|societal impact|future work"),
    ("related-work", r"related work|prior work|literature|^background"),
    ("method", r"method|approach|our model|model architecture|architecture|framework|proposed|system design|implementation|training|pre-?training|instruction tuning|alignment"),
    ("experiments", r"experiment|evaluation|results|benchmark|ablation|analysis|dataset"),
    ("introduction", r"introduction|motivation|overview"),
]


def classify(heading: str) -> str:
    text = heading.strip().lower()
    text = re.sub(r"^\d+(\.\d+)*\s*", "", text)
    for name, pattern in SECTION_RULES:
        if re.search(pattern, text):
            return name
    return "other"


def sections_of(path: Path) -> list[tuple[str, str]]:
    """Split a cleaned paper into (heading, body) pairs."""
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^# source:.*?\n", "", text, count=1)
    parts = re.split(r"^(#{2,4})\s+(.*)$", text, flags=re.M)
    out: list[tuple[str, str]] = []
    buffer = []
    heading = ""
    # parts: [pre, hashes, title, body, hashes, title, body, ...]
    if parts:
        buffer.append(parts[0])
    index = 1
    while index + 2 < len(parts) + 1 and index + 1 < len(parts):
        hashes, title, body = parts[index], parts[index + 1], parts[index + 2]
        if heading:
            out.append((heading, "\n".join(buffer).strip()))
            buffer = []
        heading = title.strip()
        buffer.append(body)
        index += 3
    if heading:
        out.append((heading, "\n".join(buffer).strip()))
    elif buffer:
        out.append(("__preamble__", "\n".join(buffer).strip()))
    return out


def clean_body(text: str) -> str:
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if len(line) < 40:
            continue
        if re.fullmatch(r"[\W_]+", line):
            continue
        lines.append(line)
    return "\n\n".join(lines)


def main() -> None:
    CORPUS.mkdir(exist_ok=True)
    meta = json.loads((WORK / "meta.json").read_text(encoding="utf-8")) if (WORK / "meta.json").exists() else {}
    buckets: dict[str, list[tuple[str, str, str]]] = {key: [] for key in CLUSTER_TITLES}
    stats: dict[str, dict] = {}

    for path in sorted(CLEAN.glob("*.txt")):
        arxiv_id = path.stem
        info = meta.get(arxiv_id, {})
        title = info.get("title") or arxiv_id
        covered = []
        for heading, body in sections_of(path):
            prose = clean_body(body)
            if len(prose) < 400:
                continue
            cluster = classify(heading)
            if cluster not in buckets:
                cluster = "other"
            buckets[cluster].append((arxiv_id, heading, prose))
            covered.append(cluster)
        stats[arxiv_id] = {
            "title": title,
            "clusters": sorted(set(covered)),
            "chars": path.stat().st_size,
        }

    for arxiv_id, info in meta.items():
        abstract = (info.get("abstract") or "").strip()
        if len(abstract) >= 200:
            buckets["abstract"].append((arxiv_id, "Abstract", abstract))
            stats.setdefault(arxiv_id, {"title": info.get("title", arxiv_id), "clusters": [], "chars": 0})
            stats[arxiv_id].setdefault("clusters", []).append("abstract")

    index_lines = []
    for cluster, filename in CLUSTER_TITLES.items():
        rows = buckets[cluster]
        if not rows:
            continue
        chunks = [f"# {cluster} corpus ({len(rows)} sources)\n"]
        for arxiv_id, heading, prose in rows:
            title = (meta.get(arxiv_id, {}).get("title") or "").strip()
            chunks.append(
                f"@src https://arxiv.org/abs/{arxiv_id}\n"
                f"@title {title}\n"
                f"@section {heading}\n\n{prose}\n"
            )
        body = "\n".join(chunks)
        (CORPUS / filename).write_text(body, encoding="utf-8")
        index_lines.append(
            f"{filename}\t{len(rows)} sources\t{len(body)} chars"
        )
        print(index_lines[-1])

    (WORK / "cluster_stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (CORPUS / "00-index.tsv").write_text("\n".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
