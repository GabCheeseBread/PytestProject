import re

especiais = "!@#$%¨&*()_=+-{}[]/?°º<>,.;:´`^~\|"
numeros = "0123456789"

def validar_nome(nome):
    if nome == ""\
       or len(nome) > 30\
       or nome != nome.translate(str.maketrans(especiais," "*len(especiais))).replace(" ","")\
       or not (nome[0].isupper() or nome[0] in numeros):
        return False
    else:
        return True

def validar_senha(senha):
    if len(senha) < 10\
       or not re.search("[a-z]",senha)\
       or not re.search("[A-Z]",senha)\
       or not re.search("[0-9]",senha):
        return False
    else:
        return True
