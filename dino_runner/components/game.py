import pygame

from dino_runner.components import text_utils
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import (
   BG, 
   ICON, 
   SCREEN_HEIGHT, 
   SCREEN_WIDTH, 
   TITLE, FPS, 
   RUNNING, 
   DINO_DEAD,
   GAME_OVER,
   HEART_COUNT
)

from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import Player_heart_manager
from dino_runner.components.clouds import Cloud



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.runnning = True
        self.death_count = 0
        self.print_score = 0
        self.power_up_manager = PowerUpManager()
        self.player_heart_manager = Player_heart_manager()
        self.cloud = Cloud()
        


    def run(self):
        self.create_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.print_score = self.points
            if self.death_count == HEART_COUNT: #reinicia los componentes despues de una muerte
                self.create_components()
    
    def create_components(self):
        self.obstacle_manager.reset_obstacles(self)
        self.power_up_manager.reset_power_ups()  #Se quito el parametro
        self.player_heart_manager.reset_hearts()
        self.points = 0
        self.game_speed = 10

    def execute(self):
        while self.runnning:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                self.playing = False
                self.runnning = False
        self.screen.fill((255, 255, 255))


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update()
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        


    def draw(self):
        self.score() ##MOSTRAR EL SCORE EN TIEMPO REAL EN LA PANTALLA  
        self.clock.tick(FPS)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.cloud.draw(self.screen)


        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        self.player.check_invicibility(self.screen)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runnning = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            #self.create_components()
            white_color = (255, 255, 255)
            self.screen.fill(white_color)
            text, text_rect = text_utils.get_centred_message('Press any Key to Start')
            self.screen.blit(text, text_rect)
            self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height - 140))
        elif self.death_count > 0:
            red_color = (239, 21, 21)
            self.screen.fill(red_color)
            text, text_rect = text_utils.get_centred_message('Press any Key to Restart')
            score, score_rect = text_utils.get_centred_message('Your score: '+ str(self.print_score), height=half_screen_height + 50)
            death, death_rect = text_utils.get_centred_message('Death count: '+ str(self.death_count), height=half_screen_height + 100)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
            self.screen.blit(DINO_DEAD, (half_screen_width - 20, half_screen_height - 140))
            self.screen.blit(GAME_OVER, (half_screen_width -190, half_screen_height -200))


    def show_menu(self):
        self.runnning = True
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()
        