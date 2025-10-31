import random
print ("\033[36mVamos a ordem de apresentação dos trabalhos:\033[0m ");
grupo1 = str(input("Digite o nome do Grupo 1: "));
grupo2 = str(input("Digite o nome do Grupo 2: "));
grupo3 = str(input("Digite o nome do Grupo 3: "));
grupo4 = str(input("Digite o nome do Grupo 4: "));
grupos = [grupo1,grupo2,grupo3,grupo4];
random.shuffle(grupos);
print(f"\033[44m A ordem de apresentação dos aluno vai ser:\033[0m");
print("\033[33m",grupos,"\033[0m");