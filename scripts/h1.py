import pathlib

root = pathlib.Path(".")

for path in root.rglob("*.md"):
    if path.name == "index.md":
        continue
    text = path.read_text().lstrip()

    if not text.startswith("##") and text.startswith("#"):
        continue

    title = path.stem.replace("_", " ")
    text = f"# {title}\n\n" + text

    path.write_text(text)
