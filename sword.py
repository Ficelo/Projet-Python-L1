import pygame
from sword_fx import *


class Sword(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, player):
        self.groups = game.allsprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load("./Sprites/Personnages/Cac/amogus_sword.png")
        self.image_up = pygame.image.load("./Sprites/Personnages/Cac/amogus_sword.png")
        self.image_down = pygame.image.load("./Sprites/Personnages/Cac/amogus_sword2.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.player = player
        self.game = game

        self.hit_duration = 15
        self.cooldown = 15
        self.actual_coolsown = self.cooldown

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

        if click == (1, 0, 0):

            if self.actual_coolsown != self.cooldown:
                self.actual_coolsown += 1
            else:  
                for i in range(0, self.hit_duration):
                    
                    fx = Sword_fx(self.game, self.rect.x, self.rect.y)

                    hit = pygame.sprite.spritecollide(self, self.game.ennemis, False)
                    if hit:
                        for sprite in hit:
                            sprite.kill()
                            self.game.ennemis_in_room[self.game.current_room] -= 1
                self.actual_coolsown = 0
        


        self.rect.x = self.x
        self.rect.y = self.y