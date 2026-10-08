"""Resolve remaining titles through the arXiv API and merge into selected_papers.tsv.

arXiv asks for at most one request every three seconds; we use 3.2 s.
"""

import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

WORK = Path(__file__).resolve().parent
UA = "paper-skill-corpus/0.1 (local research corpus build)"
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))
ATOM = "{http://www.w3.org/2005/Atom}"


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def arxiv_lookup(title: str) -> tuple[str, str] | None:
    query = urllib.parse.urlencode(
        {"search_query": f'ti:"{title}"', "max_results": "5"}
    )
    url = f"https://export.arxiv.org/api/query?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with OPENER.open(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    root = ET.fromstring(raw)
    target = normalize(title)
    best = None
    best_score = 0.0
    for entry in root.findall(f"{ATOM}entry"):
        name = " ".join((entry.findtext(f"{ATOM}title") or "").split())
        cand = normalize(name)
        if not cand:
            continue
        score = 1.0 if cand == target else 0.0
        if not score:
            shorter, longer = sorted((cand, target), key=len)
            if len(shorter) >= 18 and shorter in longer:
                score = 0.8
        if score > best_score:
            link = entry.findtext(f"{ATOM}id") or ""
            match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", link)
            if match:
                best_score, best = score, (match.group(1), name)
    return best if best_score >= 0.8 else None


def main() -> None:
    resolved_path = WORK / "selected_papers.tsv"
    missing_path = WORK / "selected_missing.txt"
    rows = [
        line.split("\t")
        for line in resolved_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    missing = [
        line.split("\t")
        for line in missing_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    still_missing = []
    for index, (source, title) in enumerate(missing, 1):
        found = None
        for attempt in range(2):
            try:
                found = arxiv_lookup(title)
                break
            except Exception as exc:
                print(f"[{index:02d}] retry{attempt + 1} {title[:50]} -> {exc}")
                time.sleep(5)
        if found:
            arxiv_id, matched = found
            rows.append([source, title, "", arxiv_id, matched])
            print(f"[{index:02d}] {arxiv_id}  {title[:64]}")
        else:
            still_missing.append([source, title])
            print(f"[{index:02d}] still-missing  {title[:64]}")
        time.sleep(3.2)

    resolved_path.write_text(
        "\n".join("\t".join(row) for row in rows), encoding="utf-8"
    )
    missing_path.write_text(
        "\n".join("\t".join(row) for row in still_missing), encoding="utf-8"
    )
    print(f"\ntotal resolved={len(rows)} still missing={len(still_missing)}")


if __name__ == "__main__":
    main()
