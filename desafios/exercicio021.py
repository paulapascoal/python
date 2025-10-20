import pygame.mixer
from time import sleep
pygame.mixer.init();
try:
    pygame.mixer.music.load('audio.mp3');
except pygame.error:
    print('Eita deu erro ao tentar carregar o arquivo. Verifique se o nome está correto.');
print('Reproduzindo áudio...');
pygame.mixer.music.play();
print('Reprodução Finalizada.')

