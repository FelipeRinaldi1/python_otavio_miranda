contador = 0

while contador <10:
    contador +=1

    if contador==5:
        print("sem o 5") #ignora uma instancia do loop
        continue

    print(contador)

    if contador ==10:
        break


print("acabou")