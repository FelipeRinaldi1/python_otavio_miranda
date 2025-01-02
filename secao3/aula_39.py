nome = "Felipe Rinaldi"

i = 0
novo_nome= ''

while nome:
    print("*",end="")
    if i >= len(nome):
        break
    print(nome[i],end="")
    i+=1

print() 
print()

i = 0

while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i +=1

novo_nome += "*"
print(novo_nome)