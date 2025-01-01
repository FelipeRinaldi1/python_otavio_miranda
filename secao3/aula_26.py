"""
Formatação básica de strings
s- string
d- int
f- float
.<númeroo de digitos>f
x ou X - hexadecimal
(Caractere) (><^) (quantidade)
> esquerda
< direita
^ centro
= força o numero a aprecer antes dos zeros
sinal + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a"""

var = "ABC"
print(f"{var}")
print(f"{var: >10}") # preenche 10 caracteres à esquerda
print(f"{var: <10}") # preenche 10 caracteres à direita
print(f"{var: ^10}") # preenche 10 caracteres dividido entre a esquerda e direita (centraliza)
print(f'{1000.128190081:,.1f}')
print(f'{-1000.128190081:+,.1f}') # o + indica que mostra tanto se o numero for positivo ou negativo
print(f'{1000.128190081:-,.1f}') # o - mostra o sinal negativo caso o numero for negativo, se for positivo não mostra nada (padrao)
print(f'{1000.128190081:0>+10,.1f}') 
print(f'{1000.128190081:0=+10,.1f}') 
print(f"O hexadecimal de 1500 é {1500:08X}")


