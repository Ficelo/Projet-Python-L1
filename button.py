import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, image, function, funct_params = []):
        self.groups = game.allsprites, game.menus
        pygame.sprite.Sprite.__init__(self, self.groups)

        #image = pygame.Surface((32, 32))
        #image.fill(color)
        self.image = image
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.function = function
        self.game = game
        self.funct_params = funct_params

    def update(self):
        
        self.rect.x = self.x
        self.rect.y = self.y

        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        
        if pos[0] >= self.x and pos[0] <= self.x + self.width:
            if pos[1] >= self.y and pos[1] <= self.x + self.height:
                if click == (1, 0, 0):
                    self.function(*self.funct_params)