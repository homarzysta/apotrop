from global_variables import *


def render_fog(surface, color, radius, layers):
    surface.fill(color)
    for offset in range(0, layers):
        pygame.draw.circle(surface, (color[0], color[1], color[2], 255 - (offset*3)), (surface.width / 2, surface.height / 2), radius / 2 - offset)
    pygame.draw.circle(surface, (color[0], color[1], color[2], 255 - (layers*3)), (surface.width / 2, surface.height / 2), radius / 2 - layers)

def circle_collision(x1, y1, r1, x2, y2, r2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance < r1 + r2
