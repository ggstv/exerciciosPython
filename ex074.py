"""
  Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""
vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra.lower(), end=' ')
    print()
