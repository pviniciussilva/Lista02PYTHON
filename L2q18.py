'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input('Informe sua data: '))
mes = int(input('Informe seu mes: '))
ano = int(input('Informe seu ano: '))
invalido = 'Sua data não é valida'
if dia > 0 and dia < 32 or mes > 0 and mes < 12 or ano > 0 and ano < 2023:
    print('Data valida')
else:
    print('Data invalida')