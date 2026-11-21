#!/usr/bin/env python3
"""Busca literal ou por referência no corpus bíblico Markdown. Requer Python 3.9+."""
from __future__ import annotations
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSE = re.compile(r"^\*\*([A-Za-z0-9]+)\s+(\d+):(\d+)\*\*\s+(.+)$")
REF = re.compile(r"^([1-3]?[A-Za-z]+)\s+(\d+):(\d+)$", re.I)

def normalizar(value: str, ignorar_marcas: bool) -> str:
    value = value.casefold()
    if ignorar_marcas:
        value = "".join(
            ch for ch in unicodedata.normalize("NFD", value)
            if unicodedata.category(ch) != "Mn"
        )
    return value

def main() -> int:
    p = argparse.ArgumentParser(description="Consultar a Bíblia em Markdown por texto ou código:capítulo:verso")
    p.add_argument("consulta", help="Ex.: 'Matt 24:29', 'παρουσία', 'יְהוָה', 'arrebatamento'")
    p.add_argument("--colecao", choices=("at", "nt", "pt", "todos"), default="todos",
                   help="at=hebraico, nt=grego, pt=tradução; default: todos")
    p.add_argument("--limite", type=int, default=20, help="Máximo de resultados (padrão 20)")
    p.add_argument("--sem-diacriticos", action="store_true", help="Busca aproximada, ignora marcas vocálicas/acento")
    p.add_argument("--json", action="store_true", help="Saída em JSON")
    args = p.parse_args()
    if args.limite < 1:
        p.error("--limite deve ser maior que zero")
    consulta = args.consulta.strip()
    ref = REF.fullmatch(consulta)
    if not consulta:
        p.error("A consulta não pode estar vazia")
    folders = ("at", "nt", "pt") if args.colecao == "todos" else (args.colecao,)
    resultados = []
    termo = normalizar(consulta, args.sem_diacriticos)
    for pasta in folders:
        directory = ROOT / "corpus" / pasta
        if not directory.is_dir():
            print(f"ERRO: corpus indisponível: {directory}", file=sys.stderr)
            return 2
        for path in sorted(directory.glob("*.md")):
            for line in path.read_text(encoding="utf-8").splitlines():
                m = VERSE.match(line)
                if not m:
                    continue
                codigo, cap, ver, texto = m.groups()
                if ref:
                    ok = (codigo.casefold() == ref[1].casefold()
                          and int(cap) == int(ref[2]) and int(ver) == int(ref[3]))
                else:
                    ok = termo in normalizar(texto, args.sem_diacriticos)
                if ok:
                    resultados.append({
                        "referencia": f"{codigo} {cap}:{ver}",
                        "colecao": pasta, "arquivo": str(path.relative_to(ROOT)),
                        "texto": texto,
                    })
                    if len(resultados) >= args.limite:
                        break
            if len(resultados) >= args.limite:
                break
        if len(resultados) >= args.limite:
            break
    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            print(f"[{r['colecao']}] {r['referencia']}: {r['texto']}")
        print(f"Resultados: {len(resultados)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
