import pygame 
from sys import exit
import random 

pygame.init()

class Snake(object):
    def __init__(self,color):
        self.length = 1 
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = color
    
    def get_head_position(self):
        return self.position[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.get_head_position()
        x ,y = self.direction
        new = (((current[0] + (x * GRID_SIZE) ) % WIDTH), (current[1] + (y * GRID_SIZE) % HEIGHT))
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else: 
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self, score ):
        self.length = 1
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
    
    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1])), (GRID_SIZE, GRID_SIZE)


class Food(object):
    pass


def drawGrid(surface):
    for y in range(int(GRID_HEIGHT)):
        for x in range(int(GRID_WIDTH)):
            rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            # checkerboard pattern
            color = gray1 if (x + y) % 2 == 0 else gray2
            pygame.draw.rect(surface, color, rect)


# Game variables 
HEIGHT = 480
WIDTH = 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE
gray1 = (120, 120, 120)
gray2 = (170, 170, 170)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1 , 0)
RIGHT = (1 , 0)
snake_color = (100, 200 , 0)

running = True

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32 )

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    drawGrid(surface)

    snake = Snake(snake_color)
    food = Food()

    score = 0

    while running:
        clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # snake and food function 
        drawGrid(surface)

        pygame.display.update()

main()
