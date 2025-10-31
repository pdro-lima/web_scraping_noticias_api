# 🗞️ News Summarizer PT-BR com Gemini e NewsAPI

Este projeto tem como objetivo **coletar notícias em inglês**, **traduzir para português (pt-BR)** e **gerar resumos objetivos** utilizando o modelo **Gemini (Google AI)** de forma **gratuita via API pública**.

O pipeline automatiza todo o fluxo de:
1. Coleta de *headlines* e artigos via [NewsAPI.org](https://newsapi.org);
2. Tradução e resumo dos textos com o **Gemini API** (Google AI Studio);
3. Armazenamento local dos resultados traduzidos e resumidos.

---

## 🧠 Funcionalidades

- 🔍 Consulta automatizada às principais fontes da **NewsAPI.org**
- 🧾 Tradução automática do conteúdo do inglês para português e geração de resumos curtos e objetivos via **Gemini**
- 💾 Armazenamento local dos resultados em `.txt`

---

## 🧩 Arquitetura do Projeto

```bash
.
├── src/
│   ├── noticias.py          # Script principal: coleta, tradução e resumo
│   ├── .env                 # Variáveis de ambiente (chaves de API)
├── data/                    # Pasta onde os resumos são salvos
├── requirements.txt         # Dependências do projeto
└── README.md
