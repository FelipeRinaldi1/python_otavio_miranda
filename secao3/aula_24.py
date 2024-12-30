nome = "Felipe"
print(nome[2])
print(nome[-2])

print('a' in nome)
print('a' not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que quer encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')