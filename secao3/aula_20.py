primeiro_valor = input("Digite o 1º valor")
segundo_valor = input("Digite o 2º valor")

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor < int_segundo_valor:
    menor_valor = segundo_valor
    print(f"O valor {segundo_valor} é maior que {primeiro_valor}")
    
elif int_primeiro_valor > int_segundo_valor:
    menor_valor = primeiro_valor
    print(f"O valor {primeiro_valor} é maior que {segundo_valor}")

else:
    print("Os valores são iguais!")