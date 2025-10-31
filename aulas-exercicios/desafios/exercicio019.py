import random
print("Quem vai limpar o Quadro roof os tambores")
aluno1 = input('Digite o nome do Primeiro Aluno: ');
aluno2 = input('Digite o nome do Segundo Aluno: ');
aluno3 = input('Digite o nome do Terceiro Aluno: ');
aluno4 = input('Digite o nome do Quarto Aluno: ');
sorteio =   (aluno1,aluno2,aluno3,aluno4);
escolhido = random.choice(sorteio);
print(f'O aluno escolhido para limpar o quadro foi {escolhido}');