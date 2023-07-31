import pygame

class Tresor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.groups = game.allsprites, game.tresors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load("./Sprites/Divers/coffre.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

        self.width = width
        self.height = height

        self.game = game

    def update(self):
        hit = pygame.sprite.spritecollide(self, self.game.players, False)

        if hit:
            self.game.game_won = True