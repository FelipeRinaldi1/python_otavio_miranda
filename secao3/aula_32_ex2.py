"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input ("Digite qual é a hora atual (00-23): ")

try:
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <=11:
        print("Bom dia!")
    elif horas_int >= 12 and horas_int <=17:
        print("Boa tarde!")
    elif horas_int >=18 and horas_int <=23:
        print("Boa noite!")
    else:
        print("Por favor, insira um valor entre 00 e 23!")
except:
    print("Por favor, insira um número inteiro!")