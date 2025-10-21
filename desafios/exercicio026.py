print("Quantas letras A tem sua frase e quando aparece primeiro e por último");
frase = str(input('Digite uma frase: '));
frase_maiusculo = frase.upper()
maiusculo = frase_maiusculo.count('A');
primeira = frase_maiusculo.find('A');
ultimo = frase_maiusculo.rfind('A');
print(f'Sua frase possui {maiusculo} letras "A" e a letra A aparece pela primeira vez em {primeira} espaço e pela última vez em {ultimo}.');