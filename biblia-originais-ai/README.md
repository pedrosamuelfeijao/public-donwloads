# Bíblia Originais AI

**Corpus bíblico público, em Markdown UTF-8, preparado para consultas e exegese assistida por IA.**

Esta edição contém os **66 livros do cânon protestante**, organizados em **132 arquivos de texto bíblico**: 39 do Antigo Testamento (hebraico/arameu), 27 do Novo Testamento (grego koiné) e 66 traduções de apoio em português.

## Comece aqui

- [Índice de todos os livros](INDICE.md)
- [Skill reutilizável para agentes](skills/exegese-biblica/SKILL.md)
- [Orientações para IAs que acessam esta pasta](AGENTS.md)
- [Método e limites históricos](METODOLOGIA.md)
- [Fontes, licenças e atribuições](FONTES_E_LICENCAS.md)
- [Cuidados e problemas identificados](QUALIDADE_E_LIMITES.md)

## Organização

- **corpus/at/** — 39 livros na tradição massorética, edição WLC/OSHB; inclui trechos originalmente em aramaico.
- **corpus/nt/** — 27 livros no texto grego crítico SBLGNT, com sinais editoriais conservados.
- **corpus/pt/** — tradução de apoio Bíblia Livre (2018), isolada dos textos originais.
- **skills/exegese-biblica/** — instruções reutilizáveis, formato Agent Skills.
- **scripts/buscar.py** — consulta textual ou por referência, sem bibliotecas externas.
- **scripts/validar.py** — valida arquivos, identificação dos versículos e contagem dos livros.

## Exemplo rápido

Use Python 3.9+ e execute a partir desta pasta:

```bash
python3 scripts/buscar.py 'Matt 24:29' --colecao nt
python3 scripts/buscar.py 'παρουσία' --colecao nt --limite 10
python3 scripts/buscar.py 'Gen 1:1' --colecao at
python3 scripts/validar.py
```

## Instalação da skill

Copie a pasta **skills/exegese-biblica/** para o diretório de skills suportado pelo seu agente e mantenha o corpus acessível. O arquivo SKILL.md contém as regras da consulta; sua presença no GitHub **não ativa automaticamente** um plugin no ChatGPT, Claude ou Codex.

## Critério científico e textual

Não temos os autógrafos originais da Bíblia. O WLC é uma edição da tradição massorética baseada em manuscrito medieval; o SBLGNT é uma edição crítica moderna do grego. Eles não são 'a cópia original' e não encerram todas as variantes manuscritas. A tradução portuguesa é secundária. Nenhuma conclusão escatológica deve ser tratada como fato textual incontroverso sem mostrar a passagem, o idioma, a edição e as interpretações alternativas.

**Escopo:** Bíblia protestante de 66 livros; outros cânones e testemunhos (Septuaginta, Manuscritos do Mar Morto, Pentateuco Samaritano, Vulgata, NA28/UBS5) são referências de comparação, **não incluídas** neste corpus.

**Licenças:** o código e as instruções deste projeto têm licença MIT; **os textos bíblicos mantêm suas licenças originais**, detalhadas em [FONTES_E_LICENCAS.md](FONTES_E_LICENCAS.md).

**Versão pública inicial:** 1.0.0. Textos de origem identificados por revisão fixa para auditoria.
