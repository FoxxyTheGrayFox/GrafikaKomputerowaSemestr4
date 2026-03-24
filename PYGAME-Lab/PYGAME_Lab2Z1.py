import pygame
import sys

pygame.init()

width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

CZARNY = (0, 0, 0)

image = pygame.image.load("obraz.jpg").convert_alpha()
image = pygame.transform.smoothscale(image, (100, 100))

def center(surface, offset_x=0, offset_y=0):
    win.fill(CZARNY)
    win.blit(surface, ((width - surface.get_width()) // 2 + offset_x,(height - surface.get_height()) // 2 + offset_y))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scaled = pygame.transform.smoothscale(image,(int(width * 0.35), int(height * 0.35)))
                center(scaled)
            elif event.key == pygame.K_2:
                rotated = pygame.transform.rotate(image, 45)
                center(rotated)
            elif event.key == pygame.K_3:
                flipped = pygame.transform.flip(image, 0, 1)
                center(flipped)
            elif event.key == pygame.K_4:
                scale = pygame.transform.smoothscale(image,(int(width * 0.35), height))
                rotozoom = pygame.transform.rotozoom(scale, 45, 1)
                center(rotozoom)
            elif event.key == pygame.K_5:
                top_scaled = pygame.transform.smoothscale(image,(width, int(height * 0.35)))
                center(top_scaled, 0, -height // 2 + top_scaled.get_height() // 2)
            elif event.key == pygame.K_6:
                scaled_2 = pygame.transform.smoothscale(image,(int(width * 0.35), height))
                rotozoom = pygame.transform.rotozoom(scaled_2, 180, 1)
                center(rotozoom)
            elif event.key == pygame.K_7:
                scaled_3 = pygame.transform.smoothscale(image,(int(width * 0.5), height))
                flipped = pygame.transform.flip(scaled_3, 1, 0)
                center(flipped)
            elif event.key == pygame.K_8:
                scaled_4 = pygame.transform.smoothscale(image,(width, int(height * 0.4)))
                rotated_2 = pygame.transform.rotate(scaled_4, -20)
                center(rotated_2,int((width - rotated_2.get_width()) * 0.2),int((height - rotated_2.get_height()) * 0.5) )
            elif event.key == pygame.K_9:
                scaled_5 = pygame.transform.smoothscale(image,(int(width * 0.35), height))
                rotozoom = pygame.transform.rotozoom(scaled_5, 90, 1)
                center(rotozoom, 250 // 2)
            else:
                win.fill(CZARNY)

    pygame.display.update()

pygame.quit()
sys.exit()
