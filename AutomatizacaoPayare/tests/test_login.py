import os
from pages.login_page import LoginPage
from pages.cardholder_page import CardholderPage


def test_login_cms(page):

    usuario = os.getenv("USER_NAME")
    senha = os.getenv("PASS_WORD")
    card_number = os.getenv("CARD_NUMBER")

    print("USUARIO:", usuario)
    print("SENHA EXISTE", senha is not None)

    assert usuario is not None, "USER_NAME não foi configurada"
    assert senha is not None, "PASS_WORD não foi configurada"
    assert card_number is not None, "CARD_NUMBER não foi configurada"

    page.goto(
        "https://sistemashomol.fastpays.com.br/CMS-ISSUER/loginUser.jsf"
    )

    login = LoginPage(page)

    login.acessar(
        usuario=usuario,
        senha=senha
    )

    login.validar_login(usuario)

    #
    #


    page.goto(
        "https://sistemashomol.fastpays.com.br/CMS-ISSUER/"
        "modules/issuer/cardHolder/templates/cardHolderTemplate.jsf?openSearch=true"
    )

    print("SEARCH CARDHOLDER:", page.locator("#searchCardHolder").count())
    print("SEARCH FORM:", page.locator("#searchForm").count())
    print("MENU CARTÃO:", page.locator("#menu\\:searchByCard").count())
    print("INPUT CARTÃO:", page.locator("#inputCard").count())

    ##page.locator("#searchCardHolder").click() TAVA DANDO ERROO NO FLUXOO

    print("MENU CARTÃO:", page.locator("#menu\\:searchByCard").count())

    page.locator("#menu\\:searchByCard").click()
    print("INPUT CARTÃO APÓS CLICAR:", page.locator("#inputCard").count())

    page.locator("#inputCard").fill(card_number)

    print("CARTÃO PREENCHIDO!")
    #print("VALOR DO CAMPO:", page.locator("#inputCard").input_value())

    page.locator("#btnSearch").click()
    #page.wait_for_timeout(30000)
    print("PESQISA REALIZADA")
    input("Pressione ENTER para finalizar o teste...")