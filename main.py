# Simple Pong game using Pygame
import pygame

print(pygame.version.ver)

def main():
    # Initialize Pygame and set up the game window
    pygame.init()
    font = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 36)
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

        if paddle_y < 0:
            paddle_y = 0
        if paddle_y > 500:
            paddle_y = 500

        if paddle2_y < 0:
            paddle2_y = 0
        if paddle2_y > 500:
            paddle2_y = 500
 
        if score1 < 7 and score2 < 7:
    # all movement, input, collision code here
            
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
        
        text1 = font.render(str(score1), True, (255, 255, 255))
        text2 = font.render(str(score2), True, (255, 255, 255))
        screen.blit(text1, (200, 20))
        screen.blit(text2, (550, 20))

        if score1 >= 7 or score2 >= 7:
            winner_text = "Player 1 Wins!" if score1 > score2 else "Player 2 Wins!"
            prompt_text = "Press R to restart or Q to quit"
            winner_surface = font.render(winner_text, True, (255, 255, 255))
            prompt_surface = font_small.render(prompt_text, True, (255, 255, 255))
            prompt_x = (800 - prompt_surface.get_width()) // 2
            screen.blit(winner_surface, (250, 230))
            screen.blit(prompt_surface, (prompt_x, 320))
            if keys[pygame.K_r]:
                score1 = 0
                score2 = 0
                ball_x, ball_y = 400, 300
                paddle_y = 250
                paddle2_y = 250
               #game_state = "playing"
            if keys[pygame.K_q]:
                running = False
  

        pygame.draw.rect(screen, (255, 255, 255), (50, paddle_y, 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (740, paddle2_y, 10, 100))
        pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 8)
        pygame.display.flip()
    
    pygame.quit()

main()

