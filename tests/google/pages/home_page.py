from selene import Browser
from selene.api import s

from sources.enums.urls import GOOGLE_URL

class HomePage():
  TIMEOUT_DEFAULT = 15

  def __init__(self, app: Browser):
    super().__init__(app)
    self.input_barra_pesquisa = s("//input[@title='Pesquisar']")
    self.btn_pesquisa_google = s("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    self.btn_estou_com_sorte = s("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")

  def acessar_google(app):
    app.open(super.get_url())
  
  def digitar_cot_dolar(self):
    self.input_barra_pesquisa.type("Cotação Dólar")
  
  def pesquisa_google(self):
    self.btn_pesquisa_google.click()

  def get_url(self):
    return GOOGLE_URL.BASE_URL.value

#app.open(HomePage(app).get_url())