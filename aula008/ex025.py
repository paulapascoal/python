'''import math
angulo = float(input('Digite o ângulo que você deseja: '));
seno = math.sin(math.radians(angulo));
cosseno = math.cos(math.radians(angulo));
tangente = math.tan(math.radians(angulo));
print(f'O ângulo de {angulo}º tem o Seno de {seno:.2f}, o Cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}.')'''

from math import radians,sin,cos,tan

angulo = float(input('Digite o ângulo que voce deseja: '));
seno = sin(radians(angulo));
cosseno = cos(radians(angulo));
tangente = tan(radians(angulo));
print(f'O angulo de {angulo}º tem o Seno de {seno:.2f}, o Cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}.')
