import random
print ("Vamos a ordem de apresentação dos trabalhos: ");
grupo1 = str(input("Digite o nome do Grupo 1: "));
grupo2 = str(input("Digite o nome do Grupo 2: "));
grupo3 = str(input("Digite o nome do Grupo 3: "));
grupo4 = str(input("Digite o nome do Grupo 4: "));
grupos = [grupo1,grupo2,grupo3,grupo4];
random.shuffle(grupos);
print(f"A ordem de apresentação dos aluno vai ser:");
print(grupos);