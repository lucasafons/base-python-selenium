#language:pt

@to_review
Funcionalidade: FT01 Pesquisar no google

  Cenario: Pesquisar a cotação do dólar no google
    Dado que o usuário acesse o google
    Quando digitar cotação do dólar na barra de pesquisa
    Quando clicar em 'Pesquisa Google'
    Entao a pesquisa retornará a cotação do dólar atual