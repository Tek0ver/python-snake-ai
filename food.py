from settings import *
from random import randint
import pygame

class Food:
    def __init__(self, snake):

        self.image = pygame.Surface((GAME_RESOLUTION,GAME_RESOLUTION))
        self.image.fill((194,46,46))
        self.rect = self.image.get_rect()

        self.spawn(snake)

    def spawn(self, snake):

        if NO_FOOD:
            self.rect.topleft = (-1000,-1000)
        else:
            self.rect.topleft = (randint(0,GAME_GRID - 1) * GAME_RESOLUTION,
                             randint(0,GAME_GRID - 1) * GAME_RESOLUTION)
        
        if self.rect.collidelist(snake.tail) != -1 or self.rect.colliderect(snake.rect) is True:
            self.spawn(snake)
    
    def draw(self, screen):

        screen.blit(self.image, self.rect)
