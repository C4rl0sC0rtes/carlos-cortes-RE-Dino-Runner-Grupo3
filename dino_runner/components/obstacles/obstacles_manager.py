import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import (
    SMALL_CACTUS, LARGE_CACTUS, GAME_OVER_SOUND, BIRD, HIT, COLLISION)
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from pygame import mixer
pygame.mixer.init()

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.PowerUp = PowerUpManager()  

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0, 2)
            if cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:

            obstacle.update(game.game_speed, self.obstacles)

            if game.player.hammer is not None and game.player.hammer.rect.colliderect(obstacle.rect):
                game.player.hammer.kill() 
                self.obstacles.pop()
                COLLISION.play()
            else:
                obstacle.update(game.game_speed, self.obstacles)


            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:

                    HIT.play()
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        if game.player_heart_manager.heart_count == 0:
                            GAME_OVER_SOUND.play()

                        break 
                else:
                    self.obstacles.remove(obstacle)
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []




