import pygame

from level import Level


class Player:
    def __init__(self, level: Level, speed: int, color = (0,0,200)):
        self.player = pygame.Rect(*level.find_coordinates('0'),
                                  level.resolution//2,level.resolution//2)
        self.speed = speed
        self.color = color

    def player_movement(self,key_pressed, level):
        fplayers = self.player.copy()
        if key_pressed[pygame.K_a]:
            fplayers.x -= self.speed
            if not level.get_collision(self.player) and not level.get_collision(fplayers):
                self.player.x -= self.speed
        if key_pressed[pygame.K_d]:
            fplayers.x += self.speed
            if not level.get_collision(self.player) and not level.get_collision(fplayers):
                self.player.x += self.speed
        if key_pressed[pygame.K_w]:
            fplayers.y -= self.speed
            if not level.get_collision(self.player) and not level.get_collision(fplayers):
                self.player.y -= self.speed
        if key_pressed[pygame.K_s]:
            fplayers.y += self.speed
            if not level.get_collision(self.player) and not level.get_collision(fplayers):
                self.player.y += self.speed