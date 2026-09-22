from playwright.sync_api import Page, expect
import re


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.usuario = page.locator("#username")  #"Playwright, encontre na página o elemento cujo id é username."
        self.senha = page.locator("#password")
        self.botao_acessar = page.locator("#btnEnter")
        self.mensagem_erro = page.get_by_role("alert")


    def acessar(self, usuario, senha): # representa a ação de fazer login.
        self.usuario.fill(usuario) #usuario e senha fill para PREENCHER os campos
        self.senha.fill(senha)
        self.botao_acessar.click()

    def validar_login(self, usuario):
        expect(self.page).to_have_url(
            re.compile(r".*/CMS-ISSUER/issuerMenu\.jsf.*")
        )

        expect(
        self.page.get_by_text(usuario, exact=False)
        ).to_be_visible()