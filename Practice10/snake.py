import pygame
from color_palette import *
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)
image_game_over = font.render("Game Over", True, colorRED)
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
sc_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
CELL = 30

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            if j != 0:
                pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1
        self.alive = True

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x > WIDTH // CELL - 1 or self.body[0].x < 0:
            self.alive = False
        if self.body[0].y > HEIGHT // CELL - 1 or self.body[0].y == 0:
            self.alive = False

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 1
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)
            self.level = 1 + self.score // 3

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(self.pos.x == s.x and self.pos.y == s.y for s in snake_body) and self.pos.y > 0:
                break

FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()
food.generate_random_pos(snake.body)

running = True
while running:

    score = snake.score
    level = snake.level

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP:
                snake.dx, snake.dy = 0, -1

    if not snake.alive:
        stra = f"Score: {score}  Level: {level}"
        sc_r = font.render(stra, True, colorRED)

        screen.fill(colorBLACK)
        screen.blit(image_game_over, image_game_over_rect)
        screen.blit(sc_r, sc_rect)
        pygame.display.flip()

        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()   # <-- ВАЖНО

    sc = font.render(f'Score: {score}', True, colorWHITE)
    lv = font.render(f'Level: {level}', True, colorWHITE)

    screen.fill(colorBLACK)
    draw_grid()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    screen.blit(sc, (2, 0))
    screen.blit(lv, (120, 0))

    pygame.display.flip()
    clock.tick(FPS + level)

pygame.quit()