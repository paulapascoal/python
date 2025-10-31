print("Realizando uma Operação Aritmética");

n1 = int(input("Digite um valor: "))
n2 = int (input("Digite outro valor:"));
a = n1 + n2; #Adição
b = n1 - n2; #Subtração
c = n1 * n2; #Multiplicação
d = n1 / n2; #Divisão
e = n1 ** n2; #Potência
f = n1 // n2; #Divisão Inteira
g = n1 %  n2; #Resto da Divisão

print (f"A soma de {n1} e {n2} é {a}");
print (f"A subtração de {n1} e {n2} é {b}");
print (f"A multiplicação de {n1} e {n2} é {c}");
print (f"A divisão de {n1} e {n2} é {d}");
print (f"A potência de {n1} e {n2} é {e}");
print (f"A divisão inteira de {n1} e {n2} é {f}");
print (f"O resto da divisão entre {n1} e {n2} é {g}");
