print("Alugueis de carro para passear no Final do Ano");
aluguel = int(input('Quantos dias você ficou com o carro? '));
dias = aluguel * 60;
km = float(input('Quantos quilômetros você rodou com o carro?'));
total = km * 0.15 + dias;
print(f'Pelo {aluguel:.1f} dias que você ficou mais os {km} Km rodado o seu valor final para pagamento ficou em R${total:.2f}. Qual vai ser a forma de pagamento?')