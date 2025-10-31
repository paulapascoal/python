from time import sleep
print('Com os número que você informou será ou não possível montar um triângulo.');
lado1 = float(input('Digite o primeiro valor: '));
lado2 = float(input('Digite o segundo valor: '));
lado3 = float(input('Digite o terceiro valor: '));
print('ANALISSANDO...')
sleep(2.5);
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print(f'É POSSÍVEL formar um triângulo.');
else:
    print(f'NÃO é POSSÍVEL formar um triângulo.');