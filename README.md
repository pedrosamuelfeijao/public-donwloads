# Central pública de downloads — Lorde & CultoFlow

Instaladores oficiais de Windows publicados **sem exigir login no GitHub**. Os repositórios com código-fonte, dados, segredos e pipelines de desenvolvimento continuam privados.

## Baixar agora

| Aplicativo | Download direto (canal de testes) | Versão | Tamanho |
| --- | --- | --- | --- |
| **Lorde Hub** | [Baixar Lorde Agent para Hub](https://github.com/pedrosamuelfeijao/public-donwloads/releases/download/hub-preview-v0.4.0rc20/LordeAgentSetup-0.4.0rc20.exe) | 0.4.0rc20 | ~100 MB |
| **Lorde Compras** | [Baixar Lorde Agent para Compras](https://github.com/pedrosamuelfeijao/public-donwloads/releases/download/compras-preview-v0.4.0rc20/LordeAgentSetup-0.4.0rc20.exe) | 0.4.0rc20 | ~100 MB |
| **CultoFlow** | [Baixar CultoFlow Agent](https://github.com/pedrosamuelfeijao/public-donwloads/releases/download/cultoflow-preview-v0.5.3/CultoFlowSetup-0.5.3.exe) | 0.5.3 | ~46 MB |

Hub e Compras usam **o mesmo Lorde Agent** com diferentes recursos e integrações, mas possuem canais de distribuição separados. Esses são builds de testes; não são releases estáveis definitivas. Consulte também [todas as Releases](https://github.com/pedrosamuelfeijao/public-donwloads/releases).

## Links permanentes para sites e atualizadores

Não use `/releases/latest`, pois um mesmo repositório contém vários produtos. Para sempre obter a versão correta, consulte os manifestos independentes:

| Produto | Canal de testes | Canal estável |
| --- | --- | --- |
| Hub | [Manifesto Hub](updates/hub/preview.json) | [Estável](updates/hub/stable.json) |
| Compras | [Manifesto Compras](updates/compras/preview.json) | [Estável](updates/compras/stable.json) |
| CultoFlow | [Manifesto CultoFlow](updates/cultoflow/preview.json) | [Estável](updates/cultoflow/stable.json) |

O manifesto traz a URL pública, versão, tamanho e SHA-256. Um cliente deve confirmar `app_id`, `channel`, URL permitida, versão crescente e integridade antes de instalar qualquer executável. Manifestos que anunciam `available: false` não devem ser tratados como atualização.

## Publicação automática

O GitHub Actions [**Procurar novas versões privadas**](.github/workflows/discover-updates.yml) consulta releases privadas a cada seis horas por aplicativo, usando o secret já configurado `PRIVATE_RELEASE_READ_TOKEN`, exclusivamente para leitura. Só gera um novo pedido quando identifica avanço de versão.

O workflow [**Publicar instalador**](.github/workflows/publish-installer.yml) lê apenas o instalador binário da release privada, valida os checksums originais quando disponíveis, gera uma Release pública do produto/canal e atualiza o manifesto correspondente.

Ambos têm [testes automatizados](.github/workflows/validate-manifests.yml). A publicação manual pelo workflow continua disponível para uma promoção controlada.

**Regra de segurança:** versões rc/a/b/dev não entram no canal estável. O sistema não sobrescreve instaladores de versões já publicadas nem faz downgrade. Nunca publique tokens nem código privado neste repositório.

## Atualizações dentro dos agentes

- **CultoFlow Agent 0.5.3+:** verifica atualizações públicas automaticamente na inicialização e periodicamente. Quando existir versão superior, oferece instalação confirmada em um clique, com SHA-256 e bloqueio durante preparo de culto. Preserva as configurações do perfil Windows.
- **Lorde Agent (Hub/Compras):** possui mecanismo independente de atualização assinada, mas a chave pública de confiança da instalação ainda precisa ser provisionada para ativar a atualização automática completa. **Até lá, use os downloads públicos oficiais e o instalador normal**, sem contornar a validação criptográfica.

O GitHub pode avisar que o executável não é assinado por certificado Authenticode. SHA-256 comprova a correspondência com o manifesto, mas não substitui uma assinatura de código confiável.

> Nome real do repositório: `public-donwloads` (grafia preservada nos endereços).
