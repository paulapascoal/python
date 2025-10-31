from time import sleep
print('Vamos abreviar para saber se um número é Binário, Octogonal ou Hexadecimal.')
num = int(input('Informe um número: '))
binario = bin(num)
octogonal = oct(num)
hexadecimal = hex(num)
escolha = str(input('Informe uma opção: Binário, Octogonal, Hexadecimal: '))
print('Analisando...')
sleep(1)
if escolha == 'Binário':
    print(f'O número \033[1;32m{num}\033[m em binário é {binario}')
elif escolha == 'Octogonal':
    print(f'O numero \033[3;35m{num}\033[m em octogonal é {octogonal}')
elif escolha == 'Hexadecimal':
    print(f'O numero \033[5;36m{num}\033[m em hexadecimal é {hexadecimal}')
else:
    print('Opção INVÁLIDA tente novamente.')
print('Só um momento.')
sleep(1.5)
print('Obrigado por participar da nossa brincadeira!!!')



