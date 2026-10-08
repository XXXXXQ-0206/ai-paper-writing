"""Verify and add two classic embodied-AI (VLA) papers to the selection."""

import json
import time
from pathlib import Path

import fetch_meta

WORK = Path(__file__).resolve().parent
CANDIDATES = [
    ("2212.06817", "RT-1: Robotics Transformer for Real-World Control at Scale"),
    ("2307.15818", "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"),
]


def normalize(text: str) -> str:
    import re

    return re.sub(r"[^a-z0-9]+", "", text.lower())


def main() -> None:
    tsv = WORK / "selected_papers.tsv"
    rows = [
        line.split("\t")
        for line in tsv.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    meta_path = WORK / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    have = {row[3] for row in rows}

    for arxiv_id, expected in CANDIDATES:
        if arxiv_id in have:
            print(f"already present {arxiv_id}")
            continue
        info = fetch_meta.fetch(arxiv_id)
        got = normalize(info["title"])
        want = normalize(expected)
        ok = got == want or want in got or got in want
        print(f"{arxiv_id}\texpected_ok={ok}\t{info['title'][:80]}")
        if not ok:
            print("  !! title mismatch, not added")
            continue
        year = (info.get("submitted") or "")[-4:]
        rows.append(["SUPP", info["title"], year, arxiv_id, info["title"]])
        meta[arxiv_id] = info
        time.sleep(3.2)

    rows.sort(key=lambda r: r[3])
    tsv.write_text("\n".join("\t".join(r) for r in rows), encoding="utf-8")
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"rows={len(rows)} meta={len(meta)}")


if __name__ == "__main__":
    main()
