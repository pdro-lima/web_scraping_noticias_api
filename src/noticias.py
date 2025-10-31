# %%

import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

# %%

chave_api = 'df7e4a93990d47998818ee41bcc4a786'

headers = {
    'Authorization': chave_api
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

resposta

# %%
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



