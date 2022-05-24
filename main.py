import pygame
import sys

WIDTH = 900

pygame.init()

display = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Pathfinding Visualization')


def main():
    while True:
          # creating a loop to check events that are occurring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # updating the display
        pygame.display.flip()

if __name__ == '__main__':
    main()