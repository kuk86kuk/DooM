import pygame
import math
import settings


class RayCating:
    def __init__(self, game):
        self.game = game
    
    def ray_cast(self):
        ox, oy = self.game.player_.pos
        x_map, y_map = self.game.player_.map_pos
        
        


        rau_angle = self.game.player_.angle - settings.HALF_FOV + 0.0001 # число использется для избежания деления на ноль 
        for rau in range(settings.NUM_RAYS):
            sin_a = math.sin(rau_angle)
            cos_a = math.cos(rau_angle)
            
            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy /sin_a
            dx = delta_depth * cos_a

            for i in range(settings.MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map_.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(settings.MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map_.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
            rau_angle += settings.DELTA_ANGLE

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor  

            pygame.draw.line(self.game.screen, 'green', (100 * ox, 100 * oy),
                            (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)


    def update(self):
        self.ray_cast() 