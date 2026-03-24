import pygame
import sys

pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

CZARNY = (0, 0, 0)

middle = (width // 2, height // 2)

image = pygame.image.load("obraz.jpg")
image = pygame.image.load("obraz.jpg").convert_alpha()
image = pygame.transform.smoothscale(image, (100, 100))

win.blit(image, (0, 0))
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scaled = pygame.transform.smoothscale(image, (int(width * 0.35), int(height * 0.35)))
                win.fill(CZARNY)
                win.blit(scaled, ((width - scaled.get_width()) // 2, (height - scaled.get_height()) // 2))
                pygame.display.flip()
            elif event.key == pygame.K_2:
                rotated = pygame.transform.rotate(image, 45)
                win.fill(CZARNY)
                win.blit(rotated, ((width - rotated.get_width()) // 2, (height - rotated.get_height()) // 2))
                pygame.display.flip()
            elif event.key == pygame.K_3:
                flipped = pygame.transform.flip(image, 0, 1)
                win.fill(CZARNY)
                win.blit(flipped, ((width - flipped.get_width()) // 2, (height - flipped.get_height()) // 2))
                pygame.display.flip()
            elif event.key == pygame.K_4:
                scale = pygame.transform.smoothscale(image, (int(width * 0.35), height))
                rotozoom = pygame.transform.rotozoom(scale, 45, 1)
                win.fill(CZARNY)
                win.blit(rotozoom, ((width - rotozoom.get_width()) // 2, (height - rotozoom.get_height()) // 2))
                pygame.display.flip()
            elif event.key == pygame.K_5:
                top_scaled = pygame.transform.smoothscale(image, (width, int(height * 0.35)))
                win.fill(CZARNY)
                win.blit(top_scaled, ((width - top_scaled.get_width()) // 2, 1))
                pygame.display.flip()
            elif event.key == pygame.K_6:
                scaled_2 = pygame.transform.smoothscale(image, (int(width * 0.35), height))
                rotozoom = pygame.transform.rotozoom(scaled_2, 180, 1)
                win.fill(CZARNY)
                win.blit(rotozoom, ((width - rotozoom.get_width()) // 2, (height - rotozoom.get_height()) // 2))
                pygame.display.flip()
            elif event.key == pygame.K_7:
                scaled_3 = pygame.transform.smoothscale(image, (int(width * 0.5), height))
                flip = pygame.transform.flip(scaled_3, 1, 0)
                win.fill(CZARNY)
                win.blit(flip, ((width - flip.get_width()) // 2, (height - flip.get_height()) // 2))
                pygame.display.flip()
            elif event.key == pygame.K_8:
                scaled_4 = pygame.transform.smoothscale(image, (width, int(height * 0.4)))
                rotated_2 = pygame.transform.rotate(scaled_4, -20)
                win.fill(CZARNY)
                win.blit(rotated_2, ((width - rotated_2.get_width()) * 1.2, (height - rotated_2.get_height()) * 1.5))
                pygame.display.flip()
            elif event.key == pygame.K_9:
                scaled_5 = pygame.transform.smoothscale(image, (int(width * 0.35), height))
                rotozoom = pygame.transform.rotozoom(scaled_5, 90, 1)
                win.fill(CZARNY)
                win.blit(rotozoom, ((width - rotozoom.get_width() + 250) // 2, (height - rotozoom.get_height()) // 2))
                pygame.display.flip()
            else:
                win.fill(CZARNY)
                win.blit(win, (0, 0))
                pygame.display.flip()

    pygame.display.update()
