'''import random
n1 = str(input('Primeiro Aluno: '));
n2 = str(input('Segundo Aluno: '));
n3 = str(input('Terceiro Aluno: '));
n4 = str(input('Quarto Aluno: '));
lista = [n1, n2, n3, n4];
random.shuffle(lista);
print(f'A ordem de apresentação será:');
print(lista);'''

from random import shuffle
aluno = str(input('Escreva o nome dos aluno: ')).split(",");
shuffle(aluno);
print(f'A ordem de apresentação será {aluno}');
