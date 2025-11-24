from time import sleep
from datetime import date
print('Qual sua equipe na Confederação Nacional de Natação.')
atual = date.today().year
nome = str(input('Digite seu nome completo: '))
nascimento = int(input('Digite seu ano de nascimento: '))
print('Analisando sua faixa etária...')
sleep(2)
if atual - nascimento <= 9:
    print(f'{nome} você tem {atual - nascimento} anos. Por isso você está na faixa etária \033[1;31mMIRIM\033[m.')
elif 14 >= atual - nascimento >= 9:
    print(f'{nome} você tem {atual - nascimento} anos. Por isso você está na faixa etária \033[1;32mINFANTIL\033[m. ')
elif 19 >= atual - nascimento >= 14:
    print(f'{nome} você tem {atual - nascimento} anos. Por isso você está na faixa etária \033[1;33mJÚNIOR\033[m.')
elif 25 >= atual - nascimento >= 19:
    print(f'{nome} você tem {atual - nascimento} anos. Por isso você está na faixa etária \033[1;34mSÊNIOR\033[m.')
else:
    print(f'{nome} você tem {atual - nascimento} anos. Por isso você está na faixa etária \033[1;35mMASTER\033[m.')
print('Parabéns por seu espírito esportivo!!!')