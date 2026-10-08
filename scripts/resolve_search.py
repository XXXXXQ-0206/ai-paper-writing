"""Resolve remaining titles through the arXiv search page (export API is rate-limited).

The search endpoint is served by arxiv.org itself, which is reachable here.
Polite pacing: one request every ~3.5 s.
"""

import html
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

WORK = Path(__file__).resolve().parent
UA = "Mozilla/5.0 (compatible; paper-skill-corpus/0.1)"


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def search_arxiv(title: str) -> tuple[str, str] | None:
    query = urllib.parse.urlencode(
        {"searchtype": "all", "query": title, "size": "50"}
    )
    url = f"https://arxiv.org/search/?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        page = resp.read().decode("utf-8", errors="replace")
    blocks = re.findall(r'<li class="arxiv-result">(.*?)</li>', page, flags=re.S)
    target = normalize(title)
    best = None
    best_score = 0.0
    for block in blocks:
        id_match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", block)
        title_match = re.search(
            r'<p class="title is-5 mathjax">(.*?)</p>', block, flags=re.S
        )
        if not id_match or not title_match:
            continue
        found_title = " ".join(
            html.unescape(re.sub(r"<[^>]+>", " ", title_match.group(1))).split()
        )
        cand = normalize(found_title)
        score = 1.0 if cand == target else 0.0
        if not score:
            shorter, longer = sorted((cand, target), key=len)
            if len(shorter) >= 18 and shorter in longer:
                score = 0.8
        if score > best_score:
            best_score = score
            best = (id_match.group(1), found_title)
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
                found = search_arxiv(title)
                break
            except Exception as exc:
                print(f"[{index:02d}] retry{attempt + 1} {title[:45]} -> {exc}", flush=True)
                time.sleep(6)
        if found:
            arxiv_id, matched = found
            rows.append([source, title, "", arxiv_id, matched])
            print(f"[{index:02d}] {arxiv_id}  {title[:60]}", flush=True)
        else:
            still_missing.append([source, title])
            print(f"[{index:02d}] still-missing  {title[:60]}", flush=True)
        time.sleep(3.5)

    resolved_path.write_text(
        "\n".join("\t".join(row) for row in rows), encoding="utf-8"
    )
    missing_path.write_text(
        "\n".join("\t".join(row) for row in still_missing), encoding="utf-8"
    )
    print(f"\ntotal resolved={len(rows)} still missing={len(still_missing)}")


if __name__ == "__main__":
    main()
