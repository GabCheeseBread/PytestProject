import cryptographyFramework as cf
import validar_login as vl

while True:
    nome = input("Informe o nome de usuário.\n(Nome deve ter no máximo 30 caracteres, começar com maiúscula e não possuir caracteres especiais): ")
    if vl.validar_nome(nome):
        break
while True:
    senha = input("Informe a senha.\n(Senha deve possuir no mínimo 10 caracteres, uma letra minúscula e uma maiúscula, um número e um caractere especial): ")
    if vl.validar_senha(senha):
        break

msg = ""

while msg == "" or len(msg) > 70:
    msg = input("Informe uma mensagem (máximo 70 caracteres): ")

cf.initializeWrite()
cf.saveNewLine(cf.encryptMessage(nome,senha,msg))
