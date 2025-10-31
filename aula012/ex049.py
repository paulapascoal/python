nome = str(input('Digite seu nome: '))
if nome == 'Paula':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Sei nome é bem normal no Brasil!')
print(f'Tenha um bom dia \033[34m{nome}\033[0m')