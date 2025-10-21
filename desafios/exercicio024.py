print("A sua cidade começa ou não com Santo?")
cidade = str(input('Digite o nome da sua cidade: ')).strip()
d = cidade.split();
print(f'A cidade começa com "Santo?"{'Santo' in d[0].capitalize()}');
