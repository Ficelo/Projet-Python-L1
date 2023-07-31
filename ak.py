import pygame
from bullet import *

class AK(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, player):
        self.groups = game.allsprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.player = player

        self.image = pygame.image.load("./Sprites/Personnages/Ranged/AK.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.game = game

        self.cooldown = 15
        self.actual_cooldown = self.cooldown

        self.en_animation = False
        self.retourne = False



    def update(self):
        
        click = pygame.mouse.get_pressed()


        if self.player.sens == "droite":
            self.x = self.player.rect.topright[0]
            self.y = self.player.rect.topright[1]
            if self.retourne:
                self.image = pygame.transform.flip(self.image, True, False)
            self.retourne = False
            

        if self.player.sens == "gauche":
            self.x = self.player.rect.topleft[0] - self.width
            self.y = self.player.rect.topleft[1]
            if not self.retourne:
                self.retourne = True
                self.image = pygame.transform.flip(self.image, True, False)

        self.rect.x = self.x
        self.rect.y = self.y

        if click == (1, 0, 0):
            if self.actual_cooldown >= 0:
                self.actual_cooldown -= 1
            else:
                pos = pygame.mouse.get_pos()
                if self.player.sens == 'gauche':
                    bul = Bullet(self.game, self.rect.topleft[0], self.rect.topleft[1], pos, self)
                if self.player.sens == "droite":
                    bul = Bullet(self.game, self.rect.topright[0], self.rect.topright[1], pos, self)
                self.actual_cooldown = self.cooldown
                
        