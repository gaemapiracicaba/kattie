"""
ssss
"""

import requests
import urllib3
from bs4 import BeautifulSoup
import unidecode


def get_soup(url):
    # Faz o request
    urllib3.disable_warnings()
    doe = requests.get(url, verify=False)

    if doe.status_code == 200:
        soup = BeautifulSoup(doe.text, 'html.parser')
        print(f'URL gerada: {url}')
        print(f'Objeto soup criado.\nCódigo: {doe.status_code}\n')
        return soup

    elif doe.status_code != 200:
        raise Exception(
            f'\nObjeto soup não criado\nDOE não encontrado. Código: {doe.status_code}\nTente outra vez mais tarde.')
    else:
        return 0




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


def trata_palavras(texto):
    """
    Tira os acentos, caracteres º e ª e converte o texto em letras maiúsculas
    """
    texto = texto.replace('º', '')
    texto = texto.replace('ª', '')
    texto = texto.replace('    ', ' ')  # 4
    texto = texto.replace('   ', ' ')  # 3
    texto = texto.replace('  ', ' ')  # 2
    return unidecode.unidecode(texto).upper()


def encontra_correspondencias(lista_alias, lista_doe):
    """
    Encontra a correspondência entre os textos contidos em lista
    e as publicações do DOE e o número de ocorrências
    """
    resultados = []
    n_correspondencias = 0
    for publicacao in lista_doe:
        for nome in lista_alias:
            if trata_palavras(nome) in publicacao:
                resultados.append(publicacao)
                n_correspondencias += 1
    return resultados, n_correspondencias


def set_content():

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
    return content
