a = 'A'
b = 'B'
c = 1.1
#parametros nomeados!!
#eles vem POR ULTIMO, pois quando se nomeia um, precisa nomear os proximos
formato = 'a={valor1} b={valor2} c={valor3}'.format(
    valor1=a,valor2=b,valor3=c
    )
print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))