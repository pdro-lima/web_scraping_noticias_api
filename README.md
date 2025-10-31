# 🗞️ News Summarizer PT-BR com Gemini e NewsAPI

Este projeto tem como objetivo **coletar principais manchetes de portais de notícias em inglês**, **traduzir para português (pt-BR)** e **gerar resumos objetivos** utilizando o modelo **Gemini (Google AI)** de forma **gratuita via API pública**.

O pipeline automatiza todo o fluxo de:
1. Coleta de manchetes e artigos via [NewsAPI.org](https://newsapi.org);
2. Tradução e resumo dos textos com o **Gemini API** (Google AI Studio);
3. Armazenamento local dos resultados traduzidos e resumidos objetivamente.

---

## 🧠 Funcionalidades

- 🔍 Consulta automatizada às fontes da **NewsAPI.org**
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

```

## ⚙️ Passo a passo para o melhor uso

1. Acesse os links abaixo para criação das chaves pessoais para acesso às duas APIs utilizadas (Google AI e NewsAPI.org)

- https://ai.google.dev/gemini-api/docs/api-key?utm_source=chatgpt.com&hl=pt-br
- https://newsapi.org/docs/get-started

2. Crie um ambiente virtual e faça a instalação do pacote de recursos descritos no requirements.txt
3. Execute o script em python selecionando na execução o tema das notícias desejadas para serem coletadas, traduzidas e resumidas
4. Acesse o resumo na pasta "data"