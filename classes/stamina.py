from global_variables import *


# Class for stamina level and stamina bar
class Stamina:
    def __init__(self, max_value, resolution, position):
        self.resolution = resolution
        self.position = position
        self.max_value = max_value
        self.value = max_value
        self.bar = pygame.Surface((1, 1))
        self.bar_resized = self.bar
        self.COLOR_FULL = (255, 255, 255)
        self.COLOR_EMPTY = (200, 0, 0)

    def redraw(self):
        if self.value <= self.max_value * 0.25:
            self.bar.fill(self.COLOR_EMPTY)
        else:
            self.bar.fill(self.COLOR_FULL)
        percentage = (self.value / self.max_value) * 100
        self.bar_resized = pygame.transform.scale(self.bar, (percentage * self.resolution[0] / 100, self.resolution[1]))
        self.position[0] = SCREEN.get_width() / 2 - self.bar_resized.get_width() / 2

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value
        if self.value < 0:
            self.value = 0
        self.redraw()

    def decrease(self, amount):
        self.value -= amount
        if self.value > self.max_value:
            self.value = self.max_value
        if self.value < 0:
            self.value = 0
        self.redraw()

    def render(self):
        if not self.value == self.max_value:
            SCREEN.blit(self.bar_resized, self.position)