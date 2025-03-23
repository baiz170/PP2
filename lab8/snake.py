import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SPEED_INCREMENT = 2

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)
        self.growing = False
        self.speed = 10
        self.level = 1
        self.score = 0
    
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check for collisions with walls
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            return False
        
        # Check for collisions with itself
        if new_head in self.body:
            return False
        
        self.body.insert(0, new_head)
        
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
            self.score += 1
            
            # Increase level every 3 points
            if self.score % 3 == 0:
                self.level += 1
                self.speed += SPEED_INCREMENT
        
        return True
    
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self, snake):
        self.position = self.generate_position(snake)
    
    def generate_position(self, snake):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake.body:
                return (x, y)
    
    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Game loop
snake = Snake()
food = Food(snake)
running = True

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.direction != (0, CELL_SIZE):
        snake.direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake.direction != (0, -CELL_SIZE):
        snake.direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake.direction != (CELL_SIZE, 0):
        snake.direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-CELL_SIZE, 0):
        snake.direction = (CELL_SIZE, 0)
    
    if not snake.move():
        print("Game Over!")
        running = False
    
    # Check for food collision
    if snake.body[0] == food.position:
        snake.growing = True
        food = Food(snake)
    
    snake.draw()
    food.draw()
    
    # Draw score and level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {snake.score}", True, BLUE)
    level_text = font.render(f"Level: {snake.level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.update()
    clock.tick(snake.speed)

pygame.quit()
