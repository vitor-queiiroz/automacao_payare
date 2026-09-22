from playwright.sync_api import Page, expect


def test_fluxo_basico(page: Page):

    # 1 - ACESSAR O SITE
    page.goto("https://playwright.dev/python/")

    # Validar título
    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright Python"
    )


    # 2 - VALIDAR ELEMENTOS DA PÁGINA
    logo = page.get_by_role("link", name="Playwright for Python")
    expect(logo).to_be_visible()


    pesquisa = page.get_by_role("button", name="Search (Control+k)")
    expect(pesquisa).to_be_visible()

    pesquisa.click()

    campo_pesquisa = page.get_by_placeholder("Search")
    expect(campo_pesquisa).to_be_visible()
    campo_pesquisa.fill("Trace Viewer")


    # 3 - FAZER SCROLL
    poderosa = page.get_by_role("heading", name="Powerful tooling")
    poderosa.scroll_into_view_if_needed()

    expect(poderosa).to_be_visible()


    # 4 - LOCALIZAR UMA FUNCIONALIDADE
    resultado = page.locator("#docsearch-hits_playwright-python_0-item-0"
    ).get_by_role("link", name = "Trace viewer")

    expect(resultado).to_be_visible()

    # 5 - CLICAR
    resultado.click()


    # 6 - VALIDAR A NOVA PÁGINA
    expect(page).to_have_url(
        "https://playwright.dev/python/docs/trace-viewer-intro"
    )


    # 7 - VALIDAR CONTEÚDO DA NOVA PÁGINA
    titulo = page.get_by_role(
        "heading",
        name="Trace viewer"
    )

    expect(titulo).to_be_visible() TESTETESTETESTE