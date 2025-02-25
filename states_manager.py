from constants import *
import sys, pygame, player, camera, wall, block, random, main_drop



class States_manager:
    def __init__(self):
        self.running = True
        self.states = ["start", "running", "paused", "dead"]
        self.state = self.states[1]

        self.all_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.items = pygame.sprite.Group()


        n = 20
        self.player = player.Player()
        # the args for this need to be the w, h, of the world map NOT THE SCREEN SIZE!
        self.camera = camera.Camera(n * BLOCK_SIZE, n * BLOCK_SIZE)

        # self.player_group.add(self.player)

        # adds walls
        for i in range(100):
            r = random.randint(0, GAME_WORLD_W) // BLOCK_SIZE * BLOCK_SIZE
            c = random.randint(0, GAME_WORLD_H) // BLOCK_SIZE * BLOCK_SIZE
            self.all_group.add(wall.Wall(r, c))


        # adds pickups
        self.items.add(main_drop.Main_drop(BLOCK_SIZE * 3, BLOCK_SIZE * 3))

        self.player_group.add(self.player)

    def events(self, events):

        # print(events)
        for event in events:
            # if event.type == pygame.QUIT:
            #     self.running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                #used to kill outside loop
                if event.key == pygame.K_q:
                    return True

                if event.key == pygame.K_r:
                    # Reset map
                    self.map.reset()

                if event.key == pygame.K_p:

                    if self.state == "paused":
                        self.state = "running"
                    else:
                        self.state = "paused"

            if event.type == pygame.KEYUP:

                if event.key == 32:#SPACE
                    #Start Screen
                    if self.state == "start":
                        self.state = "running"

                    #Dig a block
                    if self.state == "running":
                        for all in self.all_group:
                            all.dig(self.player)


    def draw(self, surface):
        # surface.fill((100, 100, 100))#background


        if self.state == "start":
            surface.fill((100, 100, 255))#background

        elif self.state == "running":


            for wall in self.all_group:
                surface.blit(wall.image, self.camera.move(wall.rect))

            for player in self.player_group:
                surface.blit(player.image, self.camera.move(player.rect))

            for item in self.items:
                surface.blit(item.image, self.camera.move(item.rect))





            self.camera.draw(surface)
            self.draw_grid(surface)


        elif self.state == "paused":
            surface.fill((255, 100, 100))#background


        elif self.state == "dead":
            surface.fill((50, 50, 50))#background

        pygame.display.flip()


    def update(self, surface):
        surface.fill((100, 100, 100))#background
        self.camera.update(self.player)

        if self.state == "start":
            pass
        elif self.state == "running":
            self.camera.update(self.player)
            self.all_group.update()
            self.player_group.update(self.all_group)
            self.items.update(self.player_group)

        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass


    def draw_grid(self, surface):
        for x in range(0, GAME_WIDTH, BLOCK_SIZE):
            pygame.draw.line(surface, BLUE, (x, 0), (x, GAME_HEIGHT))
        for y in range(0, GAME_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(surface, BLUE, (0, y), (GAME_WIDTH, y))
