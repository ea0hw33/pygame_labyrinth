import pygame


class Level:
    level = []

    def __init__(self, level,resolution):
        self.resolution = resolution
        self.level = level
        self.surface = self.level_surface(self.level)

    def level_surface(self, level):
        surface = []
        for i in range(len(level)):
            level_surface = []
            for j in range(len(level)):
                if level[i][j] == '*':
                    rectangle = pygame.Rect(j * self.resolution, i * self.resolution,
                                            self.resolution, self.resolution)
                    # pygame.draw.rect(screen, (200, 200, 200), rectangle)
                    level_surface.append(rectangle)
            surface.append(level_surface)
        return surface

    def get_collision(self,players):
        collided = False
        for i in self.surface:
            for j in i:
                if players.colliderect(j):
                    collided = True
        return collided

    def level_action(self, player):
        if not len(self.surface)*self.resolution > player.x > 0 or \
                not len(self.surface)*self.resolution > player.y > 0:
            return True
        return False

    def find_coordinates(self, char):
        for i in range(len(self.level)):
            if self.level[i].find(char) != -1:
                return self.level[i].find(char) * self.resolution, i * self.resolution

if __name__=='__main__':
    level1 = ['********',
              '**     *',
              '*      *',
              '*  ** 0*',
              '**  ****',
              '*  **  *',
              '*       ',
              '********']
    level = Level(level1,50)
    print(level.surface)