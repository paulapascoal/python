from time import sleep;
print('Dos número que você digitou qual é o maior e o menor...');
n1 = int(input('Informe o primeiro número: '));
n2 = int(input('Informe o segundo número: '));
n3 = int(input('Informe o terceiro número: '));
print('Analisando os números...');
sleep(1);
l = [n1,n2,n3];
l.sort();
print(f'O maior número é {l[2]} e o menor {l[0]}.');

