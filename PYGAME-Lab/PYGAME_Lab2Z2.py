import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")

NIEBIESKI = (0, 0, 255)
BIALY = (255,255,255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill(BIALY)
    pygame.draw.rect(win, NIEBIESKI, (100, 200, 400, 200))
    pygame.draw.polygon(win, NIEBIESKI, ([300, 200], [200, 0], [400, 0]))
    pygame.draw.polygon(win, NIEBIESKI, ([300, 400], [200, 600], [400, 600]))
    pygame.display.update()

