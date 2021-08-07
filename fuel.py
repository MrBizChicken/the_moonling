from main_block import *
import constants
class Fuel(Main_block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 500
        self.height =  20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)




    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_z]):
            self.width -= 1
            self.height = 20
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(self.image.get_rect())
            self.rect.center = self.rect.center
        if self.width <= 475:
            self.image.fill((255,223,0))
        if self.width <= 350:
            self.image.fill((255,223,0))            
