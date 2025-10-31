from time import sleep
print('E aí. O ano que você escolheu é ou não bissexto');
ano = int(input('Digite um ano qualquer: '));
print('Analisando os Dados...')
sleep(1);
if ano % 4 == 0:
    print(f'O ano que você escolheu {ano} é Bissexto.');
else:
    print(f'O ano que você escolheu {ano} não é Bissexto.');
print('E ai gostou de saber se o ano é não Bissexto.')