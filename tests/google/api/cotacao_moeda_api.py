import requests

from sources.enums.urls import API_COTACAO_URL
import logging

requests = requests.Session()

def get_cotacao(moeda1:str, moeda2:str):
  logging.info('Iniciando a busca da cotação entre moedas via API')
  response = requests.get(API_COTACAO_URL.BASE_URL.value+f"/{moeda1}-{moeda2}")

  logging.info('Response Status Code: '+str(response.status_code))

  assert response.status_code == 200

  cotacao = response.json()[str(moeda1+moeda2)]

  return cotacao