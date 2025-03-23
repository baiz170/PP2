import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 700  # Adjusted for Mac screen size
ROAD_WIDTH = 500
LANE_WIDTH = ROAD_WIDTH // 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
RED = (200, 0, 0)
SAFE_DISTANCE = 40  # Minimum distance between coins and obstacles

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# Load images
car_img = pygame.image.load("/Users/madikbaizakov/Documents/vscode/PP2/lab8/car.png")
car_img = pygame.transform.scale(car_img, (60, 120))

# Player car class
class PlayerCar:
    def __init__(self):
        self.x = WIDTH // 2 - 30
        self.y = HEIGHT - 140
        self.speed = 7
        self.score = 0  # Coin counter

    def move(self, direction):
        if direction == "left" and self.x > WIDTH // 2 - ROAD_WIDTH // 2:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH // 2 + ROAD_WIDTH // 2 - 60:
            self.x += self.speed

    def draw(self):
        screen.blit(car_img, (self.x, self.y))

# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = random.choice([WIDTH//2 - LANE_WIDTH + 10, WIDTH//2 + 10])
        self.y = random.randint(-400, -100)
        self.width = 80
        self.height = 100
        self.speed = 6

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Coin class
class Coin:
    def __init__(self, obstacles):
        while True:
            self.x = random.choice([WIDTH//2 - LANE_WIDTH + 20, WIDTH//2 + 20])
            self.y = random.randint(-300, -50)
            self.radius = 15
            self.speed = 6
            # Ensure the coin does not spawn too close to any obstacle
            if not any(abs(ob.x - self.x) < SAFE_DISTANCE and abs(ob.y - self.y) < SAFE_DISTANCE for ob in obstacles):
                break

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, GOLD, (self.x, self.y), self.radius)

# Function to draw the road with white lane markings
def draw_road():
    pygame.draw.rect(screen, BLACK, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, YELLOW, (WIDTH//2 - 5, i, 10, 20))  # Center lane markings

# Function to display score
def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 150, 20))

# Game loop
player = PlayerCar()
obstacles = [Obstacle()]
coins = [Coin(obstacles)]
running = True

while running:
    screen.fill(WHITE)
    draw_road()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Update and draw obstacles
    for obstacle in obstacles[:]:
        obstacle.move()
        obstacle.draw()
        
        # Check for collision with player car
        if (player.x < obstacle.x + obstacle.width and player.x + 60 > obstacle.x and
            player.y < obstacle.y + obstacle.height and player.y + 120 > obstacle.y):
            print("Game Over!")
            running = False
    
    if obstacles[-1].y > 300:
        obstacles.append(Obstacle())
    
    if obstacles[0].y > HEIGHT:
        obstacles.pop(0)

    # Update and draw coins
    for coin in coins[:]:
        coin.move()
        coin.draw()
        
        # Check for collision with player car (more sensitive detection)
        if abs(player.x - coin.x) < 35 and abs(player.y - coin.y) < 50:
            player.score += 1
            coins.remove(coin)
    
    if coins[-1].y > 300:
        coins.append(Coin(obstacles))
    
    if coins[0].y > HEIGHT:
        coins.pop(0)
    
    player.draw()
    draw_score(player.score)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
