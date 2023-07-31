import pygame


class Sword_fx(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allsprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        
        self.image = pygame.image.load("Sprites/Personnages/Cac/sword_fx.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

        self.anim_time = 5

    def update(self):
        if self.anim_time > 0:
            self.anim_time -= 1
        else:
            self.kill()