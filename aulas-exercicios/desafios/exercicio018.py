print("Seno e Conseno de um Ângulo");
angulo = float(input('Informe um ângulo:'));
seno = (angulo**(1/2))/2;
cosseno = -(angulo**(1/2))/2;
tangente = seno/cosseno;
print(f'O ângulo de {angulo} tem um seno de {seno:.2f}, cosseno {cosseno:.2f} e uma tangente de {tangente:.2f}.');