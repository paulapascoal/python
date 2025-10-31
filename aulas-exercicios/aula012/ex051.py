num = int(input('Informe um número inteiro: '))
print('''Escolha uma das opções das bases para a conversão
[1] Converter Binário
[2] Converter Octogonal 
[3] Converter Hexadecimal
''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para Octogonal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
