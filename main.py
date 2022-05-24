import pygame
import sys

WIDTH = 800
BLACK = (0, 0, 0)
WHITE = (230, 230, 230)

def drawGrid():
    blockSize = 40
    for x in range(0, WIDTH, blockSize):
        for y in range(0, WIDTH, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(display, BLACK, rect, 1)

def main():
    global display
    pygame.init()
    display = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Pathfinding Visualization')
    display.fill(WHITE)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()