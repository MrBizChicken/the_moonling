from constants import *
import pygame
from main_block import *
class Enemy(Main_block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((BLOCK_SIZE // 2, BLOCK_SIZE // 2))
        self.image.fill((0, 0, 0))





    def update(self, all_group):
        hits = pygame.sprite.spritecollide(self, all_group, False)
