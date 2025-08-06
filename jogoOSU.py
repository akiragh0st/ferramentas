import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Osu! Pygame")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

circle_radius = 30
circle_lifetime = 2000
spawn_interval = 1500

score = 0

class Circle:
    def __init__(self):
        self.x = random.randint(circle_radius, WIDTH - circle_radius)
        self.y = random.randint(circle_radius, HEIGHT - circle_radius)
        self.spawn_time = pygame.time.get_ticks()
        self.clicked = False
    
    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), circle_radius, 5)
    
    def is_expired(self, current_time):
        return current_time - self.spawn_time > circle_lifetime

    def is_clicked(self, pos):
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx*dx + dy*dy <= circle_radius * circle_radius

circles = []
last_spawn_time = 0

running = True
clock = pygame.time.Clock()

while running:
    current_time = pygame.time.get_ticks()
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for circle in circles:
                if not circle.clicked and circle.is_clicked(pos):
                    circle.clicked = True
                    score += 1

    if current_time - last_spawn_time > spawn_interval:
        circles.append(Circle())
        last_spawn_time = current_time

    circles = [c for c in circles if not c.is_expired(current_time) and not c.clicked]

    for circle in circles:
        circle.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
