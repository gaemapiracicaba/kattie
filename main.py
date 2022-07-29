"""
fffffff
"""

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




if __name__ == '__main__':
    pass
    print(content)
