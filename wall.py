import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, color):
        self.groups = game.allsprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        image = pygame.Surface((width, height))
        image.fill(color)
        self.image = image

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = width
        self.height = height