import sys
import pygame

pygame.init()
w = pygame.display.set_mode((1280, 720))

def getPos(a, b, f):
    arr = []
    x = min(a, b)
    while x < max(a, b):
        x += 0.1
        pos = x, f(x)
        arr.append(pos)
    return arr

def draw_function(a, b, f):
    while True:
        pygame.display.flip()
        w.fill((255, 255, 255))

        arr = getPos(a, b, f)
        s = 50
        pos = arr[0]
        last_pos = (pos[0] * s + 1280 / 2), (-pos[1] * s + 1280 / 2)
        for pos in arr:
            new_pos = (pos[0] * s + 1280 / 2), (-pos[1] * s + 1280 / 2)
            pygame.draw.line(w, (0, 0, 0), last_pos, new_pos)
            last_pos = new_pos

        black = (200, 200, 200)
        x = 0
        while x < 1280:
            x += 50
            pygame.draw.line(w, black, (x, 0), (x, 1280))
            pygame.draw.line(w, black, (0, x), (1280, x))

        pygame.draw.line(w, (0,0,255), (-8 * 50 + 10 + 1280 / 2, 0), (-8 * 50 + 1280 / 2 + 10, 720))
        pygame.draw.line(w, (0,0,255), (-7.5 * 50 + 1280 / 2 + 10, 0), (-7.5 * 50 + 1280 / 2 + 10, 720))

        pygame.draw.line(w, (0, 255, 0), (0, 1280 / 2 + 10), (1280, 1280/2 + 10))
        pygame.draw.line(w, (0, 255, 0), (1280/2 + 10, 1280), (1280 / 2 + 10, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
