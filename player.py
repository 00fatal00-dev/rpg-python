import pygame
import json

class Player():
    def __init__(self, x, y, width, height, colour, move_speed, move_x, move_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.move_speed = move_speed
        self.move_x = move_x
        self.move_y = move_y
        self.stats = {
            'health': 100
        }


    def set_stats(self, stat_to_set, new_value):
        pass

    def get_stats(self, stat_to_get):
        return self.stats[stat_to_get]
