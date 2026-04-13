# Simple Pong game using Pygame
import pygame

print(pygame.version.ver)

def main():
    # Initialize Pygame and set up the game window
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    running = True
    paddle_y = 250
    paddle2_y = 250
    ball_x = 400
    ball_y = 300
    ball_dx = 4
    ball_dy = 4
    score1 = 0
    score2 = 0
    #while loop for game state

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)
        screen.fill((0, 0, 0))
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle_y -= 5
        if keys[pygame.K_DOWN]:
            paddle_y += 5
        if keys[pygame.K_w]:
            paddle2_y -= 5
        if keys[pygame.K_s]:
            paddle2_y += 5
        
        ball_x += ball_dx
        ball_y += ball_dy

        if ball_y - 8 <= 0 or ball_y + 8 >= 600:
            ball_dy = -ball_dy

        if ball_x - 8 <= 60 and paddle_y < ball_y < paddle_y + 100:
            ball_dx = -ball_dx
            ball_x = 68

        if ball_x + 8 >= 740 and paddle2_y < ball_y < paddle2_y + 100:
            ball_dx = -ball_dx
            ball_x = 732

        if ball_x < 0:
            score2 += 1
            ball_x, ball_y = 400, 300

        if ball_x > 800:
            score1 += 1
            ball_x, ball_y = 400, 300

        pygame.draw.rect(screen, (255, 255, 255), (50, paddle_y, 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (740, paddle2_y, 10, 100))
        pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 8)
        pygame.display.flip()
    
    pygame.quit()

main()

