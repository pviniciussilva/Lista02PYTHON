#Faça um Programa que peça dois números e imprima o maior deles.

#entrada
print("Programa para comparar dois números")

#processamento
numero_1 = int(input("Digite o 1o numero para comparar: "))
numero_2 = int(input("Digite o 2o numero para comparar: "))

#saída
if numero_1 > numero_2:
    print("O número {} é o maior".format(numero_1))
else:
    print('O número {} é o maior'.format((numero_2)))