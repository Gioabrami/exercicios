#16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
# nas seguintes situações:
#   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#   Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#   Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = float (input ("Qual o valor de A? "))

if a == 0:
    print ("A equação não é de segundo grau.")
else:
    b = float (input ("Qual o valor de B? "))
    c = float (input ("Qual o valor de C? "))

    delta = (b**2) - (4 * a * c)
    x1 = (- b + (delta** (0.5))) / (2 * a)
    x2 = (- b - (delta** (0.5))) / (2 * a)

    if delta > 0:
        print (f"A equação possui duas raízes reais. São elas {x1} e {x2}.")
    elif delta == 0:
        print (f"A equação possui apenas uma raiz real. Ela é {x1}.")
    elif delta < 0:
        print ("A equação não possui raízes reais.")