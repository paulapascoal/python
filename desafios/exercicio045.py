from time import sleep
from random import choice
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
print('''As opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
escolha = int(input('Escolha uma opção: '))
opcoes = [pedra, papel, tesoura]
escolhido = choice(opcoes)
usuario = opcoes [escolha]
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print(f'Computador escolheu: {escolhido}')
print(f'O usuário escolheu: {usuario}')
if usuario == escolhido:
    print('O jogo EMPATOU.')
elif (escolhido == 'PEDRA' and usuario == 'TESOURA') or (escolhido == 'PAPEL' and usuario == 'PEDRA') or (escolhido == 'TESOURA' and usuario == 'PAPEL'):
    sleep(1.5)
    print(f'Computador GANHOU \U0001F4BB!!!')
elif (usuario == 'PEDRA' and escolhido == 'TESOURA') or (usuario == 'PAPEL' and escolhido == 'PEDRA') or (usuario == 'TESOURA' and escolhido == 'PAPEL'):
    sleep(1.5)
    print(f'Jogador GANHOU \U0001F468\u200D\U0001F4BB!!!')
else:
    print('Opção inválida! Tente novamente ;(')

print('Vamos jogar de novo...')