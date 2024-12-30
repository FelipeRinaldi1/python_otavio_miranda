#O "not" inverte expressões
#not true = false
#not false = true

senha = input("Senha: ")

if not senha:
    print("Você não digitou nada!")
elif senha != '123456':
    print("Senha incorreta")
else:
    print("Acesso permitido")