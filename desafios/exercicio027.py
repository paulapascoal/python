print('Vamos vê qual é o primeiro e o último nome do nosso usuário!!!');
nome = str(input('Digite seu nome completo: ')).strip();
limite = nome.split();
primeiro = limite [0];
ultimo = limite[-1];
print(f'Seu nome completo é: {nome}');
print(f'Seu primeiro nome é {primeiro} e seu último nome é {ultimo}');

