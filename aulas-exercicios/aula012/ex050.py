casa = float(input('Valor da casa R$: '))
salario = float(input('Salário do comprador: R$ '));
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12);
minimo = salario * 30 /100;
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos. A prestação será de R${prestacao:.2f}')
print(f'Comaprando tem que pagar {prestacao:.2f} e o minimo é de {minimo:.2f}')
print('--'*20)
if prestacao <= minimo:
    print(f'Empréstimo pode ser \033[1;32mCONCEDIDO!\033[m')
else:
    print('Empréstimo \033[1;31mNEGADO\033[m')