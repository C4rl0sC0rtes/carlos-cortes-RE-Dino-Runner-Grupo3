import random
from dino_runner.components.obstacles.obstacle import Obstacles
from dino_runner.utils.constants import (LARGE_CACTUS, SMALL_CACTUS, BIRD)

class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        if self.image == LARGE_CACTUS:
            self.rect.y = 296
        elif self.image == SMALL_CACTUS: 
            self.rect.y = 319
        #if self.image == BIRD and self.type == 2:
         #   pass

