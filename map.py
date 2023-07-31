import pygame


class Map:
    def __init__(self, game, file):
        self.data = []
        with open(file, 'rt') as f:
            for line in f:
                self.data.append(line)

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = (self.tilewidth - 1) * 32
        self.height = self.tileheight * 32