# Atalhos Dr. Padel (Espanso)

Mensagens padrão aos clientes como atalhos de teclado, em qualquer app (WhatsApp, Kommo, Gmail...).

- PT: `;nome` - EN: `;nomeen` - ES: `;nomees`
- Escreve o atalho e carrega em **espaço**.
- Lista completa: [LISTA.md](LISTA.md)
- Ver todos no Mac: `Option + Espaço` abre a pesquisa do Espanso.

## Instalar num Mac (uma vez)

1. Instalar o Espanso: https://espanso.org (e abri-lo).
2. Colar no Terminal:

```
mkdir -p ~/Library/Application\ Support/espanso/match && git clone https://github.com/drpadelracket/atalhos ~/Library/Application\ Support/espanso/match/drpadel && bash ~/Library/Application\ Support/espanso/match/drpadel/instalar.sh
```

Depois disto atualiza-se sozinho de 10 em 10 minutos.

## Alterar mensagens

A fonte é a tabela **MENSAGENS** (base ESCRI, Airtable). Quando se corrige uma mensagem lá, atualiza-se também `gerar.py` e corre-se `python3 gerar.py`, que gera `mensagens.yml` e `LISTA.md`. Não editar `mensagens.yml` à mão.
