---
name: exegese-biblica
description: Consulta e analisa a Bíblia nos idiomas originais (hebraico, aramaico e grego), com tradução auxiliar em português. Use em estudos bíblicos, escatologia, arrebatamento, tribulação, teologia sistemática, comparação de versículos e perguntas sobre o sentido textual de passagens.
license: MIT para instruções; corpus sob licenças das fontes
compatibility: Leitura local de Markdown UTF-8; busca opcional via Python 3.9+
---

# Exegese bíblica baseada em textos identificados

Esta skill trabalha sobre um corpus **não inspiradamente reconstruído**: textos publicados em edições específicas. Siga o protocolo abaixo sempre que for ativada.

## Primeira leitura

1. Encontre o diretório raiz por meio do arquivo **INDICE.md**. Se a skill foi instalada isoladamente, peça acesso ao corpus ou use referências que o usuário forneça; não simule ter lido arquivos inexistentes.
2. Localize o livro no índice. Abra somente o capítulo relevante em **corpus/at/** (hebraico/arameu) ou **corpus/nt/** (grego). Utilize **corpus/pt/** para ajudar na compreensão, nunca como prova de literalidade do original.
3. Cite sempre identificador canônico e edição, como **Matt 24:29 (SBLGNT)**, **Dan 7:13 (WLC)**; se comparar a tradução, identifique-a como **Bíblia Livre 2018**.
4. Verifique o **contexto imediato**, o argumento do livro, o gênero literário e a cronologia narrativa; compare outras passagens pertinentes.

## Rigor de interpretação

- Identifique dados textuais observáveis antes de comentar teologia. Não apresente uma doutrina como se fosse tradução literal.
- Separe quatro camadas: **texto**, **tradução**, **contexto histórico-literário** e **interpretação**.
- Em profecias, distinga linguagem simbólica, literal e apocalíptica; não converta uma imagem automaticamente em calendário.
- Compare interpretações pré-tribulacionistas, mesotribulacionistas e pós-tribulacionistas sem assumir uma posição de antemão. Diga qual premissa hermenêutica sustenta cada leitura.
- Não deduza com certeza o que Deus 'teria de fazer' por lógica humana: explique o que um texto afirma, o que permite inferir e o que permanece controverso.
- Se a discussão depender de variante textual, consulte uma edição crítica/aparato adequado fora deste corpus e diga que aqui não há aparato exaustivo.
- Preservar grafia de nomes, sinais editoriais do grego e sinais vocálicos do hebraico; não normalizar caracteres silenciosamente.
- Não presumir equivalência 1:1 da numeração de Salmos, Joel e Malaquias entre WLC e português. Compare por conteúdo.
- Não atribua ao autor bíblico cabeçalhos modernos, títulos de seção ou notas deste projeto.

## Formato de resposta sugerido

1. **Pergunta e passagem:** referência e edição exatas.
2. **Evidência textual:** palavras relevantes em hebraico/arameu/grego, análise gramatical *com incertezas declaradas*.
3. **Tradução de trabalho:** português próprio, marcado como tradução e não como citação de versão protegida.
4. **Contexto:** autor, público, gênero, passagens paralelas, possíveis ecos do AT/NT.
5. **Interpretações concorrentes:** seus argumentos mais fortes e críticas justas.
6. **Síntese:** conclusão proporcional às evidências e questões não resolvidas.

## Ferramenta de consulta

Se disponível, rode `python3 scripts/buscar.py 'Rev 20:1' --colecao nt` (a partir da raiz). Buscas gregas/hebraicas são literais Unicode, com opção de comparação sem diacríticos quando necessário, mas isso NÃO substitui análise lexical.

Consulte **METODOLOGIA.md**, **QUALIDADE_E_LIMITES.md** e **FONTES_E_LICENCAS.md** antes de formular conclusões críticas.
