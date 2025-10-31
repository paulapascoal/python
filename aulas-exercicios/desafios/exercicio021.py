import pygame.mixer
from time import sleep

pygame.init();
print('\033[35mReproduzindo áudio...\033[3m');
pygame.mixer.music.load('audio.mp3');

input();
print('Sua cultura musical aumentou um pouquinho mais. Parabéns!!!:)')
pygame.event.wait();


