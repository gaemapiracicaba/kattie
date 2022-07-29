"""
ssss
"""


import yagmail
import unidecode





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






def envia_email(destinatario, assunto, corpo_email):
    """
    Envia e-mail a partir do destinatário e corpo de mensagem informados
    """
    try:
        yag = yagmail.SMTP(usuario, senha)
        yag.send(destinatario, assunto, corpo_email)
        print(f'e-mail enviado para {destinatario}')

    except Exception as e:
        print(f'e-mail não enviado para {destinatario}\n{e}')
    return 0
