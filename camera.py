import pygame


class Camera:
    def __init__(self, game, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.game = game
        self.X = 0
        self.Y = 0
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x =  - target.rect.x + int(960/2)
        y = - target.rect.y + int(540/2)
        
        self.X = x
        self.Y = y
        
        self.camera = pygame.Rect(x, y, self.width, self.height)