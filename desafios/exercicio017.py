print("E ai vamos descobrir o comprimento da hipotenusa de um triângulo retângulo.")
oposto = float(input("Informe o valor do cateto oposto:"));
adjacente = float(input("Informe o valor do cateto adjacente:"));
soma = (oposto**2) + (adjacente**2)
hipotenusa = soma**(1/2);
print(f'Tendo o cateto oposto no valor {oposto} e o cateto adjacente {adjacente} o valor da hipotenusa é de {hipotenusa:.2f}');