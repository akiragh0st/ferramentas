import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini CS:GO com Pygame - Inimigos Atiram")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Jogador
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
player_speed = 5
player_size = 20
player_health = 5

# Inimigos
enemy_size = 20
enemy_speed = 2
enemy_fire_rate = 90  # frames entre tiros
enemies = []

# Balas do jogador
player_bullets = []
bullet_speed = 10
bullet_size = 5

# Balas inimigas
enemy_bullets = []
enemy_bullet_speed = 7
enemy_bullet_size = 5

# Pontuação
score = 0

# Fonte para texto
font = pygame.font.SysFont(None, 36)

# Funções
def draw_player(pos):
    pygame.draw.circle(screen, GREEN, (int(pos.x), int(pos.y)), player_size)

def draw_enemy(pos):
    pygame.draw.rect(screen, RED, (pos.x - enemy_size//2, pos.y - enemy_size//2, enemy_size, enemy_size))

def draw_crosshair(pos):
    x, y = pos
    pygame.draw.line(screen, BLACK, (x - 15, y), (x + 15, y), 2)
    pygame.draw.line(screen, BLACK, (x, y - 15), (x, y + 15), 2)

def draw_bullet(pos, color):
    pygame.draw.circle(screen, color, (int(pos.x), int(pos.y)), bullet_size)

def check_collision_rect(pos1, size1, pos2, size2):
    rect1 = pygame.Rect(pos1.x - size1//2, pos1.y - size1//2, size1, size1)
    rect2 = pygame.Rect(pos2.x - size2//2, pos2.y - size2//2, size2, size2)
    return rect1.colliderect(rect2)

def spawn_enemy():
    # Spawn inimigo em bordas aleatórias da tela
    side = random.choice(['top', 'bottom', 'left', 'right'])
    if side == 'top':
        return {'pos': pygame.Vector2(random.randint(50, WIDTH-50), 30), 'fire_cooldown': enemy_fire_rate}
    elif side == 'bottom':
        return {'pos': pygame.Vector2(random.randint(50, WIDTH-50), HEIGHT - 30), 'fire_cooldown': enemy_fire_rate}
    elif side == 'left':
        return {'pos': pygame.Vector2(30, random.randint(50, HEIGHT-50)), 'fire_cooldown': enemy_fire_rate}
    else:  # right
        return {'pos': pygame.Vector2(WIDTH - 30, random.randint(50, HEIGHT-50)), 'fire_cooldown': enemy_fire_rate}

# Criar inimigos iniciais
for _ in range(5):
    enemies.append(spawn_enemy())

# Loop principal
running = True
while running:
    screen.fill(WHITE)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Atirar bala jogador
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            direction = (mouse_pos - player_pos).normalize()
            bullet_pos = player_pos + direction * (player_size + bullet_size)
            player_bullets.append({'pos': bullet_pos, 'dir': direction})
    
    # Movimento do jogador (WASD)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed
    if keys[pygame.K_s]:
        player_pos.y += player_speed
    if keys[pygame.K_a]:
        player_pos.x -= player_speed
    if keys[pygame.K_d]:
        player_pos.x += player_speed
    
    # Manter jogador dentro da tela
    player_pos.x = max(player_size, min(WIDTH - player_size, player_pos.x))
    player_pos.y = max(player_size, min(HEIGHT - player_size, player_pos.y))
    
    # Atualizar balas do jogador
    for bullet in player_bullets[:]:
        bullet['pos'] += bullet['dir'] * bullet_speed
        if bullet['pos'].x < 0 or bullet['pos'].x > WIDTH or bullet['pos'].y < 0 or bullet['pos'].y > HEIGHT:
            player_bullets.remove(bullet)
    
    # Atualizar balas inimigas
    for bullet in enemy_bullets[:]:
        bullet['pos'] += bullet['dir'] * enemy_bullet_speed
        if bullet['pos'].x < 0 or bullet['pos'].x > WIDTH or bullet['pos'].y < 0 or bullet['pos'].y > HEIGHT:
            enemy_bullets.remove(bullet)
    
    # Atualizar inimigos
    for enemy in enemies[:]:
        # Movimentar inimigo em direção ao jogador
        direction = (player_pos - enemy['pos']).normalize()
        enemy['pos'] += direction * enemy_speed
        
        # Atirar se cooldown zerado
        enemy['fire_cooldown'] -= 1
        if enemy['fire_cooldown'] <= 0:
            bullet_dir = (player_pos - enemy['pos']).normalize()
            bullet_pos = enemy['pos'] + bullet_dir * (enemy_size + enemy_bullet_size)
            enemy_bullets.append({'pos': bullet_pos, 'dir': bullet_dir})
            enemy['fire_cooldown'] = enemy_fire_rate
        
        # Checar colisão com balas do jogador
        for bullet in player_bullets:
            if check_collision_rect(enemy['pos'], enemy_size, bullet['pos'], bullet_size):
                try:
                    player_bullets.remove(bullet)
                except:
                    pass
                enemies.remove(enemy)
                score += 1
                enemies.append(spawn_enemy())
                break
    
    # Checar colisão do jogador com balas inimigas
    for bullet in enemy_bullets[:]:
        if check_collision_rect(player_pos, player_size, bullet['pos'], enemy_bullet_size):
            enemy_bullets.remove(bullet)
            player_health -= 1
            if player_health <= 0:
                running = False  # Fim do jogo
    
    # Desenhar jogador
    draw_player(player_pos)
    
    # Desenhar inimigos
    for enemy in enemies:
        draw_enemy(enemy['pos'])
    
    # Desenhar balas jogador
    for bullet in player_bullets:
        draw_bullet(bullet['pos'], BLUE)
    
    # Desenhar balas inimigas
    for bullet in enemy_bullets:
        draw_bullet(bullet['pos'], RED)
    
    # Desenhar mira
    draw_crosshair(pygame.mouse.get_pos())
    
    # Mostrar pontuação e vida
    score_text = font.render(f"Pontuação: {score}", True, BLACK)
    health_text = font.render(f"Vida: {player_health}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))
    
    pygame.display.flip()
    clock.tick(60)

# Tela de game over
screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, RED)
final_score_text = font.render(f"Pontuação final: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2))
pygame.display.flip()

# Esperar alguns segundos antes de fechar
pygame.time.wait(3000)
pygame.quit()
sys.exit()

