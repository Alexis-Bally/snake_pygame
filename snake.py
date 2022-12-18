import pygame
import sys

class Snake():


    def __init__(self):
        self.score = 0
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]


    def snake_draw(self, game_window):
        for pos in self.snake_body:
            pygame.draw.rect(game_window, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))


    def grow(self, food):
        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos[0] == food.food_pos[0] and self.snake_pos[1] == food.food_pos[1]:
            self.score += 1
            food.food_spawn = False
            return food
        else:
            self.snake_body.pop()


    def movements(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('z'):
                    self.change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('q'):
                    self.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10


    def out_of_bound(self):
        if self.snake_pos[0] < 0:
            self.snake_pos[0] = 720-10
        if self.snake_pos[0] > 720-10:
            self.snake_pos[0] = 0
        if self.snake_pos[1] < 0:
            self.snake_pos[1] = 480-10
        if self.snake_pos[1] > 480-10:
            self.snake_pos[1] = 0