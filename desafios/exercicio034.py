print('Qual será o valor do seu aumento!!!');
salario = float(input('Qual é o seu salário atual? R$: '));
if salario >=1250:
    aumento = (salario * 0.10) + salario;
    print(f'O seu salário atual é de R${salario:.2f} por isso o seu aumento vai ser de 15%. Sendo assim o seu novo salário será de R${aumento:.2f}.');
else:
    aumento = (salario * 0.15) + salario;
    print(f'O seu salário atual é de R${salario:.2f} por isso o seu aumento vai ser de 10%. Sendo assim o seu novo salário será de R${aumento:.2f}.');
