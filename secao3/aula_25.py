"""
Interpolação basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) (x minusculo gera letra minuscula, X maiúscula)
"""

nome ="Felipe"
preco = 1000.95808234
variavel ="%s, o preço é R$%.2f" % (nome,preco) # a qntd de placeholder que tem na string tem que ser igual ao numero de parametros passado
print(variavel)
print("o hexadecimal de %d é %08X" % (150000,150000)) 