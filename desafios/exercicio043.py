from time import sleep
print('Vamos verificar seu IMC')
nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso:(KG) '))
print('Fazendo os cálculos...')
sleep(3.5)
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Com base na sua altura {altura}m e seu peso {peso}Kg. Seu IMC é de {imc:.2f} sendo assim você é classificado como: \033[1;32mAbaixo do peso. \033[m')
elif 18.5 <= imc < 25:
    print(f'Com base na sua altura {altura}m e seu peso {peso}Kg. Seu IMC é de {imc:.2f} sendo assim você é classificado como: \033[1;33mPeso Ideal. \033[m')
elif 25 <= imc < 30:
    print(f'Com base na sua altura {altura}m e seu peso {peso}Kg. Seu IMC é de {imc:.2f} sendo assim você é classificado como: \033[1;34m Sobrepeso. \033[m')
elif 30 <= imc < 40:
    print(f'Com base na sua altura {altura}m e seu peso {peso}Kg. Seu IMC é de {imc:.2f} sendo assim você é classificado como: \033[1;35m Obesidade. \033[m')
else:
    print(f'Com base na sua altura {altura}m e seu peso {peso}Kg. Seu IMC é de {imc:.2f} sendo assim você é classificado como: \033[1;36m Obesidade Mórbida.')
print(' \033[1;31mIsso é somente para feito educativo para mais informações procure um médico responsável não os de INTERNET.\033[m')