from time import sleep
print('Chegou a época do Alisamento Militar. Vamos analisar sua situação.')
nome = str(input('Digite seu nome completo: ')).strip()
idade = int(input('Informe sua idade: '))
print('Analisando sua situação...')
sleep(1.5)
if idade == 18:
    print(f'Verificando os dados {nome} por conta da sua idade de {idade} anos está na época de fazer o alistamento obrigatório.')
elif idade < 18:
    falta = 18 - idade
    print(f'Verificando os dados {nome} por conta da sua idade de {idade} ainda falta {falta} anos para o alistamento.')
else:
    passou = 18 + idade
    print(f'Verificando os dados {nome} você não fez o alistamento na época correta se passou {passou} tempo do alistamento. Você esta com essa pendência. Dirija-se ao Quartel mais próximo e regularize sua situação.')
print('Tenha um bom dia! \U0001F468\u200D\U0001F396\uFE0F')