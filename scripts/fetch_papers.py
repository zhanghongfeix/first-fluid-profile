"""
从 arXiv 抓取流体力学相关最新论文，生成 Markdown 文件。

数据源：
  - physics.flu-dyn  (流体动力学 — 主类别)
  - physics.comp-ph  (计算物理 — CFD 方法)
  - physics.ao-ph    (大气海洋物理 — 地球物理流体)

依赖：pip install arxiv
"""

import arxiv
import datetime
import os
import re
import sys

# ── 配置 ─────────────────────────────────────────────
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIES = [
    "physics.flu-dyn",
    "physics.comp-ph",
    "physics.ao-ph",
]

# 研究方向关键词 → 分类 (用于自动打标签)
TAG_KEYWORDS = {
    "湍流": ["turbulence", "turbulent", "LES", "DNS", "RANS", "eddy"],
    "CFD": ["CFD", "computational fluid", "numerical simulation", "finite volume",
            "finite element", "lattice boltzmann", "immersed boundary", "spectral method"],
    "空气动力学": ["aerodynamic", "airfoil", "wing", "drag reduction", "supersonic",
                   "hypersonic", "transonic", "shock wave", "compressible flow"],
    "水动力学": ["hydrodynamic", "ship", "wave", "free surface", "cavitation",
                 "water entry", "sloshing", "offshore", "marine"],
    "多相流": ["multiphase", "bubble", "droplet", "particle-laden", "two-phase",
               "spray", "atomization", "emulsion", "fluidized bed"],
    "微流体": ["microfluidic", "microchannel", "lab-on-a-chip", "electrokinetic",
               "electrowetting", "capillary"],
    "生物流体力学": ["biofluid", "blood flow", "cardiovascular", "respiratory",
                     "swimming", "flying", "insect flight", "fish swimming"],
    "环境流体力学": ["atmospheric boundary layer", "ocean", "stratified",
                     "convection", "plume", "pollutant dispersion", "urban flow"],
    "反应流": ["combustion", "reacting flow", "flame", "detonation", "ignition",
               "chemical reaction", "soot"],
    "流动稳定性": ["instability", "transition", "linear stability",
                   "Rayleigh", "Kelvin-Helmholtz", "Richtmyer-Meshkov"],
}


def today_str():
    return datetime.date.today().strftime("%Y-%m-%d")


def target_file_path(date_str):
    """papers/YYYY/MM/YYYY-MM-DD.md 的绝对路径"""
    year = date_str[:4]
    month = date_str[5:7]
    return os.path.join(REPO_ROOT, "papers", year, month, f"{date_str}.md")


def ensure_dir(fp):
    os.makedirs(os.path.dirname(fp), exist_ok=True)


def tag_paper(title, summary):
    """根据标题和摘要自动打研究方向标签"""
    text = (title + " " + summary).lower()
    tags = []
    for tag, keywords in TAG_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text:
                tags.append(f"`{tag}`")
                break
    return " ".join(tags) if tags else "—"


def extract_doi(entry):
    """从 arxiv 结果中提取 DOI（如果有）"""
    doi = getattr(entry, "doi", None)
    if doi:
        return doi
    # 有些文章用 comment 字段存 DOI
    comment = getattr(entry, "comment", "")
    if comment and "doi" in comment.lower():
        match = re.search(r"doi[:\s]*([^\s,]+)", comment, re.IGNORECASE)
        if match:
            return match.group(1)
    return None


def fetch_papers(date_str=None):
    """
    抓取论文并写入 Markdown。

    返回 (filepath, paper_count)
    """
    if date_str is None:
        date_str = today_str()

    lookback = datetime.date.today() - datetime.timedelta(days=3)

    client = arxiv.Client(page_size=100, delay_seconds=3.0)

    papers = []
    seen_ids = set()

    for cat in CATEGORIES:
        search = arxiv.Search(
            query=f"cat:{cat}",
            sort_by=arxiv.SortCriterion.SubmittedDate,
            max_results=100,
        )
        try:
            results = list(client.results(search))
        except Exception as e:
            print(f"[WARN] 类别 {cat} 查询失败: {e}", file=sys.stderr)
            continue

        for r in results:
            pid = r.get_short_id()
            if pid in seen_ids:
                continue
            seen_ids.add(pid)

            pub_date = r.published.date()
            if pub_date < lookback:
                continue

            doi = extract_doi(r)
            authors = ", ".join(a.name for a in r.authors[:5])
            if len(r.authors) > 5:
                authors += " et al."

            papers.append({
                "id": pid,
                "title": r.title.strip().replace("\n", " "),
                "authors": authors,
                "date": pub_date.isoformat(),
                "abstract": r.summary.strip().replace("\n", " "),
                "url": r.entry_id,
                "doi": doi,
                "category": r.primary_category,
                "tags": tag_paper(r.title, r.summary),
            })

    # 按日期降序排列
    papers.sort(key=lambda p: p["date"], reverse=True)

    # ── 生成 Markdown ───────────────────────────────────
    out_path = target_file_path(date_str)
    ensure_dir(out_path)

    lines = [
        f"# {date_str}",
        "",
        f"> arXiv `{'`, `'.join(CATEGORIES)}` 最新论文  ·  共 {len(papers)} 篇",
        "",
    ]

    if not papers:
        lines.append("_未找到昨日至今的新论文。_")
    else:
        for i, p in enumerate(papers, 1):
            links = f"[📄 arXiv]({p['url']})"
            if p["doi"]:
                links += f" · [🔗 DOI](https://doi.org/{p['doi']})"

            lines += [
                f"### {i}. {p['title']}",
                "",
                f"**{p['authors']}** · {p['date']}",
                "",
                f"研究方向：{p['tags']}",
                "",
                f"> {p['abstract'][:500]}",
                "",
                f"{links}",
                "",
                "---",
                "",
            ]

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[OK] 写入 {out_path}  ({len(papers)} 篇论文)")
    return out_path, len(papers)


def update_paper_index(date_str):
    """更新 papers/README.md 索引"""
    readme_path = os.path.join(REPO_ROOT, "papers", "README.md")
    entry = f"- [{date_str}]({date_str[:4]}/{date_str[5:7]}/{date_str}.md)"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if entry not in content:
        # 插入到第一个日期条目之前
        marker = "## 2026"
        if marker in content:
            content = content.replace(
                marker,
                f"{marker}\n\n{entry}",
            )
        else:
            # 没有 2026 年标题，追加到末尾
            content += f"\n{entry}\n"

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] 更新索引 {readme_path}")


# ── 主入口 ─────────────────────────────────────────────
if __name__ == "__main__":
    ds = today_str()
    if len(sys.argv) > 1:
        ds = sys.argv[1]  # 允许手动传日期：python fetch_papers.py 2026-05-15

    filepath, count = fetch_papers(ds)
    if count > 0:
        update_paper_index(ds)
