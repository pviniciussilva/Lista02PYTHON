'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    ◦ Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
    demais valores, sendo encerrado;
    ◦ Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    ◦ Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    ◦ Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
    

    
print('ax2 + bx + c.')
    
a = (input('Informe o valor de "a": '))
b = (input('Informe o valor de "b": '))
c = (input('Informe o valor de "c": '))
delta = pow(b,2)- 4 * a * c
x1 = (-(-b) + delta ** (1/2)) / 2 * a
x2 = (-(-b) - delta ** (1/2)) / 2 * a

if x1 > 0:
    x = x1
elif x2 > 0:
    x = x2
elif a < 0:
    print('O valor informado à "a" não é válido, a equação não é uma equação de segundo grau') 
print(f'{x}')