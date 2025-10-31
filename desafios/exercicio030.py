from time import sleep
print('Ímpar; Par. E ai seu número é qual?');
num = int(input('Digite um número: '));
print('PROCESSANDO...');
sleep(2)
if num % 2 == 0:
    print(f'O número {num} que você escolheu é PAR!!!')
else:
    print(f'O número {num} que você escolheu é ÍMPAR!!!');
print('Obrigado por ter participado da nossa brincadeira ;)');
