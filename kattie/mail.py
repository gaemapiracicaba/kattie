"""
"""


import yagmail


def envia_email(credenciais, destinatario, assunto, corpo_email):
    """
    Envia e-mail a partir do destinatário e corpo de mensagem informados
    """
    try:
        yag = yagmail.SMTP(credenciais['usuario'], credenciais['senha'])
        yag.send(destinatario, assunto, corpo_email)
        print(f'e-mail enviado para {destinatario}')

    except Exception as e:
        print(f'e-mail não enviado para {destinatario}\n{e}')
    return 0
