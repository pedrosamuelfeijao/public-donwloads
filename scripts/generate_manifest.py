#!/usr/bin/env python3
"""Validate release metadata and prepare a public app-specific update manifest."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO = "pedrosamuelfeijao/public-donwloads"
APPS = {"cultoflow": "CultoFlow", "hub": "Lorde Hub", "compras": "Lorde Compras"}
CHANNELS = {"stable", "preview"}
VERSION = re.compile(r"^[0-9]+(?:\.[0-9]+){1,3}(?:(?:a|b|rc|dev)[0-9]+)?$", re.I)
SOURCE_TAG = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{1,100}$")

def sort_key(version: str):
    match = re.fullmatch(r"(\d+(?:\.\d+){1,3})(?:(a|b|rc|dev)(\d+))?", version, re.I)
    if not match:
        raise ValueError("Unsupported version format: " + version)
    numbers = tuple(int(x) for x in match[1].split("."))
    numbers = (numbers + (0, 0, 0, 0))[:4]
    suffix = match[2].lower() if match[2] else ""
    # Stable is newer than any prerelease with the same numeric portion.
    return (*numbers, {"dev": 0, "a": 1, "b": 2, "rc": 3, "": 4}[suffix], int(match[3] or 0))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--app", choices=sorted(APPS), required=True)
    p.add_argument("--channel", choices=sorted(CHANNELS), required=True)
    p.add_argument("--version", required=True)
    p.add_argument("--source-tag", required=True)
    p.add_argument("--source-installer", type=Path, required=True)
    p.add_argument("--public-installer", type=Path, required=True)
    a = p.parse_args()
    if not VERSION.fullmatch(a.version) or not SOURCE_TAG.fullmatch(a.source_tag):
        raise ValueError("Invalid version or tag")
    if a.channel == "stable" and re.search(r"(dev|a|b|rc)\d+$", a.version, re.I):
        raise ValueError("Release candidate cannot be stable")
    source = a.source_installer
    if not source.is_file() or source.stat().st_size < 1024 * 1024 or source.stat().st_size > 300 * 1024 * 1024:
        raise ValueError("Missing or invalid installer (1-300 MiB)")
    public = a.public_installer
    public.parent.mkdir(parents=True, exist_ok=True)
    if public.exists():
        raise ValueError("Public release file already exists")
    digest = hashlib.sha256()
    with source.open("rb") as incoming, public.open("xb") as outgoing:
        for chunk in iter(lambda: incoming.read(4 * 1024 * 1024), b""):
            digest.update(chunk)
            outgoing.write(chunk)
    sha = digest.hexdigest()
    tag = f"{a.app}-{a.channel}-v{a.version}"
    manifest_file = Path("updates") / a.app / f"{a.channel}.json"
    old = json.loads(manifest_file.read_text(encoding="utf-8"))
    if old.get("available"):
        if sort_key(a.version) <= sort_key(old["version"]):
            raise ValueError("Version must advance, never overwrite or downgrade " + a.app)
    data = {
        "schema_version": 1, "app_id": a.app, "channel": a.channel, "available": True,
        "version": a.version, "release_tag": tag,
        "published_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "installer": {
            "name": public.name,
            "url": f"https://github.com/{REPO}/releases/download/{tag}/{public.name}",
            "sha256": sha, "size_bytes": public.stat().st_size
        }
    }
    manifest_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    Path("publish/release_metadata.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"{a.app}/{a.channel}: {a.version}; SHA256={sha}; bytes={public.stat().st_size}")

if __name__ == "__main__":
    main()
