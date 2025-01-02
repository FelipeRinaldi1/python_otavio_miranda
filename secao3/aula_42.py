frase = 'O python é uma linguagem de programação '\
'multiparadigma. '\
'python foi criado por Guido van Rossum.'.lower()

print(frase)
print(frase.count(' '))

i= 0 
apareceu_mais_vezes = 0
letra_mais_vezes =''

while i<len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i +=1
        continue
    qtd_atual = frase.count(letra_atual)


    if apareceu_mais_vezes < qtd_atual:
        apareceu_mais_vezes = qtd_atual
        letra_mais_vezes = letra_atual
    
    i +=1

print(f"A letra que apareceu mais vezes foi '{letra_mais_vezes}' {apareceu_mais_vezes}x")
