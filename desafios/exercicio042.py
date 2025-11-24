from time import sleep
print('Os valores digitado equivale a qual tipo de triângulo. Escaleno, Equilátereo ou Isósceles')
lado1 = float(input('Digite o valor do Primeiro Lado: '))
lado2 = float(input('Digite o valor do Segundo Lado: '))
lado3 = float(input('Digite o valor do Terceiro Lado: '))
print('Analisando os dados...')
sleep(1.5)
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Os valores permitem formar um triângulo.')
    if lado1 == lado2 and lado1 == lado3:
         print('Com os valores digitados o triângulo que podemos formar é do tipo: \033[1;32m  Equilátereo.\033[m')
    elif lado1 == lado2 and lado2 != lado3 or lado3 == lado2 != lado1 or lado3 == lado1 != lado2:
          print('Com os valores digitados o triângulo que podemos formar é do tipo: \033[1;36m Isósceles.\033[m')
    else:
        print('Com os valores digitados o triângulo que podemos formar é do tipo: \033[1;35m Escaleno\033[m')
else:
    print('Com os valores digitados \033[1;31mNÃO É POSSÍVEL\033[m formar um triângulo.')
print('Esperamos que tenha ajudado a tirar a dúvida :)')

