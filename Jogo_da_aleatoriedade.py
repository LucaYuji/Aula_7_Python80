'''
Pensar sobre o sistema:
1- criar numero aleatório
2- digitar nome dos jogadores
3- comparar qual dos jogadores escolheu o numero certo
4- mostrar quem ganhou o jogo
5- 3 chances

dividir em pedaços, criar resolução
'''
import random

print('Sejam bem vindos ao jogo aleatório: ')
print('')
print('_._._._._._._._._._._._._._._._._._._._._._._')
print('')
print('Digitem seus usuários e escolha um número: ')

user1 = input('User 1 >> ')
user2 = input('User 2 >> ')

print(f'Sejam Bem vindos(as) {user1} e {user2}')
a = int(input(f'{user1} Digite seu {user1} >> '))
b = int(input(f'{user2} Digite seu {user2} >> '))
print('Vocês criaram uma aleatoriedade de ', a, 'e', b - 1)
chances = [5,4,3,2,1]

for i in chances:
    rand = random.randint(a,b)
    escolha_user1 = int(input(f'Escolha um número {user1} : '))
    escolha_user2 = int(input(f'Escolha um número {user2} : '))

    i -= 1
    if escolha_user1 == escolha_user2 == rand:
        print('Empataram !!')
        break
    elif escolha_user1 == rand and escolhauser1 != escolha_user2:
        print('O jogador 1 ganhou o jogo')
        break
    elif escolha_user2 == rand and escolhauser1 != rand:
        print('O jogador 2 ganhou o jogo')
        break
    elif rand != escolha_user1 and rand != escolha_user2:
        print(f'Vocês erraram,o número sorteado foi >> {rand} !')
        if 1 <= 0:
            print(f'Esgotaram, {i} chances>> {i}')
