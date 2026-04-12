import pygame

print(pygame.version.ver)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    running = True
    paddle_y = 250
    
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
        pygame.draw.rect(screen, (255, 255, 255), (50, paddle_y, 10, 100))
        pygame.display.flip()
    
    pygame.quit()

main()