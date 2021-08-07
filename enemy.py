from constants import *
import pygame
from main_block import *
class Enemy(Main_block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((BLOCK_SIZE // 2, BLOCK_SIZE // 2))
        self.image.fill((0, 0, 0))
        self.speed = 2





    def update(self, all_group, player_group):
        # all_group = pygame.sprite.spritecollide(self, all_group, False)
        self.rect = self.rect.move(self.speed, 0)




        # if self.rect.right > all_group[0].rect.left:
        #     self.rect = self.rect.move(0, self.speed)
        #
        # if self.rect.top > all_group[0].rect.bottom:
        #     self.rect = self.rect.move(-self.speed, 0)
        #
        #
        # if self.rect.left < all_group[0].rect.right:
        #     self.rect = self.rect.move(0, -self.speed)
        #
        # if self.rect.bottom > all_group[0].rect.top:
        #     self.rect = self.rect.move(self.speed, 0)
