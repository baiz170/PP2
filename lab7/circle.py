import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


x, y = WIDTH // 2, HEIGHT // 2
radius = 25
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y + radius + speed <= HEIGHT:
                y += speed
            elif event.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x + radius + speed <= WIDTH:
                x += speed

    clock.tick(30)

pygame.quit()
