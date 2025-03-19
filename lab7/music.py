import pygame
import sys

pygame.init()
pygame.mixer.init()

playlist = [
    "/Users/madikbaizakov/Documents/vscode/PP2/lab7/song1.mp3", 
    "/Users/madikbaizakov/Documents/vscode/PP2/lab7/song2.mp3", 
    "/Users/madikbaizakov/Documents/vscode/PP2/lab7/song3.mp3"
]



current_song = 0
playing = False

def play_music():
    global playing
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()
    playing = True

def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((20, 20, 30))
    
    pygame.draw.polygon(screen, (100, 255, 100), [(250, 380), (250, 420), (200, 400)])
    pygame.draw.rect(screen, (100, 255, 100), (240, 390, 20, 20))
    
    pygame.draw.polygon(screen, (100, 100, 255), [(550, 380), (550, 420), (600, 400)])
    pygame.draw.rect(screen, (100, 100, 255), (560, 390, 20, 20))
    
    if playing:
        pygame.draw.rect(screen, (255, 50, 50), (380, 370, 15, 60))
        pygame.draw.rect(screen, (255, 50, 50), (405, 370, 15, 60))
    else:
        pygame.draw.polygon(screen, (255, 50, 50), [(380, 370), (380, 430), (420, 400)])
    
    play_text = font.render("Play (P)", True, (255, 255, 255))
    stop_text = font.render("Stop (S)", True, (255, 255, 255))
    next_text = font.render("Next (N)", True, (255, 255, 255))
    prev_text = font.render("Prev (B)", True, (255, 255, 255))
    
    screen.blit(play_text, (350, 500))
    screen.blit(stop_text, (350, 550))
    screen.blit(next_text, (500, 400))
    screen.blit(prev_text, (150, 400))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(playlist)
                play_music()

pygame.quit()
sys.exit()
