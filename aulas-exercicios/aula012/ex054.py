nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando a {nota1 :.1f} e {nota2 :.1f}, a média do aluno é {media}.')
if 7 > media >=5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print ('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')