#1. Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input ("Digite o primeiro número: "))
num2 = int(input ("Digite o segundo número: "))

if num1 > num2:
    print ("O maior número é {}.".format (num1))
else:
    print ("O maior número é {}.".format (num2))