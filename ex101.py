import colored 
"""Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL e OBRIGATÓRIO nas eleições."""

def voto(ano):
    anoAtual = 2021
    if anoAtual - ano == 17:
        print(f'{anoAtual - ano} anos. Voto {colored.fg(226)}OPCIONAL{colored.attr("reset")}.')
    else:
        if anoAtual - ano < 18:
            print(f'{anoAtual - ano} anos. Voto {colored.fg(160)}NEGADO{colored.attr("reset")}.')
        elif anoAtual - ano > 18:
            print(f'{anoAtual - ano} anos. Voto {colored.fg(82)}OBRIGATÓRIO{colored.attr("reset")}.')
    
ano = int(input(f'Em que ano você nasceu? '))
voto(ano)
help(colored)