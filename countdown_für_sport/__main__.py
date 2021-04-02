import pygame
import time
from pygame import mixer
time.sleep(3)

pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 46, '46'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

effect_get_ready = pygame.mixer.Sound('get_ready.wav')
effect_start = pygame.mixer.Sound('start.wav')
effect_done = pygame.mixer.Sound('done.wav')


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Done!'
            if counter == 45:
                effect_get_ready.play()
            elif counter == 40:
                effect_start.play()
            elif counter == 0:
                effect_done.play()
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)
