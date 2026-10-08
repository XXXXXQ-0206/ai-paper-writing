"""Download arXiv LaTeX sources and reduce them to plain body text.

Output: work/clean/<arxiv_id>.txt   (plain prose, section headings kept as "## ...")
Rate: one download every ~4 s, as arXiv asks for polite crawling.
"""

import gzip
import io
import re
import tarfile
import time
import urllib.request
from pathlib import Path

WORK = Path(__file__).resolve().parent
SRC = WORK / "sources"
CLEAN = WORK / "clean"
UA = "Mozilla/5.0 (compatible; paper-skill-corpus/0.1; contact: local research use)"

DROP_ENVS = (
    "figure", "figure*", "table", "table*", "algorithm", "algorithmic",
    "equation", "equation*", "align", "align*", "eqnarray", "eqnarray*",
    "gather", "gather*", "multline", "multline*", "lstlisting", "verbatim",
    "tikzpicture", "tabular", "tabular*", "array", "longtable", "wrapfigure",
    "subfigure", "subtable", "displaymath", "math", "split", "cases",
    "thebibliography", "appendix", "algorithm2e", "algorithmicx",
)

KEEP_CONTENT = (
    "textbf", "textit", "textrm", "textsf", "texttt", "textsc", "emph", "text",
    "mathrm", "mathbf", "mathit", "mbox", "textnormal", "uline", "underline",
    "href", "url", "textcolor", "colorbox", "captionof", "paragraph", "subparagraph",
)


def download(arxiv_id: str) -> bytes | None:
    req = urllib.request.Request(
        f"https://arxiv.org/e-print/{arxiv_id}", headers={"User-Agent": UA}
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def unpack(blob: bytes) -> dict[str, str]:
    """Return {filename: text} for the LaTeX/text members of an arXiv source blob."""
    files: dict[str, str] = {}
    data = blob
    if blob[:2] == b"\x1f\x8b":
        try:
            data = gzip.decompress(blob)
        except Exception:
            return files
    if data[:5] == b"%PDF-":
        return files  # no LaTeX source, PDF only
    if data[:2] == b"\x1f\x8b":
        try:
            data = gzip.decompress(data)
        except Exception:
            pass
    if tarfile.is_tarfile(io.BytesIO(data)):
        with tarfile.open(fileobj=io.BytesIO(data)) as tar:
            for member in tar.getmembers():
                if not member.isfile():
                    continue
                if not re.search(r"\.(tex|bbl|txt|ltx)$", member.name, re.I):
                    continue
                handle = tar.extractfile(member)
                if handle is None:
                    continue
                raw = handle.read()
                files[member.name] = raw.decode("utf-8", errors="replace")
    else:
        text = data.decode("utf-8", errors="replace")
        files["main.tex"] = text
    # a gzipped single .tex arrives as one tar-less file
    if not files and data[:1] == b"\\":
        files["main.tex"] = data.decode("utf-8", errors="replace")
    return files


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        keep = []
        index = 0
        while index < len(line):
            char = line[index]
            if char == "\\" and index + 1 < len(line):
                keep.append(line[index : index + 2])
                index += 2
                continue
            if char == "%":
                break
            keep.append(char)
            index += 1
        out.append("".join(keep))
    return "\n".join(out)


def drop_environments(text: str) -> str:
    for env in DROP_ENVS:
        pattern = re.compile(
            r"\\begin\{" + re.escape(env) + r"\}.*?\\end\{" + re.escape(env) + r"\}",
            re.S,
        )
        text = pattern.sub(" ", text)
    text = re.sub(r"\\begin\{document\}", " ", text)
    text = re.sub(r"\\end\{document\}", " ", text)
    return text


def unwrap_commands(text: str) -> str:
    for cmd in KEEP_CONTENT:
        text = re.sub(
            r"\\" + cmd + r"\s*\{([^{}]*)\}", r"\1", text, flags=re.S
        )
        text = re.sub(
            r"\\" + cmd + r"\s*\{([^{}]*)\}", r"\1", text, flags=re.S
        )
    # sectioning -> markdown-ish markers
    for level, name in ((2, "section"), (3, "subsection"), (4, "subsubsection")):
        text = re.sub(
            r"\\" + name + r"\*?\s*\{([^{}]*)\}",
            lambda m, level=level: "\n\n" + "#" * level + " " + m.group(1).strip() + "\n",
            text,
        )
    # inline math
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.S)
    text = re.sub(r"\$[^$]{0,400}?\$", " MATH ", text, flags=re.S)
    # references / labels / citations / footnotes
    text = re.sub(r"\\cite[a-zA-Z]*\s*(?:\[[^\]]*\])*\s*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\ref\s*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\eqref\s*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\label\s*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\footnote\s*\{", " (", text)
    text = re.sub(r"\\(?:v|h)space\*?\s*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\[a-zA-Z@]+\*?\s*(?:\[[^\]]*\])?", " ", text)
    text = text.replace("\\\\", " ")
    # leftover braces
    text = text.replace("{", " ").replace("}", " ")
    return text


