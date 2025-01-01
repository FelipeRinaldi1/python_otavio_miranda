"""Fatiamento de Strings
012345678
olá mundo
-987654321

Fatiamento: [início:Fim:Passo] [::]
Obs: a função len retorna a qtd de caracteres"""

variavel = "Olá mundo"
print(variavel[1])
print(variavel[4:])
print(len(variavel))
print(len(variavel[4::5]))
print(variavel[::-1]) #Com o passo negativo ele inverte a string
