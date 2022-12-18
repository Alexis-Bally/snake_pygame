import pygame
import random

class Food():

    def __init__(self):
        self.food_pos = [random.randrange(1, (720//10)) * 10, random.randrange(1, (480//10)) * 10]
        self.food_spawn = True

    def food_draw(self, game_window):
        pygame.draw.rect(game_window, (255, 0, 0), pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))

    def spawn(self):
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (720//10)) * 10, random.randrange(1, (480//10)) * 10]
        self.food_spawn = True