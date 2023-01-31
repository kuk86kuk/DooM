import pygame
import sys
import settings
import map
import player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    # Метод класса который созадет карту
    def new_game(self):
        self.map_ = map.Map(self)
        self.player_ = player.Player(self)


    # Метод класса который обновлает 
    def update(self):
        self.player_.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(settings.FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')


    # Метод класса который отрисовавет экран
    def draw(self):
        self.screen.fill('black')
        self.map_.draw()
        self.player_.draw()


    # Метод класса который отслеживает события
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    # Метод класса который запускает игру
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()