# 🏆 Guia de Geração de Blocos HTML para Resultados de Jogos

Este documento contém todo o conhecimento aprendido sobre como gerar blocos HTML para resultados de jogos de futebol, incluindo mapeamento de times, logos, indicadores e estrutura do código.

---

## 📋 Formato de Input

Você pode fornecer resultados em português:

```
vitoria - Flamengo 2 x 0 Corinthians - Brasileirão
derrota - Corinthians 0 x 1 Grêmio - Copa do Brasil
empate - Vasco 1 x 1 Corinthians - Brasileirão
```

---

## 🏷️ Mapeamento de Termos

| Termo | Indicador HTML | Classe |
|-------|----------------|--------|
| `vitoria` / `vítoria` | → `victory` | `indicator-victory` (verde) |
| `derrota` | → `defeat` | `indicator-defeat` (vermelho) |
| `empate` | → `draw` | `indicator-draw` (amarelo) |

---

## 📁 Estrutura do Bloco HTML

```html
<!-- {RESULTADO} - {Mandante} {Casa}x{Visitante} {Visitante} -->
<div class="matches-row">
    <div class="indicator indicator-{INDICADOR}"></div>
    <div class="row">
        <div class="time-casa">
            <div class="nome-do-time-casa">{NOME_MANDANTE}</div>
            <div class="img-wrapper"><img src="{LOGO_MANDANTE}" alt="{NOME_MANDANTE}"></div>
        </div>

        <div class="placar">
            <div class="ponto-casa">{PONTOS_CASA}</div>
            <div class="versus">X</div>
            <div class="ponto-visitante">{PONTOS_VISITANTE}</div>
        </div>

        <div class="time-visitante">
            <div class="img-wrapper"><img src="{LOGO_VISITANTE}" alt="{NOME_VISITANTE}"></div>
            <div class="nome-do-time-fora">{NOME_VISITANTE}</div>
        </div>
    </div>
</div>
```

---

## 📂 Mapeamento de Logos

### Brasileirão Série A (`./brasileirao-serie-a/`)

| Time | Arquivo do Logo |
|------|-----------------|
| corinthians | `./brasileirao-serie-a/corinthians-logo-footylogos-320.webp` |
| flamengo | `./brasileirao-serie-a/flamengo-logo-footylogos-320.webp` |
| fluminense | `./brasileirao-serie-a/fluminense-logo-footylogos-320.webp` |
| palmeiras | `./brasileirao-serie-a/palmeiras-logo-footylogos-320.webp` |
| sao-paulo | `./brasileirao-serie-a/sao-paulo-logo-footylogos-320.webp` |
| gremio | `./brasileirao-serie-a/gremio-logo-footylogos-320.webp` |
| vasco-da-gama | `./brasileirao-serie-a/vasco-da-gama-logo-footylogos-320.webp` |
| santos-fc | `./brasileirao-serie-a/santos-fc-logo-footylogos-320.webp` |
| botafogo | `./brasileirao-serie-a/botafogo-logo-footylogos-320.webp` |
| atlético-mineiro | `./brasileirao-serie-a/atletico-mineiro-logo-footylogos-320.webp` |
| coritiba | `./brasileirao-serie-a/coritiba-logo-footylogos-320.webp` |
| sc-internacional | `./brasileirao-serie-a/sc-internacional-logo-footylogos-320.webp` |

### Brasileirão Série B (`./brasileirao-serie-b/`)

| Time | Arquivo do Logo |
|------|-----------------|
| londrina | `./brasileirao-serie-b/londrina-logo-footylogos-320.webp` |
| ceara-sc | `./brasileirao-serie-b/ceara-sc-logo-footylogos-320.webp` |
| goias | `./brasileirao-serie-b/goias-logo-footylogos-320.webp` |
| cuiaba | `./brasileirao-serie-b/cuiaba-logo-footylogos-320.webp` |
| ponte-preta | `./brasileirao-serie-b/ponte-preta-logo-footylogos-320.webp` |
| fortaleza | `./brasileirao-serie-b/fortaleza-logo-footylogos-320.webp` |
| gremio-novorizontino | `./brasileirao-serie-b/gremio-novorizontino-logo-footylogos-320.webp` |

---

## 🎯 Exemplos Práticos

### Exemplo 1: Vitória em Casa

**Input:**
```
vitoria - Corinthians 4 x 1 Ponte Preta - Copa do Brasil
```

