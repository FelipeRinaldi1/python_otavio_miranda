"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input("Digite o seu primeiro Nome: ")

try:
    if len(primeiro_nome) <= 4:
        print("Seu nome tem um tamanho curto!")
    elif len(primeiro_nome) > 4 and len(primeiro_nome) <= 6:
        print("Seu nome tem um tamanho médio!")
    else:
        print("Seu nome tem um tamanho grande!")
except:
    print("Por favor, insira um nome válido!")