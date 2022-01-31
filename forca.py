import random
temas = []
with open('C:/Users/gugu3/hello/.venv/arquivos/alimentos.txt', encoding='utf-8') as alimentos:
    alimentos = [line.strip() for line in alimentos]
    temas.append(alimentos)
with open('C:/Users/gugu3/hello/.venv/arquivos/animais.txt', encoding='utf-8') as animais:
    animais = [line.strip() for line in animais]
    temas.append(animais)
with open('C:/Users/gugu3/hello/.venv/arquivos/objetos.txt', encoding='utf-8') as objetos:
    objetos = [line.strip() for line in objetos]
    temas.append(objetos)
while True:
    chances = 7
    palavra_secreta = []
    palavra_descoberta = []
    escolhe = random.randint(0, len(temas)-1)
    palavra = random.choice(temas[escolhe]).strip().upper()
    nomes = { 0:'alimentos', 1:'animais', 2:'objetos'}
    if escolhe == 0:
        print(f'Tema: {nomes[escolhe]}')
    else:
        if escolhe:
            print(f'Tema: {nomes[escolhe]}')
        
    for char in palavra:
        palavra_secreta.append(char)
    palavra_descoberta = palavra_secreta.copy()

    for char in range(len(palavra_descoberta)):
        if palavra_descoberta[char] == ' ':
            palavra_descoberta[char] = " "
        else:
            palavra_descoberta[char] = '_'



    while '_' in palavra_descoberta:
        print(' '.join(palavra_descoberta))
        chute = str(input('Qual letra deseja chutar? ')).strip().upper()
        if chute in palavra_secreta:
            for char in range(len(palavra_descoberta)):
                if chute == palavra_secreta[char]:
                    palavra_descoberta[char] = chute
                    continue
        else:
            chances -= 1
            print(f'Chances restantes: {chances}.')
            if chances == 0:
                break
    if '_' in palavra_descoberta:
        print(f'Você perdeu. \n' + 'A palavra era ' + ''.join(palavra_secreta))
    else:
        print(f'Você acertou! \n' + ''.join(palavra_descoberta))
    
                      