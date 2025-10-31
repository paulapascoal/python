import pygame
pygame.init();
pygame.mixer.music.load('ex028.mp3');
pygame.mixer.music.play(loops=-1);
input()
pygame.event.wait();
