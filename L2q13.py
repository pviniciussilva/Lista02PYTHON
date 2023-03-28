'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

<<<<<<< HEAD
numero = int(input('Digite o número correspondente a o dia da semana: '))
=======
numero = str(input('Digite o número correspondente a o dia da semana: '))
>>>>>>> e62d982cabd61780809a9cdad7b1cb4dd0d30ee7

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
<<<<<<< HEAD
elif numero > 7 and numero < 0:
    print('Valor invalido!')
=======
>>>>>>> e62d982cabd61780809a9cdad7b1cb4dd0d30ee7

print(f'O {dia} corresponde ao dia de {numero} na semana')