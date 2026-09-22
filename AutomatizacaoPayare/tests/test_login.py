import os
from pages.login_page import LoginPage


def test_login_cms(page):

    usuario = os.getenv("USER_NAME")
    senha = os.getenv("PASS_WORD")

    print("USUARIO:", usuario)
    print("SENHA EXISTE", senha is not None)

    assert usuario is not None, "USER_NAME não foi configurada"
    assert senha is not None, "PASS_WORD não foi configurada"

    page.goto(
        "https://sistemashomol.fastpays.com.br/CMS-ISSUER/loginUser.jsf"
    )

    login = LoginPage(page)

    login.acessar(
        usuario=usuario,
        senha=senha
    )

    login.validar_login(usuario)