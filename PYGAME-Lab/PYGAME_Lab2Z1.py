import pygame
import sys

pygame.init()

width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

CZARNY = (0, 0, 0)

image = pygame.image.load("obraz.jpg").convert_alpha()
image = pygame.transform.scale(image, (150, 150))

# wysrodkowanie obrazka
def draw_centered(surface): 
    win.fill(CZARNY)
    rect = surface.get_rect(center=(width // 2, height // 2))
    win.blit(surface, rect)
    pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                img = pygame.transform.smoothscale(image, (int(width * 0.35), int(height * 0.35)))
                draw_centered(img)
            elif event.key == pygame.K_2:
                img = pygame.transform.rotozoom(image, 45, 1)
                draw_centered(img)
            elif event.key == pygame.K_3:
                img = pygame.transform.flip(image, False, True)
                draw_centered(img)
            elif event.key == pygame.K_4:
                scaled = pygame.transform.smoothscale(image, (int(width * 0.35), height))
                img = pygame.transform.rotozoom(scaled, 45, 1)
                draw_centered(img)
            elif event.key == pygame.K_5:
                img = pygame.transform.smoothscale(image, (width, int(height * 0.35)))
                draw_centered(img)
            elif event.key == pygame.K_6:
                img = pygame.transform.rotozoom(image, 180, 1)
                draw_centered(img)
            elif event.key == pygame.K_7:
                scaled = pygame.transform.smoothscale(image, (int(width * 0.5), height))
                img = pygame.transform.flip(scaled, True, False)
                draw_centered(img)
            elif event.key == pygame.K_8:
                scaled = pygame.transform.smoothscale(image, (width, int(height * 0.4)))
                img = pygame.transform.rotozoom(scaled, -20, 1)
                draw_centered(img)
            elif event.key == pygame.K_9:
                img = pygame.transform.rotozoom(image, 90, 1)
                draw_centered(img)
            else:
                win.fill(CZARNY)
                pygame.display.flip()

pygame.quit()
sys.exit()
