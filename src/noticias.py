# %%
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
from dotenv import load_dotenv

# %%

load_dotenv()

headers = {
    'Authorization': os.getenv("NEWS_API_KEY")
}

# %%
def coleta_portais_categoria(categoria):
    
    url_base_portais = 'https://newsapi.org/v2/top-headlines/sources?'

    categoria = f'category={categoria}'

    url_portais = url_base_portais + categoria

    response = requests.get(url_portais, headers=headers)
    response = response.json()

    return response



dict_categorias = {
    'esportes': 'sports',
    'negócios': 'business',
    'entretenimento': 'entertainment',
    'geral': 'general',
    'saúde': 'health',
    'ciência': 'science',
    'tecnologia': 'technology'
}

categoria_pt = input('Categorias: esportes, negócios, entretenimento, geral, saúde, ciência ou tecnologia\nEscolha sua categoria: ')

categoria_us = dict_categorias[categoria_pt]

resposta = coleta_portais_categoria(categoria_us)

portais = pd.DataFrame(resposta['sources'])

portais = portais[portais['language'] == 'en']
# %%
def coleta_top_headlines(portal):

    url_headlines = f'https://newsapi.org/v2/top-headlines?sources={portal}'

    response = requests.get(url_headlines, headers=headers)
    response = response.json()

    return response



lista_responses = []
for id in portais['id']:
    headlines = coleta_top_headlines(id)
    lista_responses.append(headlines)


# %%
lista_descricao_artigos = []
for noticias_portal in lista_responses:
    artigos = noticias_portal['articles']
    for artigo in artigos:
        descricao = artigo['description']
        if descricao == None:
            pass
        elif descricao == '':
            pass
        else:
            descricao = descricao.replace("\ufeff", "").replace("\r\n\r\n", "").replace("\n", "")
            lista_descricao_artigos.append(descricao)


lista_descricao_artigos = lista_descricao_artigos[:20]
# %%
from google.genai import types
from google.genai.client import Client
# %%

load_dotenv()

client = Client(api_key=os.getenv("GEMINI_API_KEY"))

texto = ""

for i in range(0, len(lista_descricao_artigos)):
    texto = texto + " " + lista_descricao_artigos[i]

# %%

prompt = f"""Considerando que o tema base das notícias é: {categoria_pt}, interprete a descrição dos artigos a seguir e gere um resumo objetivo em pt-BR abrangendo todos os tópicos.
Texto:
{texto}"""

resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(temperature=0)
)

resumo_final = resp.text

# %%
resumo_final = resp.text

data_hoje = datetime.datetime.now().strftime("%d-%m-%Y")
nome_arquivo = f"resumo_{data_hoje}.txt"

diretorio = os.path.join(*os.getcwd().split("\\")[:-1], "data", nome_arquivo)
diretorio = diretorio.replace('c:', 'C:\\')
#caminho = os.path.join(diretorio, nome_arquivo)

with open(diretorio, "w", encoding="utf-8") as f:
    f.write(resumo_final)

print(f"Resumo salvo em: {diretorio}")

