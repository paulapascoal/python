from time import sleep
print('Quanto será o valor da sua passagem?');
distancia = float(input('Quantos KM tem sua viagem? '));
print('Calculando...');
if distancia <= 200:
    valor = distancia * 0.50;
    print(f'Sua viagem de {distancia}Km terá um valor de R$ {valor:.2f}.');
else:
        valor = distancia * 0.45;
        print(f'Sua viagem de {distancia}Km terá um valor de R$ {valor:.2f}');
print('Tenha um bom dia!');
