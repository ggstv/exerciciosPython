"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep
print(f'-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print(f'-'*30)
jogos = int(input(f'Quantos jogos você quer sortear? '))
print('-='*5, f'SORTEANDO {jogos} JOGOS', '=-'*5)
jogoSort = []
jogosTod = []
for x in range(1, jogos+1):
    while len(jogoSort) < 6:
        num = randint(1, 60)
        if num not in jogoSort:
            jogoSort.append(num)
    jogoSort.sort()
    print(f'Jogo {x:>2}: ', f'{jogoSort}', end='')
    print()
    jogosTod.append(jogoSort[:])
    jogoSort.clear()
    sleep(1)

