'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

numero = str(input('Digite o número correspondente a o dia da semana: '))

if numero == 1:
  dia = 'Domingo'
elif numero == 2:
  dia = 'Segunda - feira'
elif numero == 3:
  dia = 'Terça - feira'
elif numero == 4:
  dia = 'Quarta - feira'
elif numero == 5:
  dia = 'Quinta - feira'
elif numero == 6:
  dia = 'Sexta - feira'
elif numero == 7:
  dia = 'Sábado'

print(f'O {dia} corresponde ao dia de {numero} na semana')