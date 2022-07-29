"""
sssss
"""

from time import time
from tkinter.messagebox import NO
import requests
import urllib3

from bs4 import BeautifulSoup

from datetime import date, timedelta


from .functions import *
from .data import *


def get_soup(url):
    # Faz o request
    urllib3.disable_warnings()
    doe = requests.get(url, verify=False)

    if doe.status_code == 200:
        soup = BeautifulSoup(doe.text, 'html.parser')
        print(f'URL gerada: {url}')
        print(f'Objeto soup criado.\nCódigo: {doe.status_code}\n')
        return soup

    else:
        raise Exception(
            f'\nObjeto soup não criado\nDOE não encontrado. Código: {doe.status_code}\nTente outra vez mais tarde.')



def get_elements(soup):
    # Texto e estrutura do DOE
    texto_doe = soup.find(class_='mpsp-daily-official').getText()
    texto_doe = texto_doe.replace('\n\n', '\n')
    texto_tratado = trata_palavras(texto_doe)

    # Gera a lista com o conteúdo do DOE
    lista_doe = texto_tratado.split('\n')

    # Gera a lista com a estrutura do DOE
    estrutura = soup.find_all('h1')
    return texto_tratado, lista_doe, estrutura

# Pesquisa individualizada
for nome in good_guys:

    # E-mail
    email = good_guys[nome]['email']
    print(email)

    # Data
    data = day.strftime('%d.%m.%Y')
    print(data)

    # Faz Pesquisa
    resultados, n_corrrespondencias = encontra_correspondencias(
        good_guys[nome]['aliases'],
        lista_doe
    )

    #
    palavras_chave = good_guys[nome]['pesquisa']

    # Define Assunto
    assunto = f'Pesquisa automatizada do Diário Oficial de {data} para {nome}'

    # Define Conteúdo do E-mail
    content = ''
    content += f'Prezado {nome},\n\n'
    content += f'Segue o resultado da pesquisa automatizada do Diário Oficial de {data},\n'
    content += f'obtido pelo link: {url}\n'
    content += f'\n{"-"*50}\n'

    # Pesquisa Pelo Nome
    content += f'PESQUISA NOMINAL\n\n'
    content += f'Nº de ocorrências com o seu nome: {n_corrrespondencias}\n'
    if n_corrrespondencias != 0:
        n = 0
        for r in resultados:
            content += '\n'
            n += 1
            content += f'{n}) {r}\n'

    # Pesquisa pela Palavra Chave
    content += f'\n{"-"*50}\n'
    content += f'PESQUISA POR PALAVRAS-CHAVE/FRASES\n\n'
    for palavra in palavras_chave:
        content += f'* {palavra}: {texto_tratado.count(trata_palavras(palavra))}\n'

    # Pesquisa pela Palavra Chave
    content += f"\n{'-'*50}\n"
    content += 'ESTRUTURA DO DOE\n\n'
    for i in estrutura:
        if i.get_text() != 'Navegação':
            content += '* ' + i.get_text()+'\n'

    content += f"\n{'-'*50}\n"
    content += f'Programa experimental da Promotoria de Justiça de Piracicaba/SP (Usuários ativos: {len(good_guys)}).\n'
    content += 'Responda ao e-mail se quiser cancelar o "serviço" ou alterar/acrescentar alíases, palavras-chave ou frases para a pesquisa individualizada.\n'
    content += 'Conheça: github.com/jespimentel\n\n'

    content += f"\n{'-'*50}\n"
    content += 'Texto do Diário Oficial. Use "Ctr-F" para localizar as publicações de seu interesse.\n'
    content += texto_doe


#     # Printa ou envia o e-mail
#     """ print ('\n' + email)
# 	print ('\n' + content)
# 	print ('\n' + '='* 40) """
#     envia_email(email, assunto, content)
