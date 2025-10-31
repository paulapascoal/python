nome = str(input('Qual é o seu nome completo? ')).strip();
print('Analisando seu nome...');
print(f'Seu nome em maiúsculas {nome.upper()} e em minúsculo é {nome.lower()}.');
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count('')));
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])));
