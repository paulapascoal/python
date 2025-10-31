from time import sleep
print('Avaliando suas notas')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
print('Fazendo a média...')
sleep(2)
if media < 5.0:
    print(f'A media da suas notas foram {media:.2f}.Você está foi \033[31mREPROVADO\033[0m. Vai precisa tentar novamente.')
elif 5.0 <= media <= 6.9:
    print(f'A media da suas notas foram {media:.2f}. Você está de \033[32mRECUPERAÇÃO\033[0m. Terá uma nova oportunidade não desperdice.')
elif media >= 7.0:
    print(f'A media da suas notas foram {media:.2f}. Voce foi \033[34mAPROVADO\033[0m. Parabéns :) por mais essa etapa.')
print(f'O ano letivo de 2025 chega ao fim até a próxima Pequenos Gafanhotos.\U0001F596')