"""repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira"""

condicao = True

while condicao:
    nome = input("Qual o seu nome? ")
    print(f"Seu nome é {nome}")
    
    if nome == "0":
        break