print('Vamos fazer a comparação de 2 números inteiros.')
from time import sleep
num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe um segundo número inteiro: '))
print('Analisando...')
sleep(1.5)
if num1 > num2:
    print(f'O número  \033[2;33m{num1}\033[m é maior que o número {num2}\033[m.')
elif num2 > num1:
    print(f'O número \033[2;36m{num2}\033[m é maior que o número \033[2;33m{num1}\033[m.')
elif num1 == num2:
    print(f'O \033[2;33m{num1}\033[m e \033[2;36m{num2}\033[m são valores iguais.')
print('Obrigado por ter participado da nossa brincadeira. Tenha um bom dia ;)')