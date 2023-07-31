import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, game, x, y, map, player, data, isRespawn):
        self.groups = game.allsprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        image = pygame.Surface((32, 32))
        image.fill((255, 255, 0))
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

        self.game = game
        self.map = map
        self.player = player
        self.data = data
        self.isRespawn = isRespawn

    def update(self):
        hit = pygame.sprite.spritecollide(self, self.game.players, False)

        if hit:
            for sprite in self.game.allsprites:
                sprite.kill()
            if self.isRespawn:
                self.game.current_floor = 0
            else:
                self.game.current_floor += 1

            if self.game.current_health + 20 <= 100:
                self.game.current_health += 20
            else:
                self.current_health = 100
            self.game.transition_time = self.game.max_transition_time
            self.game.start_game(self.player, self.map, self.data)