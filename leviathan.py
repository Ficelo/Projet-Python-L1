import pygame


#Le boss de la zone et donc sa classe
class Leviathan (pygame.sprite.Sprite):
    def __init__(self,game,x,y,player):
        self.groups = game.allsprites, game.ennemis, game.targeted_ennemis
        pygame.sprite.Sprite.__init__(self,self.groups)
         #Ici je veut un monstre un peu plus original et je respecte les multiples de 32 afin que rien ne crash
        image = pygame.image.load("./Sprites/Ennemis/Leviathanbg.png")
        self.image = image
        self.rect =self.image.get_rect()
        self.x = x
        self.y = y 
        self.rect.x = x
        self.rect.y = y

        self.speed = 2
    
        self.target = None
       
        self.game = game
        
        self.Angery_time = 60

        self.room = 0


        for i in range (0, len(self.game.all_floor_rooms)):
            if self.x >= self.game.all_floor_rooms[str(i)][0] and self.x <= self.game.all_floor_rooms[str(i)][2]:
                if self.y >= self.game.all_floor_rooms[str(i)][1] and self.y <= self.game.all_floor_rooms[str(i)][3]:
                    self.room = int(i)
                    self.game.ennemis_in_room[self.room] += 1

    def update (self):
        if self.target != None:
            if  self.Angery_time <= 0 and self.game.current_room == self.room:
                    
                if self.target.rect.center[0] > self.rect.center[0]:
                    self.rect.x += self.speed
                if self.target.rect.center[0] < self.rect.center[0]:
                    self.rect.x -= self.speed

                if self.target.rect.center[1] > self.rect.center[1]:
                    self.rect.y += self.speed
                if self.target.rect.center[1] < self.rect.center[1]:
                    self.rect.y -= self.speed
            else:
                self.Angery_time -= 1
    
            hit = pygame.sprite.spritecollide(self, self.game.players, False)

            


            