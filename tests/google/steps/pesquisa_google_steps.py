from pytest_bdd import scenarios, when, given, then


from tests.google.pages.home_page import HomePage
from tests.google.pages.search_page import SearchPage
from tests.google.api.cotacao_moeda_api import get_cotacao

scenarios(
    './tests/features/pesquisa_google.feature'
)

@given("que o usuário acesse o google")
def step_home_google(app):
    HomePage(app).acessar_google()

@when("digitar cotação do dólar na barra de pesquisa")
def step_digitar_dolar(app):
    HomePage(app).digitar_cot_dolar()

@when("clicar em 'Pesquisa Google'")
def step_pesquisar_google(app):
    HomePage(app).pesquisa_google()

@then("a pesquisa retornará a cotação do dólar atual")
def step_tela_pesquisa(app, context):
    moedas_ativas = get_cotacao("USD", "BRL")
    context['cotacao'] =  moedas_ativas['bid']
    SearchPage(app).confirma_cotacao(context['cotacao'])
