"""Fetch arXiv abs-page metadata (title, authors, abstract, comments, category)."""

import html
import json
import re
import time
import urllib.request
from pathlib import Path

WORK = Path(__file__).resolve().parent
UA = "Mozilla/5.0 (compatible; paper-skill-corpus/0.1)"


def text_of(fragment: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def fetch(arxiv_id: str) -> dict:
    req = urllib.request.Request(
        f"https://arxiv.org/abs/{arxiv_id}", headers={"User-Agent": UA}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        page = resp.read().decode("utf-8", errors="replace")
    title = text_of(
        re.search(r'<h1 class="title mathjax">(.*?)</h1>', page, re.S).group(1)
    ).replace("Title:", "").strip()
    abstract_match = re.search(
        r'<blockquote class="abstract mathjax">(.*?)</blockquote>', page, re.S
    )
    abstract = text_of(abstract_match.group(1)).replace("Abstract:", "").strip() if abstract_match else ""
    authors = [
        text_of(m)
        for m in re.findall(r'<a href="/search/\?searchtype=author[^"]*">(.*?)</a>', page, re.S)
    ]
    comments_match = re.search(
        r'<td class="tablecell comments[^"]*">(.*?)</td>', page, re.S
    )
    comments = text_of(comments_match.group(1)) if comments_match else ""
    subjects_match = re.search(
        r'<td class="tablecell subjects">(.*?)</td>', page, re.S
    )
    subjects = text_of(subjects_match.group(1)) if subjects_match else ""
    date_match = re.search(r"\[Submitted on ([^\]<]+)\]", page)
    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "comments": comments,
        "subjects": subjects,
        "submitted": date_match.group(1).strip() if date_match else "",
    }


def main() -> None:
    ids = [
        line.split("\t")[3]
        for line in (WORK / "selected_papers.tsv").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    meta_path = WORK / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    for index, arxiv_id in enumerate(ids, 1):
        if arxiv_id in meta and meta[arxiv_id].get("abstract"):
            print(f"[{index:02d}/{len(ids)}] cached {arxiv_id}", flush=True)
            continue
        try:
            meta[arxiv_id] = fetch(arxiv_id)
            print(
                f"[{index:02d}/{len(ids)}] ok {arxiv_id} abstract={len(meta[arxiv_id]['abstract'])}",
                flush=True,
            )
        except Exception as exc:
            print(f"[{index:02d}/{len(ids)}] ERROR {arxiv_id} -> {exc}", flush=True)
        time.sleep(3.2)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"meta entries: {len(meta)}")


if __name__ == "__main__":
    main()
