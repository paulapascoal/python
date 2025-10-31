from time import sleep
print('Vamos vê se vai ter ou não multa...');
velocidade = float(input('Informe a velocidade do seu carro: '));
print('PROCESSANDO...')
sleep(2)
if velocidade >80:
    multa = (velocidade - 80) *7;

    print(f'Sua velocidade é de {velocidade}Km/H por isso vamos ter uma multa de R${multa:.2f}')
else:
    print(f'Sua velocidade atual é de {velocidade}Km/H. Parabéns você está sendo um motorista exemplar.')