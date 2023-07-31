import pygame
from sword import *
from ak import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, data):
        self.groups = game.allsprites, game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.image = pygame.image.load(data["Images"]["Idle"])
        self.rect = self.image.get_rect()

        self.x = x * 32
        self.y = y * 32
        self.move_x = 0
        self.move_y = 0
        self.speed = data["Stats"]["speed"]

        self.width = width
        self.height = height
        self.game = game

        self.data = data
        self.game.data = data

        if self.data["Type"] == "ranged":
            self.ak = AK(self.game, self.x, self.y, 32, 32, self)
        
        if self.data["Type"] == "cac":
            self.sword = Sword(self.game, self.x, self.y, 32, 32, self)

        self.sens = "droite"
        self.retourne = False
    
    def get_keys(self):
        self.move_x = 0
        self.move_y = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_z]:
            self.move_y -= self.speed
        if key[pygame.K_s]:
            self.move_y += self.speed
        if key[pygame.K_q]:
            self.move_x -= self.speed
            self.sens = "gauche"
        if key[pygame.K_d]:
            self.move_x += self.speed
            self.sens = "droite"

        if self.move_x != 0 and self.move_y != 0:
            self.move_y *= 0.7
            self.move_x *= 0.7

    def collide_with_walls(self, direction):
        if direction == 'x':
            hit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hit:
                if self.move_x > 0:
                    self.x = hit[0].rect.left - self.rect.width
                if self.move_x < 0:
                    self.x = hit[0].rect.right
                
                self.move_x = 0
                self.rect.x = self.x
                if not self.game.game_won:
                    self.game.current_health -= 1
        if direction == 'y':
            hit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hit:
                if self.move_y > 0:
                    self.y = hit[0].rect.top - self.height
                if self.move_y < 0:
                    self.y = hit[0].rect.bottom

                self.move_y = 0
                self.rect.y = self.y
                if not self.game.game_won:
                    self.game.current_health -= 1

    def animate(self):

        if self.sens == "gauche" and self.retourne == False:
            self.image = pygame.transform.flip(self.image, True, False)
            self.retourne = True
        if self.sens == "droite" and self.retourne == True:
            self.image = pygame.transform.flip(self.image, True, False)
            self.retourne = False
        
    def collide_ennemis(self):
        hit = pygame.sprite.spritecollide(self, self.game.ennemis, False)

        if hit:
                if self.game.inv_time > 0:
                    self.game.inv_time -= 1
                else:
                    self.game.current_health -= 1
                    self.game.inv_time = self.game.max_inv_time

    def update(self):
        self.get_keys()
        self.x += self.move_x
        self.y += self.move_y
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        self.animate()
        if not self.game.game_won:
            self.collide_ennemis()
        

        for i in range (0, len(self.game.all_floor_rooms)):
                if self.x >= self.game.all_floor_rooms[str(i)][0] and self.x <= self.game.all_floor_rooms[str(i)][2]:
                    if self.y >= self.game.all_floor_rooms[str(i)][1] and self.y <= self.game.all_floor_rooms[str(i)][3]:
                        self.game.current_room = int(i)
