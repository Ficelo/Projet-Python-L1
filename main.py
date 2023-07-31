import pygame
import random
import json
from leviathan import *
from player import *
from ennemi_spike import *
from button import *
from wall import *
from map import *
from camera import *
from portal import *
from ennemi_spike_2 import *
from doors import *
from tresor import *


pygame.init()
RUNNING = True

'''Le fichier principale avec la game loop'''

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((960, 540))
        pygame.display.set_caption("Dum dum programming app")
        self.playing = True
        self.clock = pygame.time.Clock()
        self.IN_MENU = True

        self.FONT = pygame.font.Font(None, 24)

        #Les groupes de Sprites (Un peu comme des listes mais opti pour ça)
        self.allsprites = pygame.sprite.Group()
        self.tests = pygame.sprite.Group()
        self.menus = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.ennemis = pygame.sprite.Group()
        self.targeted_ennemis = pygame.sprite.Group()
        self.tresors = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()


        self.current_floor = 0
        self.current_room = 0
        self.number_of_rooms = 0
        self.all_floor_rooms = []
        self.max_transition_time = 30
        self.transition_time = self.max_transition_time

        self.max_inv_time = 5
        self.inv_time = self.max_inv_time

        self.game_won = False

        self.menu_image_1 = pygame.image.load("./Sprites/UI/test_menu_1.png")
        self.menu_image_2 = pygame.image.load("./Sprites/UI/test_menu_2.png")
        self.titre = pygame.image.load("./Sprites/UI/Titre.png")
        self.win_screen = pygame.image.load("./Sprites/UI/win_screen.png")
        
        self.ranged_idle = pygame.image.load("./Sprites/Personnages/Ranged/Ranged_Idle.png")
        self.bg = pygame.image.load("./Sprites/UI/benis.png")

        with open("./Character_data/ranged.json") as f:
            self.ranged_data = json.load(f)

        with open("./Character_data/cac.json") as f:
            self.cac_data = json.load(f)

        self.data = None

        self.map1 = Map(self, "./Room_layouts/test1.txt")
        self.map2 = Map(self, "./Room_layouts/test2.txt")
        self.map3 = Map(self,"./Room_layouts/Bossroom.txt")
        self.map4 = Map(self, './Room_layouts/test-big.txt')
        self.map5 = Map(self, "./Room_layouts/test-full-floor.txt")

        self.current_health = 100

        self.ennemis_in_room = []

        self.floor_one_maps = [self.map5]
        self.floor_two_maps = [self.map2]
        self.floor_three_maps = [self.map2]
        self.floor_four_maps = [self.map2]
        self.floor_five_maps = [self.map1]

        self.floors = [self.floor_one_maps, self.floor_two_maps, self.floor_three_maps, self.floor_four_maps, self.floor_five_maps]
        self.levels = []

        for i in self.floors:
            self.levels.append(i[random.randint(0, len(i)-1)])

        self.start_menu()

    def start_game(self, player, map, type):
        
        self.IN_MENU = False

        for sprite in self.menus:
            sprite.kill()
        for sprite in self.allsprites:
            sprite.kill()
        self.load_map(self.levels[self.current_floor], player, type)
        
        #if self.current_floor < len(self.levels) - 1:
            #portal1 = Portal(self, 64, 64, self.levels[self.current_floor + 1], player, type, False)
        self.respawn_portal = Portal(self, -1000, -1000, self.levels[self.current_floor], player, type, True)
        self.give_target()

        self.camera = Camera(self, 960, 540)


    def start_menu(self):
        
        self.Button2 = Button(self, 416 - 32, 228 + 64, 32, 32, self.menu_image_1, self.start_game, [Player, self.map1, self.ranged_data])
        self.Button1 = Button(self, 512 - 32, 228 + 64, 32, 32, self.menu_image_2, self.start_game, [Player, self.map2, self.cac_data])

    def load_map(self, map, player, type):
        self.all_floor_rooms = {}
        self.number_of_rooms = 0

        for row, tiles in enumerate(map.data):
            for col, tile in enumerate(tiles):
                if tile == 'W':
                    wall = Wall(self, col*32, row*32, 32, 32, (0,0,255))
                if tile.isnumeric():
                    if tile not in self.all_floor_rooms:
                        self.all_floor_rooms[tile] = []
                        self.all_floor_rooms[tile].append(col * 32)
                        self.all_floor_rooms[tile].append(row * 32)
                        self.ennemis_in_room.insert(int(tile), 0)

                    else:
                        self.all_floor_rooms[tile].append(col * 32)
                        self.all_floor_rooms[tile].append(row * 32)

        for row, tiles in enumerate(map.data):
                for col, tile in enumerate(tiles):
                    if tile == "E":
                        enn = Ennemi_spike(self, col*32, row*32, 32, 32)

                    if tile == "F":
                        enn = Ennemi_spike2(self, col*32, row*32, 32, 32)

                    if tile == "L":
                        enn = Leviathan(self, col*32, row*32, 32)

                    if tile == "D":
                        door = Doors(self, col*32, row*32, 32, 32, (0, 255, 0))

                    if tile == "O":
                        if self.current_floor < len(self.levels) - 1:
                            portal1 = Portal(self, col*32, row*32, self.levels[self.current_floor + 1], player, type, False)
                    
                    if tile == "T":
                        tre = Tresor(self, col*32, row*32, 32, 32)

        for row, tiles in enumerate(map.data):
                for col, tile in enumerate(tiles):            
                    if tile == 'P':
                        self.player = player(self, col, row, 32, 32, type)
    
    def give_target(self):
        for enn in self.targeted_ennemis:
            enn.target = self.player

    def run(self):
        if self.playing:
            self.clock.tick(60)
            if not self.IN_MENU:
                self.update()
                self.draw()
            else:
                self.menu_update()
                self.menu_draw()
            self.events()

    def update(self):
        self.allsprites.update()
        self.camera.update(self.player)

        if self.current_health <= 0:  #Quand le perso meurt il est renvoyé au premier niveau
            self.respawn_portal.rect.x = self.player.rect.x
            self.respawn_portal.rect.y = self.player.rect.y 
            self.current_health = 100

    def menu_update(self):
        self.menus.update()

    def screen_transition(self):
        if self.transition_time >= 0:
            self.screen.fill((0, 0, 0))
            self.transition_time -= 1

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (0, 0))
        #self.screen.blit(self.player.image, (self.player.x, self.player.y))
        for sprite in self.allsprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_stats()
        #self.screen_transition()
        if self.game_won:
            self.screen.blit(self.win_screen, (0, 0))
        pygame.display.flip()

    def menu_draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.titre, (20, 20))

        for sprite in self.menus:
            self.screen.blit(sprite.image, (sprite.x, sprite.y))
        
        pygame.display.flip()

    def draw_stats(self):
        room = self.FONT.render(f"Current room: {self.current_room}", True, (255, 255, 255))
        num_enn = self.FONT.render(f'Ennemis: {self.ennemis_in_room[self.current_room]}', True, (255, 255, 255))
        fps = self.FONT.render("FPS:" + str(self.clock.get_fps()), True, (255, 255, 255))


        if self.current_health <= 100:
            health = self.FONT.render(f"Vie: {self.current_health} %", True, (0,255,0))
        if self.current_health <= 75:
            health = self.FONT.render(f"Vie: {self.current_health} %", True, (173,255,47))
        if self.current_health <= 50:
            health = self.FONT.render(f"Vie: {self.current_health} %", True, (255,255,0))
        if self.current_health <= 20:
            health = self.FONT.render(f"Vie: {self.current_health} %", True, (255, 0, 0))

        

        self.screen.blit(room, (15, 15))
        self.screen.blit(health, (450, 15))
        self.screen.blit(fps, (15, 35))
        self.screen.blit(num_enn, (15, 55))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
            

game = Game()

while RUNNING:
    game.run()
