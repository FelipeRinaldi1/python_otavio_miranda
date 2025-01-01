"""Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""
numero = input("Digite um numero para ser dobrado: ")

try:
    print("str: ",numero)
    numero_float = float(numero)
    print("Float: ",numero)
    print(f"O dobro do numero {numero} é {numero_float * 2}")
except:
    print("Isso não é um número")