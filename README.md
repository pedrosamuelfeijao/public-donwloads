# Downloads públicos — Lorde & CultoFlow

Este repositório público distribui **somente instaladores Windows, hashes SHA-256 e manifestos de versões**. O código-fonte, os bancos, as chaves de serviço e os repositórios de desenvolvimento continuam privados.

## Canais

| Produto | Agente Windows | Manifesto estável | Manifesto de teste |
| --- | --- | --- | --- |
| Lorde Hub | Lorde Agent | [Hub estável](updates/hub/stable.json) | [Hub teste](updates/hub/preview.json) |
| Lorde Compras | Lorde Agent (impressoras/peças) | [Compras estável](updates/compras/stable.json) | [Compras teste](updates/compras/preview.json) |
| CultoFlow | CultoFlow Agent (Holyrics) | [CultoFlow estável](updates/cultoflow/stable.json) | [CultoFlow teste](updates/cultoflow/preview.json) |

**Importante:** neste estágio o Lorde Hub e o Lorde Compras compartilham o mesmo programa **Lorde Agent**, mas cada painel poderá apresentar um botão independente de download e seu respectivo canal de atualização.

## Downloads sem login

Acesse a seção [**Releases**](https://github.com/pedrosamuelfeijao/public-donwloads/releases). Depois que a primeira publicação ocorrer, qualquer pessoa poderá baixar o `.exe` sem entrar no GitHub.

Para links permanentes de aplicativos, o painel deve consultar `updates/<produto>/stable.json` (ou `preview.json` para testes) e usar `installer.url`. **Não use** `/releases/latest`, pois esse endereço é único para o repositório, enquanto aqui existem três aplicativos.

## Publicar um instalador privado no repositório público

1. Crie um token GitHub **fine-grained**, autorizado exclusivamente a ler o conteúdo dos repositórios privados de origem `planejador-de-cultos` e `lorde-agent` (`Contents: Read-only`).
2. No repositório público, abra **Settings → Secrets and variables → Actions → New repository secret**. Cadastre `PRIVATE_RELEASE_READ_TOKEN`. **Nunca** salve ou publique esse token em arquivos, issues ou chats.
3. Abra **Actions → Publicar instalador** e use **Run workflow**.
4. Selecione `cultoflow`, `hub` ou `compras`; informe a tag exata da release privada, versão e canal `preview` ou `stable`.
5. O pipeline buscará **somente o instalador binário** na release privada, calculará SHA-256 e tamanho, criará uma release pública e atualizará o manifesto do aplicativo correspondente.

O canal `stable` rejeita uma release de origem marcada como pré-release. A distribuição de versões de teste requer `preview` e não altera os manifestos estáveis.

### Versões de origem localizadas inicialmente

- CultoFlow: release privada `agent-v0.5.2-build-34` (pré-release), `CultoFlowSetup.exe`.
- Lorde Agent: release privada `v0.4.0rc20` (release candidate), `LordeAgentSetup-0.4.0rc20.exe`.

Os instaladores **ainda não ficam públicos apenas com a criação deste repositório**: a primeira execução do workflow é necessária.

## Como o atualizador deve consumir o manifesto

1. Baixar o manifesto por HTTPS e confirmar `app_id` e `channel` exatos.
2. Comparar a versão instalada com `version` sem fazer downgrade.
3. Baixar o arquivo apenas do host `github.com` (página de release deste repositório), conferir `sha256` e `size_bytes`, e fazer verificação de assinatura quando houver certificado.
4. Instalar somente quando não houver OS, impressão ou culto em execução; pedir confirmação do operador, preservar dados em AppData e registrar resultado.
5. Após falha, oferecer recuperação/rollback para uma versão conhecida, sem baixar executáveis de URLs arbitrárias.

O manifesto sozinho **não habilita atualizações automáticas**: cada agente precisa implementar o consumo seguro desses dados.

> O nome do repositório contém a grafia original `public-donwloads`. Os endereços publicados preservam exatamente essa grafia.
