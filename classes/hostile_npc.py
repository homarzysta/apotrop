from global_functions import circle_collision
from global_variables import *

# Class for computing Hostile NPC
class HostileNpc:
    def __init__(self, position, skin):
        self.position = position
        self.skin = skin
        self.edited_skin = skin
        self.speed = randint(40, 100) / 1000

    def chase(self):
        angle = math.degrees(math.atan2(152 - (self.position[1] - int(player_position[1])), 152 - (self.position[0] - int(player_position[0]))))
        self.edited_skin = pygame.transform.rotate(self.skin, -angle + 90)

        updated_position = [self.position[0] + math.sin(math.radians(angle+90)) * (self.speed * delta_time.value), self.position[1] - math.cos(math.radians(angle+90)) * (self.speed * delta_time.value)]

        collides = circle_collision(updated_position[0], updated_position[1], self.skin.get_height() / 2, player_position[0] + 152, player_position[1] + 152, player_scaled.get_height() / 2)

        if not collides:
            self.position[1] = updated_position[1]
            self.position[0] = updated_position[0]

    def render(self):
        self.chase()
        pygame.draw.circle(display, (255, 0, 0), (self.position[0] + self.skin.get_width() / 2 - player_position[0], self.position[1] + self.skin.get_height() / 2 - player_position[1]), self.skin.get_height() / 2, 1)
        pygame.draw.circle(display, (0, 0, 255), (player_position[0] + 160 - player_position[0], player_position[1] + 160 - player_position[1]), player_scaled.get_height() / 2, 1)
        display.blit(self.edited_skin, (self.position[0] - player_position[0], self.position[1] - player_position[1]))