frase = 'Curso em Vídeo Pyhton';
#print(frase.count('o')); #conta quantas vezes tem o parametro que estamos solicitando
#print(len(frase)); #o comprimento de uma string
#print(frase.find('Android')); #tenta localizar uma string. OBS=caso ela não tenha volta o resultado de -1
frase = frase.replace('Python', 'Android');
print(frase); #altera uma palavra por outra solicitada
#print(frase.upper()); #coloca todas as string em letras maíusculas
#print(frase.lower()); #coloca todas as string em letras mínusculas
#print(frase.split()); #coloca as string em uma lista cada elemento tem seu espaço como limitador
#print('-'.join(frase)) #ele vai colocar em todos os espaços um - ele é o oposto do split
#print(frase[3:13]) #estabelece um limite de quando começa termina e o passo
#frase = '   Apredendendo Python  ';
#print(frase.strip()); #elimina todos os espaços sem necessidade que se encontra no texto
#print(frase.rstrip()); #para eliminar espaços à direita do texto usamos rstrip
#print(frase.lstrip()); #para eliminiar espaços a esquerda usamos lstrip
