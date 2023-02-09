import pygame

import levels
from creatures import Player
from level import Level
from settings import Settings


def draw_frame(screen, level, creatures, clock):

    for i in level.surface:
        for j in i:
            pygame.draw.rect(screen, (200, 200, 200), j)

    for creature in creatures:
        pygame.draw.rect(screen, creature.color, creature.player)

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(str(clock.get_fps())[:4], True, (0, 0, 255))
    screen.blit(text, text.get_rect())

    pygame.display.update()



def main():
    WIDTH = 400
    HEIGHT = 400
    FPS = 60
    level_actions = 0
    SPEED = 5
    settings = Settings(width=WIDTH,height=HEIGHT,fps=FPS,speed=SPEED)
    settings.resolution_setter(levels.level[level_actions])
    level = Level(levels.level[level_actions],settings.resolution)
    creatures = []
    creatures.append(Player(level,settings.speed))
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
    pygame.display.set_caption("project")
    clock = pygame.time.Clock()
    while 1:
        clock.tick(settings.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        key_pressed = pygame.key.get_pressed()
        for creature in creatures:
            creature.player_movement(key_pressed,level)
            if level.level_action(creature.player):
                level_actions += 1
                level_actions = level_actions % 2 #!!
                creatures.clear()
                settings.resolution_setter(levels.level[level_actions])
                level = Level(levels.level[level_actions],settings.resolution)
                creatures.append(Player(level,settings.speed))
                break
        screen.fill((0,0,0))
        draw_frame(screen,level,creatures,clock)

main()