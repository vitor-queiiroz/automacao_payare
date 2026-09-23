from playwright.sync_api import Page

class CardholderPage:

    def __init__(self, page: Page): #troquei a (,) por (:) após page === page: Page.
        self.page = page

        self.botao_pesquisar_cardholder = page.locator("#searchCardHolder") # Abre a janela "Busca por Cliente"
        self.menu_cartao = page.locator("#menu\\:searchByCard") # LOCALIZA O MENU CARTAO
        self.numero_cartao = page.locator("#inputCard") # LOCALIZA O NUMERO CARTAO
        self.botao_pesquisar = page.locator("#btnSearch")

    def abrir_busca(self):
        self.botao_pesquisar_cardholder.click()

    def selecionar_cartao(self):
        self.menu_cartao.click()

    def pesquisar_cartao(self, numero_cartao):
        self.numero_cartao.fill(numero_cartao)
        self.botao_pesquisar.click()