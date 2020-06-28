import pygame as pg

TILESIZE = 40
GRIDWIDTH = 28
GRIDHEIGHT = 15
WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
DARKGRAY = (40, 40, 40)
LIGHTGRAY = (140, 140, 140)

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        # which direction can you travel in from given tile only allowing up down left right
        # used to calculate neighbors of given node
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        # walls / edge cases


def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))


running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.quit():
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
