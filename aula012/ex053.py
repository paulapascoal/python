from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = atual + 18
    print(f'Você ainda não tem 18 anos. Ainda faltam {idade - 18} anos para o ALISTAMENTO.')
    print(f'Seu alistamento será em {saldo}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado a {saldo} anos.')
    print(f'Seu alistamento deveria ter sido em {ano}')
