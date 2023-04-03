from  import math 
'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    ◦ Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
    demais valores, sendo encerrado;
    ◦ Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    ◦ Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    ◦ Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
    

    
print('ax2 + bx + c.')
    
a = float(input('Informe o valor de "a": '))
b = float(input('Informe o valor de "b": '))
c = float(input('Informe o valor de "c": '))
dela = b ** 2 - 4 * a * c
x = (-(-b) + dela ** (1/2)) / 2 *a

if  a > 0:
    equaçao = True
#   if equaçao == True:
        
else:
    equaçao = False

    
    
print(f'{equaçao}')