import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zadanie 1")
BLACK = (0, 0, 0)
img = pygame.image.load("obraz.jpg").convert_alpha()
img = pygame.transform.scale(img, (WIDTH // 2, HEIGHT // 3))

def shear(surface, sx=0, sy=0):
    pixels = pygame.surfarray.array3d(surface)
    w, h = surface.get_size()

    new_w = w + int(abs(sx) * h)
    new_h = h + int(abs(sy) * w)

    output = np.zeros((new_w, new_h, 3), dtype=np.uint8)

    for y in range(h):
        dx = int(sx * (h - y))

        for x in range(w):
            dy = int(sy * x)
            output[x + dx, y + dy] = pixels[x, y]

    result = pygame.surfarray.make_surface(output)
    final_surface = pygame.Surface(result.get_size())

    final_surface.fill(BLACK)
    result.set_colorkey(BLACK)
    final_surface.blit(result, (0, 0))

    return final_surface

def variant(n):
    match n:
        case 1:
            return pygame.transform.smoothscale_by(img, 0.5)
        case 2:
            return pygame.transform.rotate(img, -45)
        case 3:
            temp = pygame.transform.flip(img, False, True)
            return pygame.transform.smoothscale_by(temp, (0.6, 1.5))
        case 4:
            temp = pygame.transform.flip(img, True, False)
            temp = shear(temp, 0.4)
            return pygame.transform.flip(temp, True, False)
        case 5:
            return pygame.transform.smoothscale_by(img, (1.5, 0.6))
        case 6:
            temp = pygame.transform.flip(img, True, False)
            temp = shear(temp, 0.4)
            temp = pygame.transform.rotate(temp, 90)
            return pygame.transform.flip(temp, True, False)
        case 7:
            temp = pygame.transform.flip(img, False, True)
            temp = pygame.transform.smoothscale_by(temp, (0.6, 1.5))
            return pygame.transform.flip(temp, True, False)
        case 8:
            temp = pygame.transform.smoothscale_by(img, (1.5, 0.6))
            return pygame.transform.rotate(temp, -20)
        case 9:
            temp = pygame.transform.flip(img, True, True)
            return shear(temp, 0, 0.4)
    return img

current = 1
current_img = variant(current)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                current = event.key - pygame.K_0
                current_img = variant(current)
    screen.fill(BLACK)

    if current == 5:
        rect = current_img.get_rect(topleft=(WIDTH // 8, 0))
    elif current == 8:
        rect = current_img.get_rect(
            midbottom=(WIDTH // 2.2, HEIGHT - HEIGHT // 30)
        )
    elif current == 9:
        rect = current_img.get_rect(topright=(WIDTH, HEIGHT // 3))
    else:
        rect = current_img.get_rect(center=screen.get_rect().center)
    screen.blit(current_img, rect)
    pygame.display.update()

pygame.quit()
