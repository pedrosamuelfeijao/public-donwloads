#!/usr/bin/env python3
"""Validação de integridade estrutural do corpus. Não é uma crítica textual."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSE = re.compile(r"^\*\*([A-Za-z0-9]+)\s+(\d+):(\d+)\*\*\s+(.+)$")
EXPECTED = {"at": 39, "nt": 27, "pt": 66}
SPECIAL = {"21-eclesiastes.md": 222, "22-canticos.md": 117, "39-malaquias.md": 55}

def check_file(path: Path) -> tuple[int, list[str]]:
    errors, keys, chapters = [], set(), set()
    verses = 0
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("**"):
            continue
        m = VERSE.fullmatch(line)
        if m is None:
            errors.append(f"{path.name}:{number}: linha de versículo inválida")
            continue
        book, chapter, verse, text = m.groups()
        key = (book, int(chapter), int(verse))
        if not text.strip():
            errors.append(f"{path.name}:{number}: texto vazio")
        if key in keys:
            errors.append(f"{path.name}:{number}: referência duplicada: {key}")
        keys.add(key)
        chapters.add(int(chapter))
        verses += 1
    if verses == 0:
        errors.append(f"{path.name}: nenhum versículo encontrado")
    if chapters and chapters != set(range(1, max(chapters) + 1)):
        errors.append(f"{path.name}: capítulos não contíguos")
    return verses, errors

def main() -> int:
    errors, sums = [], {}
    for folder, expected in EXPECTED.items():
        files = sorted((ROOT / "corpus" / folder).glob("*.md"))
        if len(files) != expected:
            errors.append(f"{folder}: {len(files)} livros, esperado {expected}")
        total = 0
        for file in files:
            n, errs = check_file(file)
            total += n
            errors.extend(errs)
            if folder == "at" and file.name in SPECIAL and n != SPECIAL[file.name]:
                errors.append(f"{file.name}: {n} versículos, esperado {SPECIAL[file.name]}")
        sums[folder] = total
    if sums.get("nt") != 7939:
        errors.append(f"nt: {sums.get('nt')} versículos, esperado 7939 para esta edição")
    print("Resumo por coleção:", sums)
    if errors:
        for error in errors:
            print("ERRO:", error, file=sys.stderr)
        print(f"Falha: {len(errors)} erro(s)", file=sys.stderr)
        return 1
    print("VALIDAÇÃO ESTRUTURAL OK. Este teste não substitui colação textual.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
