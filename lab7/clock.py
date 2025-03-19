import pygame
import math
import time

pygame.init()

clock_img = pygame.image.load("/Users/madikbaizakov/Documents/vscode/PP2/lab7/clock.png")
minute_hand = pygame.image.load("/Users/madikbaizakov/Documents/vscode/PP2/lab7/rightarm.png")
second_hand = pygame.image.load("/Users/madikbaizakov/Documents/vscode/PP2/lab7/leftarm.png")

screen_size = (800, 800)

clock_img = pygame.transform.scale(clock_img, screen_size)


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mickey Clock")

clock_center = (400, 400)
minute_pivot = (400, 320)
second_pivot = (400, 320)

def rotate_and_blit(image, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=(pivot[0] + offset[0], pivot[1] + offset[1]))
    screen.blit(rotated_image, rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))

    t = time.localtime()
    minutes_angle = (t.tm_min % 60) * 6
    seconds_angle = (t.tm_sec % 60) * 6

    rotate_and_blit(minute_hand, minutes_angle, minute_pivot, (0, 50))
    rotate_and_blit(second_hand, seconds_angle, second_pivot, (0, 50))

    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()