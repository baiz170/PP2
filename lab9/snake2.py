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
WHITE = (255, 255, 255)
SPEED_INCREMENT = 2
FOOD_LIFETIME = 5000  # Food disappears after 5 seconds

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font for displaying food timer
font = pygame.font.Font(None, 24)

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

        return True

    def grow(self, value):
        #Increase snake size based on food weight#
        self.growing = True
        self.score += value

        # Increase level and speed every 3 points
        if self.score % 3 == 0:
            self.level += 1
            self.speed += SPEED_INCREMENT

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self, snake):
        self.position = self.generate_position(snake)
        self.value = random.choice([1, 2, 3])  # Food has different weights
        self.spawn_time = pygame.time.get_ticks()  # Track spawn time

    def generate_position(self, snake):
        #Generate food at a random position not occupied by the snake#
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake.body:
                return (x, y)

    def is_expired(self):
        """Check if food lifetime has expired"""
        return pygame.time.get_ticks() - self.spawn_time > FOOD_LIFETIME

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))
        # Display countdown timer above the food
        time_left = max(0, (FOOD_LIFETIME - (pygame.time.get_ticks() - self.spawn_time)) // 1000)
        timer_text = font.render(str(time_left), True, WHITE)
        screen.blit(timer_text, (self.position[0] + 5, self.position[1] - 20))

# Game loop
snake = Snake()
food = Food(snake)
running = True

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle snake movement
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
        snake.grow(food.value)
        food = Food(snake)  # Generate new food

    # Check if food expires
    if food.is_expired():
        food = Food(snake)  # Replace expired food

    # Draw game objects
    snake.draw()
    food.draw()

    # Draw score and level
    score_text = font.render(f"Score: {snake.score}", True, BLUE)
    level_text = font.render(f"Level: {snake.level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(snake.speed)

pygame.quit()
