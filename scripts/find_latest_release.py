#!/usr/bin/env python3
"""Select a newer private release for ONE app/channel, without downloading any source."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from generate_manifest import sort_key


def newest(app: str, channel: str, published: list[dict], current: dict) -> tuple[str,str] | None:
    if app not in {"hub","compras","cultoflow"} or channel not in {"preview","stable"}:
        raise ValueError("Unknown channel")
    options=[]
    for row in published:
        if not isinstance(row,dict):
            continue
        tag=row.get("tagName")
        prerelease=row.get("isPrerelease")
        if not isinstance(tag,str) or type(prerelease) is not bool:
            continue
        if app=="cultoflow":
            match=re.fullmatch(r"agent-v(\d+\.\d+\.\d+)-build-(\d+)",tag)
        else:
            match=re.fullmatch(r"v(\d+\.\d+\.\d+(?:(?:a|b|rc|dev)\d+)?)",tag)
        if not match:
            continue
        version=match.group(1)
        is_test=prerelease or bool(re.search(r"(a|b|rc|dev)\d+$",version))
        if channel=="stable" and is_test:
            continue
        if channel=="preview" and not is_test:
            continue
        key=sort_key(version)
        options.append((key,int(match.group(2)) if app=="cultoflow" else 0,tag,version))
    if not options:
        return None
    selected=max(options)
    existing=current.get("version") if current.get("available") else None
    if existing is not None and selected[0]<=sort_key(str(existing)):
        return None
    return selected[2],selected[3]


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--app",required=True)
    parser.add_argument("--channel",required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    args=parser.parse_args()
    published=json.load(sys.stdin)
    current=json.loads(args.manifest.read_text(encoding="utf-8"))
    result=newest(args.app,args.channel,published,current)
    if result:
        print(result[0]+"\t"+result[1])


if __name__=="__main__":
    main()
