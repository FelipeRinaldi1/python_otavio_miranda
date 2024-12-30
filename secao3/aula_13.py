nome = "Felipe Rinaldi Sobreira"
altura = 1.77
peso = 74
imc = (peso)/(altura**2) 


# f-strings
linha_1 = f'{nome} tem {altura:.2f}m de altura'
linha_2 = f'{peso}kg'

print(linha_1)
print(linha_2)
print(f'{imc:.2f}')