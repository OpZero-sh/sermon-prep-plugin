"""Build reproducible Agent Plugins packages from this repository's product sources."""
import argparse
import json
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "integrations" / "openai"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/"

def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()

def build(output):
    manifest = json.loads((CONFIG / "plugin.json").read_text())
    mcp = json.loads((CONFIG / "mcp.json").read_text())
    entries = mcp["mcpServers"]
    product = manifest["name"]
    icon = (ROOT / "assets" / "icon.png").read_bytes()
    if icon[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Expected a PNG product icon at assets/icon.png")
    shared = {"assets/icon.png": icon, "LICENSE": (ROOT / "LICENSE").read_bytes()}
    skills = {path.relative_to(ROOT).as_posix(): path.read_bytes()
              for path in sorted((ROOT / "skills").rglob("*")) if path.is_file()}
    output.mkdir(parents=True, exist_ok=True)

    def archive(name, metadata, servers, skills_to_include):
        files = dict(shared, **skills_to_include)
        files["plugin.json"] = json_bytes(metadata)
        files["mcp.json"] = json_bytes({"$schema": SCHEMA + "mcp.schema.json", "mcpServers": servers})
        target = output / (name + ".zip")
        temp = target.with_suffix(".zip.tmp")
        with ZipFile(temp, "w", compression=ZIP_STORED) as bundle:
            for filename, contents in sorted(files.items()):
                entry = ZipInfo(filename, (1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                bundle.writestr(entry, contents)
        temp.replace(target)
        print(target)

    archive(product, manifest, entries, skills)
    if len(entries) > 1:
        for key, entry in entries.items():
            component = CONFIG / "components" / key
            metadata = json.loads((component / "plugin.json").read_text())
            focused_skill = (component / "SKILL.md").read_bytes()
            archive(product + "--" + key, metadata, {key: entry},
                    {f"skills/use-{key}/SKILL.md": focused_skill})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Output directory for ZIP files")
    build(parser.parse_args().output)
