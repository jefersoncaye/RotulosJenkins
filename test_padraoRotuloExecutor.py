from playwright.sync_api import expect
import time

def login(page, usuario, senha):
    page.goto("http://cit/login",timeout=2000)
    page.get_by_placeholder("Nome do usuário").fill(usuario)
    page.get_by_placeholder("Senha").fill(senha)
    page.get_by_role("button", name="Entrar").click()
    time.sleep(2)

def alteraRotuloMaquina(page, maquina, rotulo):
    page.goto(f"http://cit/computer/{maquina}/configure", timeout=2000)
    page.wait_for_load_state()
    expect(page.locator("[class='setting-main']").locator("[name='_.labelString']")).to_be_visible()
    page.locator("[class='setting-main']").locator("[name='_.labelString']").fill(rotulo)
    page.get_by_role("button", name='Salvar').click()
    page.wait_for_load_state()
    page.goto(f"http://cit/computer/{maquina}/configure", timeout=2000)
    page.wait_for_load_state()
    expect(page.locator("[class='setting-main']").locator("[name='_.labelString']")).to_have_value(rotulo)


listaMaquinasAlterar = ['Gemini', 'Heineken', 'Libra', 'Leo', 'Sextans', 'TestExecute01', 'TestExecute02', 'TestExecute03',
                        'TestExecute04', 'TestExecute06', 'TestExecute07']

maquinaQuiu = 'testexecute02'

def test_padraoRotuloExecutor(set_up):
    page = set_up
    login(page, 'testcomplete', '12345')
    for maquina in listaMaquinasAlterar:
        rotulos = 'TestCompleteEmpresarial TestCompleteTributario TestCompleteWeb TestCompleteFolha TestCompleteFiscal TestCompletePostgreFiscal TestCompletePostgreFolha'
        if maquina.lower() == maquinaQuiu.lower():
            rotulos = rotulos + ' TestCompleteFiscalQuiu'
        page.on("console", print(f'\n\nAtualizando Rotulos da maquina: {maquina} para: {rotulos}'))
        try:
            alteraRotuloMaquina(page, maquina, rotulos)
        except: page.on("console", print(f'\nAlgo deu Errado ao atualizar os rotulos da maquina {maquina}'))
    page.close()



