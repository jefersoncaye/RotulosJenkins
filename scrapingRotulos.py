import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


def buscaPagina(url, usuario='', senha=''):
    html = requests.get(url, auth=HTTPBasicAuth(usuario, senha)).content
    return html


def buscaRotulos(html):
    soup = BeautifulSoup(html, 'html5lib')
    rotulos = soup.find('input', attrs={"name": "_.labelString"})
    rotulos = rotulos['value']
    return rotulos


listaMaquinas = ['Gemini', 'Heineken', 'Libra', 'Leo', 'Sextans', 'TestExecute01', 'TestExecute02', 'TestExecute03',
                 'TestExecute04', 'TestExecute06', 'TestExecute07']

dicionarioRotulos = {}

for maquina in listaMaquinas:
    rotulosMaquina = []
    link = f'http://cit/computer/{maquina}/configure'
    html = buscaPagina(link, 'testcomplete', '12345')
    rutulos = buscaRotulos(html)
    if 'TestCompleteFiscal' in rutulos and 'TestCompleteFiscal_n' not in rutulos:
        rotulosMaquina.append('Fiscal')
    if 'TestCompleteFolha' in rutulos and 'TestCompleteFolha_n' not in rutulos:
        rotulosMaquina.append('Folha')
    if 'TestCompleteEmpresarial' in rutulos and 'TestCompleteEmpresarial_n' not in rutulos:
        rotulosMaquina.append('Empresarial')
    if 'TestCompleteWeb' in rutulos and 'TestCompleteWeb_n' not in rutulos:
        rotulosMaquina.append('Web')
    if 'TestCompletePostgreFiscal' in rutulos and 'TestCompletePostgreFiscal_n' not in rutulos:
        rotulosMaquina.append('PostgreFiscal')
    if 'TestCompletePostgreFolha' in rutulos and 'TestCompletePostgreFolha_n' not in rutulos:
        rotulosMaquina.append('PostgreFolha')
    if 'TestCompleteFiscalQuiu' in rutulos and 'TestCompleteFiscalQuiu_n' not in rutulos:
        rotulosMaquina.append('Quiu')
    if len(rotulosMaquina) >= 6:
        if 'Quiu' in rotulosMaquina:
            rotulosMaquina = ['Todos e Quiu']
        else:
            rotulosMaquina = ['Todos']
    dicionarioRotulos[maquina] = rotulosMaquina


print('Gerenciador de VMs:')
for chave, valor in dicionarioRotulos.items():
    print(f'{chave} --> {str(valor).strip("[]")}')
