import pygame


class Ennemi_spike2(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.groups = game.allsprites, game.ennemis
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load("./Sprites/Ennemis/Mechant1.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.pt1 = x - 64
        self.pt2 = x + 64

        self.game = game

        self.speed = 2

        self.state = "right"

        self.room = 0

        for i in range (0, len(self.game.all_floor_rooms)):
            if self.x >= self.game.all_floor_rooms[str(i)][0] and self.x <= self.game.all_floor_rooms[str(i)][2]:
                if self.y >= self.game.all_floor_rooms[str(i)][1] and self.y <= self.game.all_floor_rooms[str(i)][3]:
                    self.room = int(i)
                    self.game.ennemis_in_room[self.room] += 1

    def update(self):
        if self.state == "right":
            if self.x > self.pt1:
                self.x -= self.speed
            else:
                self.state = "left"
        if self.state == "left":
            if self.x < self.pt2:
                self.x += self.speed
            else:
                self.state = "right"

        self.rect.x = self.x
        self.rect.y = self.y