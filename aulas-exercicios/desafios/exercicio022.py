print('Vamos analisar um nome completo.')
nome = str(input('Qual é o seu nome?'));
print(nome.upper());
print(nome.lower());
espaco = nome.replace(' ', '');
contagem = len(espaco)
print(espaco)
print(contagem)
primeiro = nome.split();
print(len(primeiro[0]));