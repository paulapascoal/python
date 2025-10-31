"""tempo = int(input('Quantos anos tem o seu carro: '));
if tempo <=3:
    print('Teu carro é novo ;)');
else:
    print('Eitaa seu carro ta veinho já podemos pensar em se organizar para comprar um modelo mais novo.')"""

tempo = int(input('Quantos anos tem o seu carro: '));
print(f'Carro Novo' if tempo <=3 else 'Carro Velho');
print('--Fim--')