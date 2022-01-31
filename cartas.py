import random
def cria_baralho():
    naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
    cartas = ['Rei', 'Rainha', 'Valete', 'Dez', 'Nove', 'Oito',
              'Sete', 'Seis', 'Cinco', 'Quatro', 'Três', 'Dois', 'Um', 'Ás']
    baralho = {}
    for naipe in naipes:
        for carta in cartas:
            baralho.append(carta + ' de ' + naipe)
    random.shuffle(baralho)
    return baralho   

baralho = cria_baralho()
jogador_um = []
while len(jogador_um) < 5:
    carta = random.choice(baralho)
    jogador_um.append(carta)
    baralho.remove(carta)
    
print(*jogador_um, sep='\n')    
        