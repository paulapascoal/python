from time import sleep
print('Quanto vai ficar o valor final da sua compra.')
preco = float(input('Qual é o valor da sua compra? R$'))
print('''Qual vai ser a forma de pagamento?
[1] Dinheiro/PIX/Cheque
[2] Cartão à vista
[3] Parcelamento em até 2x.
[4] Parcelamento 3x ou mais.
''')
opcao = int(input('Digite o número que corresponde a forma de pagamento: '))
print('Só um momento...')
sleep(2)
if opcao == 1:
    desconto = preco * 0.10
    pagamento = preco - desconto
    print(f'Como a forma de pagamento escolhida foi {opcao} a sua compra teve um desconto de 10% sendo assim o valor final da sua compra foi R${pagamento:.2f}.')
elif opcao == 2:
    desconto = preco * 0.05
    pagamento = preco - desconto
    print(f'Como a forma de pagamento escolhida foi {opcao} a sua compra teve um desconto de 5% sendo assim o valor final da sua compra foi R${pagamento:.2f}.')
elif opcao == 3:
    print(f'Sua forma de pagamento escolhida foi {opcao}. Foi R${preco:.2f}.')
elif opcao == 4:
    juros = preco * 0.20
    pagamento = preco + juros
    print(f'Como a forma de pagamento escolhida foi {opcao} a sua compra teve um juros de 20% sendo assim o valor final da sua compra foi R${pagamento:.2f}')
