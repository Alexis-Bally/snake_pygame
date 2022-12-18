import pygame
import sys
import time
import random
from snake import Snake
from food import Food

pygame.init()

game_window = pygame.display.set_mode((720, 480))

fps = pygame.time.Clock()

snake = Snake()
food = Food()


def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (720/2, 480/4)
    game_window.fill((0, 0, 0))
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, (255, 0, 0), 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(snake.score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (720/10, 15)
    else:
        score_rect.midtop = (720/2, 480/1.25)
    game_window.blit(score_surface, score_rect)


while True:

    snake.movements()

    snake.grow(food)

    # Dessins et fond
    game_window.fill((150, 150, 150))
    snake.snake_draw(game_window, )
    food.food_draw(game_window)

    food.spawn()

    snake.out_of_bound()

    # Condition de défaite
    # Toucher le corps de Snake
    for block in snake.snake_body[1:]:
        if snake.snake_pos[0] == block[0] and snake.snake_pos[1] == block[1]:
            game_over()

    show_score(1, (255, 255, 255), 'consolas', 20)
    pygame.display.update()
    fps.tick(24)