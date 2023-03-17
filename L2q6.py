'''Faça um Programa que leia três números e mostre o maior deles.'''

numero_um = int(input('Digite o número um: '))
numero_dois = int(input('Digite o número dois: '))
numero_tres = int(input('Digite o número três: '))

if numero_um > numero_dois and numero_um > numero_tres:
    print(numero_um)
elif numero_dois > numero_tres:
    print(numero_dois)
else:
    print(numero_tres)