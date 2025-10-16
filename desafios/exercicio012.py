print("Olha a Promoção");
l = input("Qual é o preço? ");
v = float(input("O preço é R$: "))
p = (0.05*v);
print(f"Mas temos um desconto de 5% em compras no Pix. O preço com o desconto é de R${v-p:.2f}.");