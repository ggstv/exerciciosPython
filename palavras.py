def carregaJogo():

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