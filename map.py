import pygame


# Карта
_ = False
mini_map = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, _, _, _, _, _, _, _, _, _, _, 6],
    [6, _, _, _, _, _, 2, _, _, _, _, 6],
    [6, _, _, _, 5, 4, 3, _, _, _, _, 6],
    [6, _, _, _, _, _, _, _, _, _, _, 6],
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    # Метод класс который создает карту  
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    # Метод класса который отрисововает карту
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (pos[0]*100, pos[1] * 100, 100, 100), 2) for pos  in self.world_map]

