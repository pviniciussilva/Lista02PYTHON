'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver 
o programa que calculará os reajustes.
    ◦ Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário 
    atual:
    ◦ salários até R$ 280,00 (incluindo) : aumento de 20%
    ◦ salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    ◦ salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    ◦ salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    ◦ o salário antes do reajuste;
    ◦ o percentual de aumento aplicado;
    ◦ o valor do aumento;
    ◦ o novo salário, após o aumento.'''

salario_colaborador = float(input('Digite o valor do seu salário: '))

aumento_de_20 = salario_colaborador + ((20/100) * salario_colaborador)
aumento_de_15 = salario_colaborador + ((15/100) * salario_colaborador)
aumento_de_10 = salario_colaborador + ((10/100) * salario_colaborador)
aumento_de_5 = salario_colaborador + ((5/100) * salario_colaborador)

if  salario_colaborador <= 280:
    print(f'Seu salário sofreu um aumento de 20% e o valor final é de R${aumento_de_20:,.2f}')
elif salario_colaborador > 700 and salario_colaborador < 280:
    print(f'Seu salário sofreu um aumento de 15% e o valor final é de R${aumento_de_15:,.2f}')
elif salario_colaborador > 700 and salario_colaborador < 1500:
    print(f'Seu salário sofreu um aumento de 10% e o valor final é de R${aumento_de_10:,.2f}')
elif salario_colaborador >= 1500:
    print(f'O salário antes do reajuste: R${salario_colaborador:,.2f}')
    print(f'O percentual de aumento aplicado foi de: {(5/100):,.2f}%')
    print(f'O valor do aumento: R${((5/100) * salario_colaborador):,.2f}')
    print(f'O novo salário, após o aumento: R${aumento_de_5:,.2f}')