**Saída HTML:**
```html
<!-- VITORIA - Corinthians 4x1 Ponte Preta -->
<div class="matches-row">
    <div class="indicator indicator-victory"></div>
    <div class="row">
        <div class="time-casa">
            <div class="nome-do-time-casa">Corinthians</div>
            <div class="img-wrapper"><img src="./brasileirao-serie-a/corinthians-logo-footylogos-320.webp" alt="Corinthians"></div>
        </div>

        <div class="placar">
            <div class="ponto-casa">4</div>
            <div class="versus">X</div>
            <div class="ponto-visitante">1</div>
        </div>

        <div class="time-visitante">
            <div class="img-wrapper"><img src="./brasileirao-serie-b/ponte-preta-logo-footylogos-320.webp" alt="Ponte Preta"></div>
            <div class="nome-do-time-fora">Ponte Preta</div>
        </div>
    </div>
</div>
```

### Exemplo 2: Derrota em Visitante

**Input:**
```
derrota - Corinthians 0 x 2 Londrina - Brasileirão
```

**Saída HTML:**
```html
<!-- DERROTA - Corinthians 0x2 Londrina -->
<div class="matches-row">
    <div class="indicator indicator-defeat"></div>
    <div class="row">
        <div class="time-casa">
            <div class="nome-do-time-casa">Corinthians</div>
            <div class="img-wrapper"><img src="./brasileirao-serie-a/corinthians-logo-footylogos-320.webp" alt="Corinthians"></div>
        </div>

        <div class="placar">
            <div class="ponto-casa">0</div>
            <div class="versus">X</div>
            <div class="ponto-visitante">2</div>
        </div>

        <div class="time-visitante">
            <div class="img-wrapper"><img src="./brasileirao-serie-b/londrina-logo-footylogos-320.webp" alt="Londrina"></div>
            <div class="nome-do-time-fora">Londrina</div>
        </div>
    </div>
</div>
```

### Exemplo 3: Empate

**Input:**
```
empate - Vasco 1 x 1 Corinthians - Brasileirão
```

**Saída HTML:**
```html
<!-- EMPATE - Vasco 1x1 Corinthians -->
<div class="matches-row">
    <div class="indicator indicator-draw"></div>
    <div class="row">
        <div class="time-casa">
            <div class="nome-do-time-casa">Vasco</div>
            <div class="img-wrapper"><img src="./brasileirao-serie-a/vasco-da-gama-logo-footylogos-320.webp" alt="Vasco"></div>
        </div>

        <div class="placar">
            <div class="ponto-casa">1</div>
            <div class="versus">X</div>
            <div class="ponto-visitante">1</div>
        </div>

        <div class="time-visitante">
            <div class="img-wrapper"><img src="./brasileirao-serie-a/corinthians-logo-footylogos-320.webp" alt="Corinthians"></div>
            <div class="nome-do-time-fora">Corinthians</div>
        </div>
    </div>
</div>
```

---

## 🎨 Indicadores Visuais

| Classe | Cor | Uso |
|--------|-----|-----|
| `indicator-victory` | Verde 🟢 | Vitória do time da casa |
| `indicator-defeat` | Vermelho 🔴 | Derrota do time da casa |
| `indicator-draw` | Amarelo 🟡 | Empate |

---

## ⚠️ Regras Importantes

1. **O comentário sempre indica o resultado real** (ex: `<!-- DERROTA -->`) baseado na perspectiva do Corinthians
2. **Times em casa aparecem primeiro** no bloco `<time-casa>`
3. **Logos são carregados automaticamente** com base no nome do time
4. **Pontos vazios para placares X-X** (empates)

---

## 📝 Dicas Rápidas

- Use `vitoria`, `derrota` ou `empate` em português no input
- O script automaticamente detecta o campeonato (Brasileirão, Copa do Brasil, Libertadores)
- Os logos são buscados automaticamente nas pastas correspondentes
- Se um logo não for encontrado, adicione ao mapeamento acima

---

## 🚀 Fluxo de Trabalho

1. **Forneça resultado** no formato: `vitoria - Flamengo 2 x 0 Corinthians - Brasileirão`
2. **Receba bloco HTML** pronto para copiar e colar no `index.html`
3. **Cole o bloco** no local desejado (após o último jogo ou no final do arquivo)
4. **Repita** para cada resultado novo

---

## 📂 Estrutura de Pastas

```
temporada-2029/
├── index.html                    # Arquivo principal com todos os jogos
├── estilos.css                   # Estilos CSS
├── README.md                     # Documentação
├── brasiliearao-serie-a/        # Logos Série A
│   ├── corinthians-logo-footylogos-320.webp
│   └── ...
├── brasileirao-serie-b/         # Logos Série B
│   ├── londrina-logo-footylogos-320.webp
│   └── ...
└── ...                          # Outras pastas de logos e arquivos
```

---

**Documento criado por:** AI Assistente  
**Data:** 18/10/2026  
**Projeto:** Temporada 2029 - Brasileirão, Copa do Brasil, Libertadores