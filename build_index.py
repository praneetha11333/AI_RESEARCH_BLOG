from pathlib import Path


ROOT = Path(__file__).parent
POSTS_DIR = ROOT / "docs" / "posts"
INDEX_FILE = ROOT / "docs" / "index.md"


def post_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


posts = sorted(POSTS_DIR.glob("*.md"), reverse=True)
lines = [
    "# Daily AI Brief",
    "",
    "Short, useful AI news for students. "
    "A research agent creates one cited digest every morning.",
    "",
    "## Latest posts",
    "",
]

if posts:
    for post in posts:
        date = post.name[:10]
        lines.append(f"- **{date}** — [{post_title(post)}](posts/{post.name})")
else:
    lines.append("_No digest has been generated yet._")

INDEX_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Indexed {len(posts)} post(s)")