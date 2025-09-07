from global_functions import *
from classes import *


render_fog(display_fog, AMBIENT_COLOR, display.get_height() + 10, 50)

# Objects initializing
prop1 = Prop((160, 160), player_scaled)

zombie_manager = ZombieManager(HostileNpc)
for _ in range(0, 5):
    zombie_manager.spawn()

stamina = Stamina(1000, (500, 5), [0, SCREEN.get_height() - 20])


# Main game loop
while True:
    # Game inputs gathering
    delta_time.update()
    keys = pygame.key.get_pressed()
    buttons = pygame.mouse.get_pressed()

    # Pygame events input
    for event in pygame.event.get():
        # Window close input
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] or keys[pygame.K_LALT] and keys[pygame.K_F4]:
            pygame.quit()
            sys.exit()

        # Mouse movement input
        if event.type == pygame.MOUSEMOTION:
            mouse_x, _ = event.rel
            if buttons[2]:
                map_rotate += mouse_x * 0.05
            else:
                map_rotate += mouse_x * 0.3

    # Player input
    if keys[pygame.K_LCTRL] or buttons[2]:
        player_speed = 0.05
    elif keys[pygame.K_LSHIFT] and stamina.value > 0:
        player_speed = 0.125
    else:
        player_speed = 0.1
    if (keys[pygame.K_w] or keys[pygame.K_s]) and (keys[pygame.K_a] or keys[pygame.K_d]):
        player_speed = player_speed / math.sqrt(2)

    # Stamina input
    if keys[pygame.K_LCTRL] and not buttons[2]:
        stamina.increase(4)
    elif keys[pygame.K_LSHIFT] and stamina.value > 0:
        stamina.decrease(10)
    elif not keys[pygame.K_LSHIFT]:
        stamina.increase(2)

    # Movement input
    if keys[pygame.K_w]:
        player_position[1] -= math.cos(math.radians(map_rotate)) * (player_speed * delta_time.value)
        player_position[0] += math.sin(math.radians(map_rotate)) * (player_speed * delta_time.value)
    if keys[pygame.K_s]:
        player_position[1] += math.cos(math.radians(map_rotate)) * (player_speed * delta_time.value)
        player_position[0] -= math.sin(math.radians(map_rotate)) * (player_speed * delta_time.value)
    if keys[pygame.K_a]:
        player_position[1] += math.cos(math.radians(map_rotate+90)) * (player_speed * delta_time.value)
        player_position[0] -= math.sin(math.radians(map_rotate+90)) * (player_speed * delta_time.value)
    if keys[pygame.K_d]:
        player_position[1] += math.cos(math.radians(map_rotate-90)) * (player_speed * delta_time.value)
        player_position[0] -= math.sin(math.radians(map_rotate-90)) * (player_speed * delta_time.value)

    # Objects render
    display.fill((0, 40, 0))

    prop1.render()
    zombie_manager.render()

    # Laser render
    if buttons[2]:
        display_height = 250
        end_x = display.get_width() / 2 + math.cos(math.radians(map_rotate-90)) * 160
        end_y = display.get_height() / 2 + math.sin(math.radians(map_rotate-90)) * 160
        pygame.draw.aaline(display, (255, 255, 255), (display.get_width() / 2, display.get_height() / 2), (end_x, end_y), 1)
    else:
        display_height = 0

    # Player render
    display.blit(pygame.transform.rotate(weapon_scaled, -map_rotate), (display.get_width() / 2 - weapon_scaled.get_width() / 2, display.get_height() / 2 - weapon_scaled.get_height() / 2))
    display.blit(pygame.transform.rotate(player_scaled, -map_rotate), (display.get_width() / 2 - player_scaled.get_width() / 2, display.get_height() / 2 - player_scaled.get_height() / 2))

    # Display render
    rect = display_fog.get_rect(center=(160, 160))
    display.blit(display_fog, rect)
    display_resized = pygame.transform.rotate(pygame.transform.scale(display, (SCREEN.get_height(), SCREEN.get_height())), map_rotate)

    # Screen render
    SCREEN.fill(AMBIENT_COLOR)
    SCREEN.blit(display_resized, (SCREEN.get_width() / 2 - display_resized.get_width() / 2, SCREEN.get_height() / 2 - display_resized.get_height() / 2)) # + display_height
    stamina.render()

    # Display update
    pygame.display.update()