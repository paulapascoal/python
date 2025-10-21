print('Analisando um número escrito e a casa que ocupa.')
num = int(input('Digite um número entre 0 e 9999: '));
print(f'Vamos dissecar o número digitado...');
print(f'O número {num} tem {num // 1000%10} milhar, {num //100%10} centena, {num //10%10} dezena e {num//1%10} unidade');