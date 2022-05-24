import pygame
import sys

WIDTH = 800
ROWS = 20
BLACK = (0, 0, 0)
WHITE = (230, 230, 230)
RED = (255, 0, 0)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * WIDTH
        self.y = col * WIDTH
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

def makeGrid(rows, width):
    grid = []
    gap = width // rows
    for x in range(rows):
        grid.append([])
        for y in range(rows):
            node = Node(x, y, gap, rows)
            grid[x].append(node)
    return grid

def drawGrid(window, rows, width):
    gap = width // rows
    for x in range(rows):
        pygame.draw.line(window, BLACK, (0, x*gap), (width, x*gap))
        for y in range(rows):
            pygame.draw.line(window, BLACK, (y*gap, 0), (y*gap, width))

def draw(window, grid, rows, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
    
    drawGrid(window, rows, width)
    pygame.display.update()

def handleMouseDown():
    pos = pygame.mouse.get_pos()
    column = pos[0] // (WIDTH)
    row = pos[1] // (WIDTH)
    print(pos[0]/WIDTH*50)
    print(pos[1]/WIDTH*50)
    print("Click ", pos, "Grid coordinates: ", row, column)

def main():
    global display
    pygame.init()
    display = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Pathfinding Visualization')

    grid = makeGrid(ROWS, WIDTH)
    print(grid[0][0].color)
    while True:
        draw(display,grid,ROWS,WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handleMouseDown()

if __name__ == '__main__':
    main()