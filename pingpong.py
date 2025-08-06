import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

paddle_width, paddle_height = 10, 100
paddle_speed = 7

ball_size = 15
ball_speed_x = 5
ball_speed_y = 5
speed_increment = 0.5  # aumento na velocidade a cada batida

paddle1_y = HEIGHT // 2 - paddle_height // 2
paddle2_y = HEIGHT // 2 - paddle_height // 2
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

score1 = 0
score2 = 0

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - paddle_height:
        paddle2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y *= -1

    if (ball_x <= 20 and paddle1_y < ball_y < paddle1_y + paddle_height):
        ball_speed_x *= -1
        # aumenta a velocidade mantendo o sinal
        ball_speed_x += speed_increment if ball_speed_x > 0 else -speed_increment
        ball_speed_y += speed_increment if ball_speed_y > 0 else -speed_increment

    if (ball_x >= WIDTH - 20 - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
        ball_speed_x *= -1
        ball_speed_x += speed_increment if ball_speed_x > 0 else -speed_increment
        ball_speed_y += speed_increment if ball_speed_y > 0 else -speed_increment

    if ball_x < 0:
        score2 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = 5 * (-1 if ball_speed_x < 0 else 1)
        ball_speed_y = 5

    if ball_x > WIDTH - ball_size:
        score1 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = 5 * (-1 if ball_speed_x < 0 else 1)
        ball_speed_y = 5

    paddle1 = pygame.Rect(10, paddle1_y, paddle_width, paddle_height)
    paddle2 = pygame.Rect(WIDTH - 20, paddle2_y, paddle_width, paddle_height)
    ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

