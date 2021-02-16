import pygame
from constants import SIZE, FPS

if __name__ == '__main__':
    def draw():
        screen.fill("black")

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Adventure")
    running = True
    clock = pygame.time.Clock()
    clock.tick(FPS)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        pygame.display.flip()
    pygame.quit()
