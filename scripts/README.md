# 🛠️ Scripts da Temporada 2029 - Corinthians

Scripts utilitários para adicionar resultados de partidas no projeto.

---

## 📝 Adicionar Resultados

### ✅ **Modo Individual** (1 resultado por vez)

Adicione um único resultado:

```bash
python add_result.py "🟢 Corinthians 3 x 1 Palmeiras" --competicao brasileirao-serie-a
```

**Exemplos:**

```bash
# Brasileirão Série A
python add_result.py "🟢 Corinthians 2 x 1 Flamengo" --competicao brasileirao-serie-a

# Copa Libertadores
python add_result.py "🔴 Boca Juniors 3 x 1 Corinthians" --competicao copa-libertadores-2029

# Copa do Brasil
python add_result.py "⚪ Goiás 2 x 2 Corinthians" --competicao copa-do-brasil
```

---

### 🚀 **Modo Batch** (vários resultados de uma vez)

Adicione múltiplos resultados em um único comando, separados por ponto e vírgula:

```bash
python add_result.py "🟢 Jogo 1;🔴 Jogo 2;⚪ Jogo 3" --competicao brasileirao-serie-a
```

**Exemplo com vários resultados:**

```bash
python add_result.py \
    "🟢 Corinthians 2 x 1 Flamengo;⚪ Botafogo 1 x 1 Palmeiras;🔴 São Paulo 3 x 0 Corinthians;🟢 Cruzeiro 0 x 2 Corinthians" \
    --competicao brasileirao-serie-a
```

**Resultado:** Adiciona **4 jogos novos** no HTML de uma só vez! ✅

---

## 📂 Competições Disponíveis

| Competição | Arquivo Atualizado | Pastas de Logos |
|------------|-------------------|-----------------|
| `brasileirao-serie-a` | `index.html` | `.\\brasileirao-serie-a\\` |
| `copa-libertadores-2029` | `copa-libertadores-2029.html` | `.\\libertadores\\` |
| `copa-do-brasil` | `copa-do-brasil.html` | `.\\brasileirao-serie-a\\` |

---

## 🎯 Formato do Resultado

Use este formato para cada resultado:

```
[EMOJI] [TIME-CASA] [PLACAR-CASA] x [PLACAR-VISITANTE] [TIME-VISITANTE]
```

### Emojis Disponíveis:

| Emoji | Significado | Classe HTML |
|-------|-------------|--------------|
| `🟢` | Vitória do Time da Casa | `indicator-victory` |
| `⚪` | Empate | `indicator-draw` |
| `🔴` | Derrota do Time da Casa (Vitória do Visitante) | `indicator-defeat` |

### Exemplos Válidos:

```bash
# Vitória em casa
python add_result.py "🟢 Corinthians 3 x 1 Flamengo" --competicao brasileirao-serie-a

# Empate
python add_result.py "⚪ Corinthians 2 x 2 Palmeiras" --competicao brasileirao-serie-a

# Derrota em casa
python add_result.py "🔴 Corinthians 0 x 2 Santos" --competicao brasileirao-serie-a
```

---

## 📋 Estrutura de Pastas

```
temporada-2029/
├── scripts/
│   ├── add_result.py      # Script principal
│   └── README.md          # Este arquivo
├── index.html             # Brasileirão Série A
├── copa-libertadores-2029.html
└── copa-do-brasil.html

brasileirao-serie-a/       # Logos do Brasileirão
libertadores/              # Logos da Libertadores
copa-do-brasil/            # Logos da Copa do Brasil
```

---

## 💡 Dicas

1. **Sempre use o emoji correto** - O script gera automaticamente a classe HTML baseada no placar, mas você pode especificar para clareza.

2. **Ordem dos jogos** - Novos resultados são sempre adicionados ao final da lista (mais recente).

3. **Logos automáticos** - O script detecta o nome do time e gera automaticamente o path do logo correto.

4. **Batch é mais rápido** - Para adicionar muitos jogos de uma vez, use o modo batch.

---

## ⚠️ Notas Importantes

- Os logs dos logos estão organizados por competição nas pastas correspondentes.
- Se um logo não for encontrado automaticamente, você pode precisar adicioná-lo manualmente na pasta correta.
- O script mantém a estrutura HTML existente e apenas insere novos jogos após o último registrado.

---

## 🔧 Uso Avançado (Modo Batch Explícito)

```bash
python add_result.py \
    --batch \
    --results "🟢 Jogo A;🔴 Jogo B;⚪ Jogo C" \
    --competicao brasileirao-serie-a
```

Isso é útil quando você quer separar claramente os resultados entre si.

---

## 📊 Exemplo de Sessão Completa

```bash
# Adicionando 3 jogos do Brasileirão de uma vez:
python add_result.py \
    "🟢 Corinthians 2 x 1 Flamengo;⚪ Botafogo 1 x 1 Palmeiras;🔴 São Paulo 3 x 0 Corinthians" \
    --competicao brasileirao-serie-a

# Output esperado:
✅ 3 resultado(s) adicionado(s) com sucesso!
📄 Arquivo atualizado: index.html
brasileirao-serie-a

Novos jogos:
   🟢 Corinthians (2) ✈️  Flamengo (1)
   ⚪ Botafogo (1) ✈️  Palmeiras (1)
   🔴 São Paulo (3) ✈️  Corinthians (0)
```

---

**Feito para facilitar o registro de resultados da Temporada 2029! 🟡⚫**