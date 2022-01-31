"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
 expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressao = input('Digite sua expressão: ').strip()
pilha = []
for c in expressao:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está inválida!')