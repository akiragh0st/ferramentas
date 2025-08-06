import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Avião")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Avião
plane_width, plane_height = 50, 40
plane_x = WIDTH // 2 - plane_width // 2
plane_y = HEIGHT - plane_height - 10
plane_speed = 7

# Tiros
bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullets = []

# Inimigos
enemy_width, enemy_height = 50, 40
enemy_speed = 3
enemies = []
spawn_interval = 1500  # ms
last_spawn_time = 0

score = 0

running = True

while running:
    current_time = pygame.time.get_ticks()
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane_x > 0:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT] and plane_x < WIDTH - plane_width:
        plane_x += plane_speed
    if keys[pygame.K_SPACE]:
        # Limita a quantidade de tiros na tela para não travar
        if len(bullets) < 5:
            bullets.append([plane_x + plane_width // 2 - bullet_width // 2, plane_y])

    # Atualiza tiros
    bullets = [[b[0], b[1] - bullet_speed] for b in bullets if b[1] > 0]

    # Spawn inimigos
    if current_time - last_spawn_time > spawn_interval:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemies.append([enemy_x, -enemy_height])
        last_spawn_time = current_time

    # Atualiza inimigos
    enemies = [[e[0], e[1] + enemy_speed] for e in enemies if e[1] < HEIGHT]

    # Checa colisões tiros x inimigos
    for b in bullets[:]:
        bullet_rect = pygame.Rect(b[0], b[1], bullet_width, bullet_height)
        for e in enemies[:]:
            enemy_rect = pygame.Rect(e[0], e[1], enemy_width, enemy_height)
            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(b)
                enemies.remove(e)
                score += 1
                break

    # Checa colisão inimigos x avião
    plane_rect = pygame.Rect(plane_x, plane_y, plane_width, plane_height)
    for e in enemies:
        enemy_rect = pygame.Rect(e[0], e[1], enemy_width, enemy_height)
        if plane_rect.colliderect(enemy_rect):
            running = False  # Fim de jogo

    # Desenha avião
    pygame.draw.rect(screen, BLUE, plane_rect)

    # Desenha tiros
    for b in bullets:
        pygame.draw.rect(screen, WHITE, pygame.Rect(b[0], b[1], bullet_width, bullet_height))

    # Desenha inimigos
    for e in enemies:
        pygame.draw.rect(screen, RED, pygame.Rect(e[0], e[1], enemy_width, enemy_height))

    # Desenha score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
