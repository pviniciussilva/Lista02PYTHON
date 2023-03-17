"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

palavra = input('Digite a letra: ').lower()
vogais = ('a', 'e', 'i', 'o', 'u')
if palavra in vogais:
    print('A letra é vogal')
else:
    print('A letra é consoante')