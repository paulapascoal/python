from time import sleep
print('Já pensou em ter a casa própria. Vamos analisar se esse sonho já é possível.')
nome = str(input('Digite seu nome: ')).strip();
casa = float(input('Qual o valor da casa que você deseja comprar?R$ '))
salario = float(input('Quanto é o seu salário atual? '))
parcelamento = float(input('Quantas parcelas você deseja fazer para comprar a casa? '))
print('Vamos analisar seu financiamento. Só um momento...')
sleep(2.5)
tempo = parcelamento * 12
prestacao = casa / tempo;
limite = salario * 0.30;
if prestacao <= limite:
    print(f'O tempo que você vai levar pagando a casa será de {tempo:.1f} meses.')
    print(f'A sua parcela por mês da casa será fixa no valor de R${prestacao:.2f}. Sendo assim o seu parcelamento foi \033[1;32mAPROVADO\033[m.')
elif prestacao > limite:
    print(f'O tempo que você vai levar pagando a casa será de {tempo:.1f} meses.')
    print(f'A sua parcela por mês da casa será fixa no valor de R${prestacao:.2f}. Sendo assim o seu parcelamento foi \033[1;31mNEGADO\033[m.')
print('Tenha um bom dia! Para quaisquer dúvida pode entrar em contato conosco.')