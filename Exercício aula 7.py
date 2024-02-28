import random

n = [4,3,2,1]

for c in n:
    numero_correto = random.randint(1,2)
    number1 = int(input('Primeiro jogador digite um número: '))
    number2 = int(input('Segundo jogador digite um número: '))
    c = c - 1
    
    if numero_correto == number1:
        print(f'O jogador 1 acertou: {numero_correto}')
        break
    
    if numero_correto == number2:
        print(f'O jogador 2 acertou: {numero_correto}')
        break
    
    elif numero_correto != number1 or number2 and numero_correto > 0:
        print(f'Ambos erraram, o número é: {numero_correto}, vocês tem {c} chances')
        if c == 0:
            print(f'acabaram todas as chances, total de chances = {c}')
            break
            

