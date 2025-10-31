print("Seu nome tem SILVA? S/N?");
nome = str(input('Digite seu nome completo: ')).strip();
buscar = nome.find('Silva');
print(f'Seu nome tem "Silva":{buscar}');