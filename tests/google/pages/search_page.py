from selene import Browser
from selene.api import s

from sources.enums.urls import GOOGLE_URL

class SearchPage():
  TIMEOUT_DEFAULT = 15

  def __init__(self, app: Browser):
    super().__init__(app)
    self.lbl_cotacao = s('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')

  def confirma_cotacao(self, moedas_ativas:str):
    cotacao_google = self.lbl_cotacao
    moedas_ativas = ":.2f".format(moedas_ativas)
    moedas_ativas.replace('.', ',')

    assert cotacao_google == moedas_ativas

    
