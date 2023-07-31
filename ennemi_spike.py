import pygame


class Ennemi_spike(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.groups = game.allsprites, game.ennemis
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load("./Sprites/Ennemis/Mechant1.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.pt1 = y - 64
        self.pt2 = y + 64

        self.game = game

        self.speed = 2

        self.state = "up"

        self.room = 0

        for i in range (0, len(self.game.all_floor_rooms)):
            if self.x >= self.game.all_floor_rooms[str(i)][0] and self.x <= self.game.all_floor_rooms[str(i)][2]:
                if self.y >= self.game.all_floor_rooms[str(i)][1] and self.y <= self.game.all_floor_rooms[str(i)][3]:
                    self.room = int(i)
                    self.game.ennemis_in_room[self.room] += 1

    def update(self):
        if self.state == "up":
            if self.y > self.pt1:
                self.y -= self.speed
            else:
                self.state = "down"
        if self.state == "down":
            if self.y < self.pt2:
                self.y += self.speed
            else:
                self.state = "up"

        self.rect.x = self.x
        self.rect.y = self.y