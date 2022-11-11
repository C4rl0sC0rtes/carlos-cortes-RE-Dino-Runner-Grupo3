import random
from dino_runner.components.obstacles.obstacle import Obstacles
import pygame

class Bird(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0,1)
        self.high = random.randint(0,2)
        self.step_index = 0
        super().__init__(image, self.type)
        if self.high == 0:
            self.rect.y = 50
        elif self.high == 1:
            self.rect.y = 270
        else: 
            self.rect.y = 320

        