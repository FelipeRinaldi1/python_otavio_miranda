"""Calculadora com While"""
while True:
    print()
    print("Menu Calculadora:")
    print('1)Adição')
    print('2)Subtração')
    print('3)Multiplicação')
    print('4)Divisão')
    print('0)Sair')
    print()

    escolha = input("Digite o número da operação que deseja realizar: ")

    if escolha == '1':
        try:
            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))

            numero_1_float = numero_1
            numero_2_float = numero_2

            resultado = numero_1_float+numero_2_float
            print(f"O Resultado da operação é: {resultado}")
        except: 
            print("Dado inválido.")

    elif escolha == '2':
        try:
            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))

            numero_1_float = numero_1
            numero_2_float = numero_2

            resultado = numero_1_float-numero_2_float
            print(f"O Resultado da operação é: {resultado}")
        except: 
            print("Dado inválido.")

    elif escolha == '3':
        try:
            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))

            numero_1_float = numero_1
            numero_2_float = numero_2

            resultado = numero_1_float*numero_2_float
            print(f"O Resultado da operação é: {resultado}")
        except: 
            print("Dado inválido.")

    elif escolha == '4':
        try:
            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))

            numero_1_float = numero_1
            numero_2_float = numero_2

            resultado = numero_1_float/numero_2_float
            print(f"O Resultado da operação é: {resultado}")
        except: 
            print("Dado inválido.")

    elif escolha =='0':
        sair =input("Você deseja sair (sim para sair.) ?\n").lower().startswith('s')
        if sair == True:
            print("Saindo...")
            break

    else:
        print("Opção inválida. escolha as opções acima.")