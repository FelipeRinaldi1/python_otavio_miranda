str_nome = input("Digite o seu nome: ")
int_idade = input("Digite sua idade: ")

print()
if str_nome and int_idade:
    print(f"Seu nome é: {str_nome}")
    print(f"Seu nome invertido é: {str_nome[::-1]}")
    if " " in str_nome:
        print(f"Seu nome possui espaços")
    elif " " not in str_nome:
        print("Seu nome não possui espaços")
    print(f"Seu nome possui {len(str_nome)} letras")
    print(f"A primeira letra do seu nome é: '{str_nome[0]}'")
    print(f"A ultima letra de seu nome é: '{str_nome[-1]}'")
else:
    print("Desculpe, você inseriu campos vazios")