from global_variables import *


# Class for computing props
class Prop:
    def __init__(self, position, skin):
        self.position = position
        self.skin = skin
        self.edited_skin = skin

    def render(self):
        display.blit(self.edited_skin, (self.position[0] - int(player_position[0]), self.position[1] - int(player_position[1])))