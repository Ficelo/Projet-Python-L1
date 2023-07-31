import pygame


class Doors(pygame.sprite.Sprite):
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

        self.game= game

        self.room = 0

        for i in range (0, len(self.game.all_floor_rooms)):
            if self.x >= self.game.all_floor_rooms[str(i)][0] and self.x <= self.game.all_floor_rooms[str(i)][2]:
                if self.y >= self.game.all_floor_rooms[str(i)][1] and self.y <= self.game.all_floor_rooms[str(i)][3]:
                    self.room = int(i)

    def update(self):
        if self.game.ennemis_in_room[self.room] == 0:
            self.kill()