def tidy(text: str) -> str:
    replacements = {
        "~": " ", "``": '"', "''": '"', "`": "'", "---": "—", "--": "–",
        "\\%": "%", "\\&": "&", "\\_": "_", "\\#": "#", "\\S": "§",
        "\\ldots": "…", "\\dots": "…", "\\textbackslash": "\\",
        "\\'e": "é", "\\'a": "á", "\\'i": "í", "\\'o": "ó", "\\'u": "ú",
        '\\"o': "ö", '\\"u': "ü", '\\"a': "ä", "\\ss": "ß", "\\c{c}": "ç",
        "\\ae": "ae", "\\&amp;": "&",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.strip() for line in text.splitlines()]
    # drop stray lines that carry no prose (single symbols, leftovers)
    kept = []
    for line in lines:
        if line.startswith("#"):
            kept.append(line)
            continue
        if len(line) < 25:
            continue
        if re.fullmatch(r"[^A-Za-z\u4e00-\u9fff]{0,30}", line):
            continue
        kept.append(line)
    return "\n\n".join(kept)


def pick_main(files: dict[str, str]) -> str:
    best_name, best_text, best_score = "", "", -1
    for name, text in files.items():
        score = 0
        if "\\documentclass" in text:
            score += 5
        if "\\begin{document}" in text:
            score += 5
        if "\\section" in text:
            score += 2
        score += min(len(text) // 20000, 3)
        if score > best_score:
            best_name, best_text, best_score = name, text, score
    return best_text


def resolve_inputs(text: str, files: dict[str, str], depth: int = 0) -> str:
    """Inline \\input{...} / \\include{...} using the other extracted .tex files."""
    if depth > 6:
        return text
    lookup = {name: content for name, content in files.items()}
    lookup.update(
        {Path(name).stem: content for name, content in files.items()}
    )

    def replace(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        candidates = [target, target + ".tex", Path(target).name]
        for candidate in candidates:
            if candidate in lookup:
                return resolve_inputs(lookup[candidate], files, depth + 1)
        return " "

    return re.sub(r"\\(?:input|include)\s*\{([^{}]+)\}", replace, text)


def body_of(text: str) -> str:
    match = re.search(r"\\begin\{document\}(.*?)\\end\{document\}", text, re.S)
    return match.group(1) if match else text


def main() -> None:
    SRC.mkdir(exist_ok=True)
    CLEAN.mkdir(exist_ok=True)
    ids = [
        line.split("\t")[3]
        for line in (WORK / "selected_papers.tsv").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for index, arxiv_id in enumerate(ids, 1):
        clean_path = CLEAN / f"{arxiv_id}.txt"
        src_path = SRC / f"{arxiv_id}.bin"
        if clean_path.exists() and clean_path.stat().st_size > 3000:
            print(f"[{index:02d}/{len(ids)}] cached {arxiv_id}", flush=True)
            continue
        try:
            blob = src_path.read_bytes() if src_path.exists() else download(arxiv_id)
            if not src_path.exists():
                src_path.write_bytes(blob)
            files = unpack(blob)
            if not files:
                print(f"[{index:02d}/{len(ids)}] no-latex {arxiv_id}", flush=True)
                time.sleep(4)
                continue
            text = pick_main(files)
            text = resolve_inputs(text, files)
            text = body_of(text)
            text = strip_comments(text)
            text = drop_environments(text)
            text = unwrap_commands(text)
            text = tidy(text)
            clean_path.write_text(
                f"# source: https://arxiv.org/abs/{arxiv_id}\n\n" + text,
                encoding="utf-8",
            )
            print(
                f"[{index:02d}/{len(ids)}] ok {arxiv_id} chars={len(text)}",
                flush=True,
            )
        except Exception as exc:
            print(f"[{index:02d}/{len(ids)}] ERROR {arxiv_id} -> {exc}", flush=True)
        time.sleep(4)


if __name__ == "__main__":
    main()
