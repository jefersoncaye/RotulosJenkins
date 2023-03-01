import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from httplib2 import Http
from json import dumps


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


def enviaChat(urlWebhook, mensagem):
    """Hangouts Chat incoming webhook quickstart."""
    url = urlWebhook
    bot_message = {
        'text': mensagem}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


mensagem = '*Gerenciador de VMs:*'

for chave, valor in dicionarioRotulos.items():
    mensagem = mensagem + f'\n{chave} --> {str(valor).strip("[]")}'


enviaChat('https://chat.googleapis.com/v1/spaces/AAAAvyOeY1o/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=kS4NB6yzuuUSig97Gw96-ArrfmOcHEJcxH4MR0J0m48%3D', mensagem)