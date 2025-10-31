print("Vamos dar aumento de salário!!!");
nome = input("Olá qual é o seu nome?");
sal = float(input("Quanto é o seu salário hoje?"));
aum = (sal * 0.15);
print(f"Bom {nome} seu salário hoje é de {sal} devido ao seu trabalho e resultado vamos te dá um aumento de 15%. Seu novo salário vai ser de R${sal+aum:.2f} ");