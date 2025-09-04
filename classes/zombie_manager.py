from global_variables import *


# Class for managing zombies NPCs
class ZombieManager:
    def __init__(self, entity_class):
        self.container = []
        self.entity_class = entity_class

    def spawn(self):
        random = randint(0, 3)
        if random == 0:
            self.container.append(self.entity_class([randint(0, 320), 0], zombie_scaled))
        if random == 1:
            self.container.append(self.entity_class([randint(0, 320), 320], zombie_scaled))
        if random == 2:
            self.container.append(self.entity_class([0, randint(0, 320)], zombie_scaled))
        if random == 3:
            self.container.append(self.entity_class([320, randint(0, 320)], zombie_scaled))

    def render(self):
        for entity in self.container:
            entity.render()