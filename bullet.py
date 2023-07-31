import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, target, ak):
        self.groups = game.allsprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y

        self.image = pygame.image.load("./Sprites/Personnages/Ranged/bullet.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        

        self.game = game
        self.target = (target[0] - self.game.camera.X, target[1] - self.game.camera.Y)

        self.distance_x = self.target[0] - ak.rect.x
        self.distance_y = self.target[1] - ak.rect.y

        self.alive_time = 180


    def update(self):
        hit_wall = pygame.sprite.spritecollide(self, self.game.walls, False)
        if hit_wall:
            self.kill()

        if self.alive_time > 0:
            self.rect.center = (self.rect.center[0] + self.distance_x * 0.1, self.rect.center[1] + self.distance_y * 0.1)
            self.alive_time -= 1

        else:
            self.kill()

        hit_ennemis = pygame.sprite.spritecollide(self, self.game.ennemis, False)

        if hit_ennemis:
            
            for enn in hit_ennemis:
                if self.game.current_room == enn.room:
                    enn.kill()
                    self.game.ennemis_in_room[self.game.current_room] -= 1
                    self.kill()