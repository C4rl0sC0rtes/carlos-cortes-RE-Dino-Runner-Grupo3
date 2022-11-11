from dino_runner.utils.constants import CLOUD
import random

X_POS = 1200
Y_POS = 200

class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.second_cloud_rect = self.image.get_rect()

        self.cloud_rect.x = X_POS
        self.cloud_rect.y = Y_POS

        self.second_cloud_rect.x = X_POS
        self.second_cloud_rect.y = Y_POS


        self.step_index = 0

    def update(self):
        self.run()
        if self.step_index >= 10:
            self.step_index = 0
    
    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
        screen.blit(self.image, (self.second_cloud_rect.x, self.second_cloud_rect.y))

    def run(self):
        self.cloud_rect.x -= 6
        self.step_index +=1
        if self.cloud_rect.x < -self.cloud_rect.width:
            self.cloud_rect.x = X_POS * 1.2
            cloud_altitude = random.randint(0, 2)
            if cloud_altitude == 0:
                self.cloud_rect.y = Y_POS
            elif cloud_altitude == 1:
                self.cloud_rect.y = Y_POS / 4
            else:
                self.cloud_rect.y = Y_POS * 1.5

        self.second_cloud_rect.x -= 4
        if self.second_cloud_rect.x < -self.second_cloud_rect.width:
            self.second_cloud_rect.x = X_POS * 1.8
            cloud_altitude = random.randint(0, 1)
            if cloud_altitude == 0:
                self.second_cloud_rect.y = 80
            elif cloud_altitude == 1:
                self.second_cloud_rect.y = 150
        


