from main_block import *

class Block(Main_block):

    def __init__(self):
        self.width = 100
        self.height = 64
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.center = self.rect.center




    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_z]):
            self.image = pygame.Surface((64, 10))
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(self.image.get_rect())
            self.rect.center = self.rect.center
