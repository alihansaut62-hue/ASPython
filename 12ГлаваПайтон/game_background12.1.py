import sys
import pygame

class background:
    # класс для уравлениеми ресурсами и поведением игры 
    def __init__(self):
        pygame.init()
        self.bg_color = (48, 0, 80)

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invason")

    def ran_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit

            self.screen.fill(self.bg_color)   

            pygame.display.flip()

if __name__ == '__main__':
    ai = background()
    ai.ran_game()
