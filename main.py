"""
fffffff
"""


from datetime import date, timedelta

from kattie.app import *
#from .kattie.data import *
#from .kattie.functions import *


# Cria a url de hoje:
day = date.today() + timedelta(days=0)
URL_BASE = 'https://www.mpsp.mp.br/w/do-'
url = f"{URL_BASE}{day.strftime('%d-%m-%Y')}"


# Cria objeto "soup"
soup = get_soup(url)


# Cria Elementos do DO
texto_tratado, lista_doe, estrutura = get_elements(soup)


# Pesquisa individualizada
for nome in pesquisa.items():
    print(nome)
    
    # E-mail
    #email = good_guys[nome]['e_mail']
    print(nome('nome_completo'))

    # # Data
    # data = day.strftime('%d.%m.%Y')
    # print(data)

    # # Faz Pesquisa
    # resultados, n_corrrespondencias = encontra_correspondencias(
    #     good_guys[nome]['aliases'],
    #     lista_doe
    # )

    # #
    # palavras_chave = good_guys[nome]['pesquisa']

    # # Define Assunto
    # assunto = f'Pesquisa automatizada do Diário Oficial de {data} para {nome}'


#     # Printa ou envia o e-mail
#     """ print ('\n' + email)
# 	print ('\n' + content)
# 	print ('\n' + '='* 40) """
#     envia_email(email, assunto, content)








if __name__ == '__main__':
    pass
    #print(content)
