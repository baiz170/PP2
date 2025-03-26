import pygame

# Initialize Pygame
pygame.init()

# Screen parameters
WIDTH, HEIGHT = 1000, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [BLACK, RED, GREEN, BLUE]  # List of available colors

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")
clock = pygame.time.Clock()

# State variables
drawing = False  # Drawing flag
color = BLACK  # Current color
mode = "pen"  # Current drawing mode
start_pos = None  # Start position
pen_size = 5  # Pen thickness

# Create drawing canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Tool buttons
buttons = {
    "Pen": pygame.Rect(10, 10, 80, 30),
    "Eraser": pygame.Rect(100, 10, 80, 30),
    "Rect": pygame.Rect(190, 10, 80, 30),
    "Circle": pygame.Rect(280, 10, 80, 30),
    "Square": pygame.Rect(370, 10, 80, 30),
    "Right Triangle": pygame.Rect(460, 10, 130, 30),
    "Equilateral Triangle": pygame.Rect(600, 10, 150, 30),
    "Rhombus": pygame.Rect(760, 10, 100, 30),
    "Clear": pygame.Rect(870, 10, 80, 30)
}

# Main loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen
    screen.blit(canvas, (0, 0))  # Display the drawing canvas

    # Draw buttons
    for name, rect in buttons.items():
        pygame.draw.rect(screen, BLACK, rect, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(name, True, BLACK)
        screen.blit(text, (rect.x + 5, rect.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if a button was clicked
                for name, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        mode = name.lower().replace(" ", "_")  # Convert button name to mode
                        if mode == "clear":
                            canvas.fill(WHITE)

                drawing = True
                start_pos = event.pos

            elif event.button == 3:  # Right mouse button
                color = COLORS[(COLORS.index(color) + 1) % len(COLORS)]  # Change color
                pen_size = 5 if pen_size == 10 else 10  # Toggle pen thickness
        
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # Draw selected shape
            if mode == "rect":
                pygame.draw.rect(canvas, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 // 2
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(canvas, color, center, int(radius), 2)
            elif mode == "square":
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))  # Square side length
                pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], side, side), 2)
            elif mode == "right_triangle":
                pygame.draw.polygon(canvas, color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == "equilateral_triangle":
                side = abs(end_pos[0] - start_pos[0])
                height = (3 ** 0.5 / 2) * side  # Calculate height
                top_vertex = (start_pos[0] + side // 2, start_pos[1] - int(height))
                pygame.draw.polygon(canvas, color, [start_pos, (start_pos[0] + side, start_pos[1]), top_vertex], 2)
            elif mode == "rhombus":
                mid_x = (start_pos[0] + end_pos[0]) // 2
                mid_y = (start_pos[1] + end_pos[1]) // 2
                width = abs(end_pos[0] - start_pos[0]) // 2
                height = abs(end_pos[1] - start_pos[1]) // 2
                pygame.draw.polygon(canvas, color, [
                    (mid_x, start_pos[1]),  # Top
                    (end_pos[0], mid_y),  # Right
                    (mid_x, end_pos[1]),  # Bottom
                    (start_pos[0], mid_y)  # Left
                ], 2)
    
    # Continuous drawing for pen and eraser
    if drawing and mode == "pen":
        pygame.draw.circle(canvas, color, pygame.mouse.get_pos(), pen_size)
    elif drawing and mode == "eraser":
        pygame.draw.circle(canvas, WHITE, pygame.mouse.get_pos(), pen_size + 5)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
