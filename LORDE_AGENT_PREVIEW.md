# Lorde Agent — versões de teste e cobertura por plataforma

**Revisado em 22/11/2026.** Esta página lista somente arquivos que estão
efetivamente disponíveis para baixar sem login. Novidades ainda em branch
de desenvolvimento não são anunciadas como funcionalidades do instalador.

## Disponibilidade do instalador para o Lorde Hub

As indicações de download Windows foram suspensas enquanto a correção de domínio
passa pelo aceite. A versão mínima para o Hub é **0.4.0rc25**.
O [manifesto preview](updates/hub/preview.json) voltará a indicar um instalador
quando houver uma versão homologada para teste, com link e SHA-256.

### macOS Intel (x86_64) e Apple Silicon (arm64)

- **Versão completa com integração renovada: indisponível para download
  público neste momento.** Não apresentar os ZIPs antigos do Mac Lite
  como equivalentes ao Agent completo.
- Em desenvolvimento e homologação: pareamento com o Hub,
  coleta USB, leitura profunda, catálogo de modelos, ilustrações e Panic Full.
- Ainda é necessário construir, validar e publicar os pacotes por arquitetura.
  A tentativa de upload pelo GitHub Actions falhou por cota de armazenamento.
- **Não** exigir que o técnico desative proteções do macOS para instalar
  aplicativo não assinado. A assinatura/notarização Apple está pendente.

## Matriz de funções

| Função | Windows 0.4.0rc23 público | Windows com alterações pendentes | Mac Intel/Apple Silicon em desenvolvimento |
| --- | --- | --- | --- |
| Leitura USB de iPhone e iPad | Presente; validar em bancada | Reutilizada | Integrada ao código, sem aceite físico final |
| Coleta técnica: serial, IMEI, bateria, armazenamento, cor | Presente quando iOS permite | Mantida | Integrada ao código, sem aceite físico final |
| Catálogo de 178 identificadores Apple | Não incluído nessa release | Implementado em branch | Implementado em branch |
| 33 ilustrações padronizadas | Não incluídas nessa release | Implementadas em branch | Implementadas em branch |
| Pareamento por código com o Hub | Presente | Mantido | Implementado no código; validar com Hub real |
| Envio de eventos e heartbeat | Presente | Mantido | Implementado no código; validar com Hub real |
| Panic Full local | Presente | Mantido | Previsto no código; validar USB em Mac real |
| Resumo Panic Full na verificação do Hub | Depende de contrato/aceite do Hub | Fluxo precisa de teste fim a fim | Envio automático de resumo ainda pendente |
| Autoatualização segura, instalada automaticamente | Mecanismo assinado exige chave de confiança | Pendente de ativação e testes | Ainda não implementada |
| Downloads públicos do novo instalador | Disponível apenas a versão anterior | Novo build pendente | Novos builds pendentes |
| Impressão/rastreamento/WhatsApp | Recursos específicos podem existir | Mantidos no Windows | Não fazem parte do escopo solicitado |

**Atenção:** dados técnicos não garantem leitura completa em todos os iOS.
O Agent deve expor dados indisponíveis sem inventá-los.

## Roteiro de feedback de bancada

1. Identificar versão e arquitetura do sistema.
2. Parear pelo código do Lorde Hub; verificar se o computador aparece online.
3. Conectar iPhone por USB, permitir confiança e conferir nome do modelo,
   serial, armazenamento, bateria e cor (quando disponibilizados pelo iOS).
4. Verificar a ilustração correspondente **quando o novo build estiver publicado**.
5. Testar coleta Panic Full e conferir se o resumo aparece em Verificação
   **apenas após a integração ser concluída**.
6. Desconectar/reconectar USB e internet, testar fila e reiniciar o aplicativo.
7. Registrar prints, versão, modelo iPhone/ProductType, iOS e mensagens de erro.
   Ocultar seriais, IMEIs e dados pessoais nas evidências compartilhadas.

Esta página não cria release nem ativa atualização automática.
