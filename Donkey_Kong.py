import arcade

# Screen Variables
screen_width = 500
screen_height = 700
screen_title = "Donkey Kong"

# Physic Variables
mario_player_gravity = 0
mario_player_is_jump = False
mario_player_jump_counter = 15
velocity = 0.1
player_movement_speed = 5
player_jump_speed = 0.01
normal_barrel_movement_speed = 7
ladder_barrel_movement_speed = 7

# Player Variables

# Mario
mario_player_x = 65
mario_player_y = 55
mario_player_up_pressed = False
mario_player_down_pressed = False
mario_player_left_pressed = False
mario_player_right_pressed = False
mario_player_on_ladder = False
mario_player_touching_platform = True
mario_player_alive = True

# Luigi
luigi_player_x = 50
luigi_player_y = 55
luigi_player_up_pressed = False
luigi_player_down_pressed = False
luigi_player_left_pressed = False
luigi_player_right_pressed = False
luigi_player_on_ladder = False
luigi_player_touching_platform = True
luigi_player_alive = True

# Donkey Kong Variables
donkey_kong_player_x = 70
donkey_kong_player_y = 615
donkey_kong_player_alive = True

# Barrel Conditions
donkey_kong_player_barrel_condition = True
donkey_kong_player_barrel_tick_count = 0

# Barrel Types

# Normal Barrels Variables
donkey_kong_player_normal_barrel_pressed = False
donkey_kong_player_normal_barrel_cool_down = 3

donkey_kong_player_normal_barrel_x = 55
donkey_kong_player_normal_barrel_y = 600

# Invisible Barrels Variables (filled rectangle not filled)
donkey_kong_player_invisible_barrel_pressed = False
donkey_kong_player_invisible_barrel_cool_down = 7

donkey_kong_player_invisible_barrel_x = 55
donkey_kong_player_invisible_barrel_y = 600

# Mario Ladder Barrels Variables (affects mario)
donkey_kong_player_mario_ladder_barrel_pressed = False
donkey_kong_player_mario_ladder_barrel_cool_down = 5
ladder_type_mario = False

donkey_kong_ladder_mario_ladder_barrel_x = 55
donkey_kong_player_mario_ladder_barrel_y = 600

# Luigi Ladder Barrel Variables (affects luigi)
donkey_kong_player_luigi_ladder_barrel_pressed = False
donkey_kong_player_luigi_ladder_barrel_cool_down = 5
ladder_type_luigi = False

donkey_kong_player_luigi_ladder_barrel_x = 55
donkey_kong_player_luigi_ladder_barrel_y = 600

# Big Barrels Variables (slow but big bois)
donkey_kong_player_big_barrel_pressed = False
donkey_kong_player_big_barrel_cool_down = 10

donkey_kong_player_big_barrel_x = 55
donkey_kong_player_big_barrel_y = 600

# Small Barrels Variables (fast but little bois)
donkey_kong_player_small_barrel_pressed = False
donkey_kong_player_small_barrel_cool_down = 10

donkey_kong_player_small_barrel_x = 55
donkey_kong_player_small_barrel_y = 600

# Game Aspect Variables
mario_player_lives = 3
luigi_player_lives = 3
points_score_total = 0
points_normal_barrel = 100
points_invisible_barrel = 500
points_mario_ladder_barrel = 250
points_luigi_ladder_barrel = 250
points_big_barrel = 500
points_small_barrel = 50


def on_update(delta_time):
    """
    Updates the code constantly

    :param delta_time:
    :return:
    """
    global mario_player_up_pressed, mario_player_down_pressed, mario_player_left_pressed, mario_player_right_pressed, \
        mario_player_y, mario_player_x, mario_player_touching_platform, mario_player_alive, mario_player_is_jump

    global luigi_player_x, luigi_player_y, luigi_player_up_pressed, luigi_player_down_pressed, \
        luigi_player_right_pressed, luigi_player_left_pressed, luigi_player_touching_platform, luigi_player_alive

    global donkey_kong_player_normal_barrel_pressed, donkey_kong_player_mario_ladder_barrel_pressed, \
        donkey_kong_player_luigi_ladder_barrel_pressed, donkey_kong_player_big_barrel_pressed, \
        donkey_kong_player_big_barrel_pressed, donkey_kong_player_alive

    global velocity

    # Mario Conditions
    # if mario_player_up_pressed and mario_player_touching_platform and mario_player_alive:
    #    jump()
    #    mario_player_touching_platform = True
    #    mario_player_is_jump = False
    if mario_player_up_pressed and mario_player_on_ladder and mario_player_alive:
        mario_player_y += 2
    if mario_player_down_pressed and mario_player_on_ladder and mario_player_alive:
        mario_player_y -= 2
    if mario_player_right_pressed and mario_player_alive:
        mario_player_x += 2 + velocity
        velocity += 0.03
    if mario_player_left_pressed and mario_player_alive:
        mario_player_x -= 2 - velocity
        velocity -= 0.03

    # Mario State Condition
    if not mario_player_alive:
        mario_player_x = mario_player_x
        mario_player_y = mario_player_y

    # Luigi Conditions
    if luigi_player_up_pressed and luigi_player_touching_platform and luigi_player_alive or luigi_player_up_pressed \
            and luigi_player_on_ladder and luigi_player_alive:
        luigi_player_y += 2
    if luigi_player_down_pressed and luigi_player_alive:
        luigi_player_y -= 2
    if luigi_player_right_pressed and luigi_player_alive:
        luigi_player_x += 2
    if luigi_player_left_pressed and luigi_player_alive:
        luigi_player_x -= 2

    # Luigi State Condition
    if not luigi_player_alive:
        luigi_player_x = luigi_player_x
        luigi_player_y = luigi_player_y

    # Donkey Kong Condition
    if donkey_kong_player_normal_barrel_pressed and donkey_kong_player_alive:
        normal_barrel()
    if donkey_kong_player_mario_ladder_barrel_pressed and donkey_kong_player_alive:
        ladder_barrel_mario()
    if donkey_kong_player_mario_ladder_barrel_pressed and donkey_kong_player_alive:
        ladder_barrel_luigi()
    if donkey_kong_player_invisible_barrel_pressed and donkey_kong_player_alive:
        invisible_barrel()
    if donkey_kong_player_big_barrel_pressed and donkey_kong_player_alive:
        big_barrel()
    if donkey_kong_player_small_barrel_pressed and donkey_kong_player_alive:
        small_barrel()

    collision()
    donkey_kong()


def player():
    """
    Drawing the players Mario and Luigi

    :return:
    """
    global mario_player_x, mario_player_y

    global luigi_player_x, luigi_player_y

    # Mario
    arcade.draw_rectangle_outline(mario_player_x, mario_player_y, 10, 10, arcade.color.RED)

    # Luigi
    arcade.draw_rectangle_outline(luigi_player_x, luigi_player_y, 10, 10, arcade.color.GREEN)


def normal_barrel():
    """
    Drawing the normal barrel

    :return:
    """
    global donkey_kong_player_normal_barrel_x, donkey_kong_player_normal_barrel_y
    arcade.draw_rectangle_outline(donkey_kong_player_normal_barrel_x, donkey_kong_player_normal_barrel_y, 15, 15,
                                  arcade.color.FRENCH_BEIGE)
    donkey_kong_player_normal_barrel_x += 2


def invisible_barrel():
    """
    Drawing the invisible barrel

    :return:
    """
    global donkey_kong_player_invisible_barrel_x, donkey_kong_player_invisible_barrel_y
    arcade.draw_rectangle_outline(donkey_kong_player_invisible_barrel_x, donkey_kong_player_invisible_barrel_y, 15, 15,
                                  arcade.color.GHOST_WHITE)
    donkey_kong_player_invisible_barrel_x += 2


def big_barrel():
    """
    Drawing the big barrel

    :return:
    """
    global donkey_kong_player_big_barrel_x, donkey_kong_player_big_barrel_y
    arcade.draw_rectangle_outline(donkey_kong_player_big_barrel_x, donkey_kong_player_big_barrel_y, 20, 20,
                                  arcade.color.YELLOW)
    donkey_kong_player_big_barrel_x += 1


def small_barrel():
    """
    Drawing the small barrel

    :return:
    """
    global donkey_kong_player_small_barrel_x, donkey_kong_player_small_barrel_y
    arcade.draw_rectangle_outline(donkey_kong_player_small_barrel_x, donkey_kong_player_small_barrel_y, 10, 10,
                                  arcade.color.BLUE)
    donkey_kong_player_small_barrel_x += 5


def ladder_barrel_mario():
    """
    Drawing the Mario ladder barrel

    :return:
    """
    global donkey_kong_ladder_mario_ladder_barrel_x, donkey_kong_player_mario_ladder_barrel_y

    # Mario Ladder Barrels
    arcade.draw_rectangle_outline(donkey_kong_ladder_mario_ladder_barrel_x, donkey_kong_player_mario_ladder_barrel_y,
                                  15, 15, arcade.color.RED_VIOLET)
    donkey_kong_ladder_mario_ladder_barrel_x += 2


def ladder_barrel_luigi():
    """
    Drawing the Luigi ladder barrel

    :return:
    """
    global donkey_kong_player_luigi_ladder_barrel_x, donkey_kong_player_luigi_ladder_barrel_y

    # Luigi Ladder Barrels
    arcade.draw_rectangle_outline(donkey_kong_player_luigi_ladder_barrel_x, donkey_kong_player_luigi_ladder_barrel_y,
                                  15, 15, arcade.color.GUPPIE_GREEN)
    donkey_kong_player_luigi_ladder_barrel_x += 2


def donkey_kong():
    """
    Drawing Donkey Kong

    :return:
    """
    global donkey_kong_player_x, donkey_kong_player_y

    arcade.draw_rectangle_outline(donkey_kong_player_x, donkey_kong_player_y, 50, 50, arcade.color.CERULEAN)


def ladder():
    """
    Drawing the ladders

    :return:
    """
    # Mario Ladder (bottom floor - platform 1)
    arcade.draw_rectangle_outline(180, 80, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (bottom floor - platform 1)
    arcade.draw_rectangle_outline(320, 80, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 1 - platform 2)
    arcade.draw_rectangle_outline(370, 140, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 1 - platform 2)
    arcade.draw_rectangle_outline(250, 140, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 2 - platform 3)
    arcade.draw_rectangle_outline(320, 200, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 2 - platform 3)
    arcade.draw_rectangle_outline(180, 200, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 3 - platform 4)
    arcade.draw_rectangle_outline(250, 260, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 3 - platform 4)
    arcade.draw_rectangle_outline(370, 260, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 4 - platform 5)
    arcade.draw_rectangle_outline(180, 320, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 4 - platform 5)
    arcade.draw_rectangle_outline(320, 320, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 5 - platform 6)
    arcade.draw_rectangle_outline(370, 380, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 5 - platform 6)
    arcade.draw_rectangle_outline(250, 380, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 6 - platform 7)
    arcade.draw_rectangle_outline(320, 440, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 6 - platform 7)
    arcade.draw_rectangle_outline(180, 440, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 7 - platform 8)
    arcade.draw_rectangle_outline(250, 500, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 7 - platform 8)
    arcade.draw_rectangle_outline(370, 500, 25, 60, arcade.color.APPLE_GREEN)

    # Mario Ladder (platform 8 - platform 9)
    arcade.draw_rectangle_outline(180, 560, 25, 60, arcade.color.RED_ORANGE)

    # Luigi Ladder (platform 8 - platform 9)
    arcade.draw_rectangle_outline(320, 560, 25, 60, arcade.color.APPLE_GREEN)

    # The Winning Ladder (purple)
    arcade.draw_rectangle_outline(200, 623, 25, 65, arcade.color.PURPLE_HEART)


def on_draw():
    """
    Drawing everything

    :return:
    """
    global mario_player_x, mario_player_y

    global luigi_player_x, luigi_player_y

    arcade.start_render()

    # Left and Right Walls
    arcade.draw_rectangle_outline(20, screen_height / 2, 50, 700, arcade.color.RUSTY_RED)
    arcade.draw_rectangle_outline(480, screen_height / 2, 50, 700, arcade.color.RUSTY_RED)

    # Bottom Floor
    arcade.draw_rectangle_outline(screen_width / 2, 25, 500, 50, arcade.color.RUSTY_RED)

    # Top Ceiling
    arcade.draw_rectangle_outline(screen_width / 2, 690, 500, 50, arcade.color.RUSTY_RED)

    # Platform 1 (from bottom)
    arcade.draw_rectangle_outline(20, 100, 750, 20, arcade.color.RUSTY_RED)

    # Platform 2 (from bottom)
    arcade.draw_rectangle_outline(480, 160, 750, 20, arcade.color.RUSTY_RED)

    # Platform 3 (from bottom)
    arcade.draw_rectangle_outline(20, 220, 750, 20, arcade.color.RUSTY_RED)

    # Platform 4 (from bottom)
    arcade.draw_rectangle_outline(480, 280, 750, 20, arcade.color.RUSTY_RED)

    # Platform 5 (from bottom)
    arcade.draw_rectangle_outline(20, 340, 750, 20, arcade.color.RUSTY_RED)

    # Platform 6 (from bottom)
    arcade.draw_rectangle_outline(480, 400, 750, 20, arcade.color.RUSTY_RED)

    # Platform 7 (from bottom)
    arcade.draw_rectangle_outline(20, 460, 750, 20, arcade.color.RUSTY_RED)

    # Platform 8 (from bottom)
    arcade.draw_rectangle_outline(480, 520, 750, 20, arcade.color.RUSTY_RED)

    # Platform 9 (from bottom)
    arcade.draw_rectangle_outline(20, 580, 750, 20, arcade.color.RUSTY_RED)

    ladder()
    donkey_kong()
    win_condition()
    player()


def collision():
    """
    Collision

    :return:
    """
    global mario_player_x, mario_player_y, mario_player_alive, mario_player_on_ladder

    global donkey_kong_player_normal_barrel_x, donkey_kong_player_normal_barrel_y, \
        donkey_kong_player_invisible_barrel_x, donkey_kong_player_invisible_barrel_y, \
        donkey_kong_ladder_mario_ladder_barrel_x, donkey_kong_player_mario_ladder_barrel_y, \
        donkey_kong_ladder_mario_ladder_barrel_x, donkey_kong_player_luigi_ladder_barrel_y, \
        donkey_kong_player_big_barrel_x, donkey_kong_player_big_barrel_y, \
        donkey_kong_player_small_barrel_x, donkey_kong_player_small_barrel_y

    global luigi_player_x, luigi_player_y, luigi_player_alive, luigi_player_on_ladder

    # Mario Collision

    # Two Walls And Bottom Floor
    if mario_player_x - 1 <= 50:
        mario_player_x = 50
    if mario_player_x + 1 >= 450:
        mario_player_x = 450
    if mario_player_y <= 55:
        mario_player_y = 55

    # Platform 1 (from bottom) Bottom Collision
    if (85 <= mario_player_y + 1 <= 105) and mario_player_x + 1 <= 400:
        mario_player_y = 85

    # Platform 1 (from bottom) Top Collision
    if (85 <= mario_player_y - 1 <= 115) and mario_player_x + 1 <= 400:
        mario_player_y = 115

    # Platform 1 (from bottom) Right Side Collision
    if (85 <= mario_player_y - 1 <= 110) and mario_player_x - 1 <= 400:
        mario_player_x = 400

    # Platform 2 (from bottom) Bottom Collision
    if (145 <= mario_player_y + 1 <= 155) and mario_player_x - 1 >= 100:
        mario_player_y = 145

    # Platform 2 (from bottom) Top Collision
    if (150 <= mario_player_y - 1 <= 175) and mario_player_x - 1 >= 100:
        mario_player_y = 175

    # Platform 2 (from bottom) Side Collision
    if (150 <= mario_player_y - 1 <= 165) and mario_player_x + 1 >= 100:
        mario_player_x = 100

    # Platform 3 (from bottom) Bottom Collision
    if (205 <= mario_player_y + 1 <= 215) and mario_player_x + 1 <= 400:
        mario_player_y = 205

    # Platform 3 (from bottom) Top Collision
    if (205 <= mario_player_y - 1 <= 235) and mario_player_x + 1 <= 400:
        mario_player_y = 235

    # Platform 3 (from bottom) Right Side Collision
    if (205 <= mario_player_y - 1 <= 220) and mario_player_x - 1 <= 400:
        mario_player_x = 400

    # Platform 4 (from bottom) Bottom Collision
    if (265 <= mario_player_y + 1 <= 275) and mario_player_x - 1 >= 100:
        mario_player_y = 265

    # Platform 4 (from bottom) Top Collision
    if (265 <= mario_player_y - 1 <= 295) and mario_player_x - 1 >= 100:
        mario_player_y = 295

    # Platform 4 (from bottom) Side Collision
    if (265 <= mario_player_y - 1 <= 285) and mario_player_x + 1 >= 100:
        mario_player_x = 100

    # Platform 5 (from bottom) Bottom Collision
    if (325 <= mario_player_y + 1 <= 340) and mario_player_x + 1 <= 400:
        mario_player_y = 325

    # Platform 5 (from bottom) Top Collision
    if (325 <= mario_player_y - 1 <= 355) and mario_player_x + 1 <= 400:
        mario_player_y = 355

    # Platform 5 (from bottom) Right Side Collision
    if (325 <= mario_player_y - 1 <= 350) and mario_player_x - 1 <= 400:
        mario_player_x = 400

    # Platform 6 (from bottom) Bottom Collision
    if (385 <= mario_player_y + 1 <= 395) and mario_player_x - 1 >= 100:
        mario_player_y = 385

    # Platform 6 (from bottom) Top Collision
    if (385 <= mario_player_y - 1 <= 415) and mario_player_x - 1 >= 100:
        mario_player_y = 415

    # Platform 6 (from bottom) Side Collision
    if (385 <= mario_player_y - 1 <= 405) and mario_player_x + 1 >= 100:
        mario_player_x = 100

    # Platform 7 (from bottom) Bottom Collision
    if (445 <= mario_player_y + 1 <= 460) and mario_player_x + 1 <= 400:
        mario_player_y = 445

    # Platform 7 (from bottom) Top Collision
    if (445 <= mario_player_y - 1 <= 475) and mario_player_x + 1 <= 400:
        mario_player_y = 475

    # Platform 7 (from bottom) Right Side Collision
    if (445 <= mario_player_y - 1 <= 465) and mario_player_x - 1 <= 400:
        mario_player_x = 400

    # Platform 8 (from bottom) Bottom Collision
    if (505 <= mario_player_y + 1 <= 520) and mario_player_x - 1 >= 100:
        mario_player_y = 505

    # Platform 8 (from bottom) Top Collision
    if (505 <= mario_player_y - 1 <= 535) and mario_player_x - 1 >= 100:
        mario_player_y = 535

    # Platform 8 (from bottom) Side Collision
    if (505 <= mario_player_y - 1 <= 525) and mario_player_x + 1 >= 100:
        mario_player_x = 100

    # Platform 9 (from bottom) Bottom Collision
    if (565 <= mario_player_y + 1 <= 575) and mario_player_x + 1 <= 400:
        mario_player_y = 565

    # Platform 9 (from bottom) Top Collision
    if (565 <= mario_player_y - 1 <= 595) and mario_player_x + 1 <= 400:
        mario_player_y = 595

    # Platform 9 (from bottom) Right Side Collision
    if (565 <= mario_player_y - 1 <= 585) and mario_player_x - 1 <= 400:
        mario_player_x = 400

    # Mario Ladder Collision

    # Collision Check (bottom floor - platform 1)
    if (167.5 <= mario_player_x <= 192.5) and (50 <= mario_player_y <= 110):
        mario_player_on_ladder = True

    # Off Check (bottom floor - platform 1)
    if (192.5 < mario_player_x) or (mario_player_x < 167.5):
        mario_player_on_ladder = False
        if 50 < mario_player_y < 110:
            mario_player_y = 55

    # Collision Check (platform 1 - platform 2)
    if (157.5 <= mario_player_x <= 382.5) and (110 <= mario_player_y <= 170):
        mario_player_on_ladder = True

    # Off Check (platform 1 - platform 2)
    if (382.5 < mario_player_x) or (mario_player_x < 157.5):
        mario_player_on_ladder = False
        if 115 < mario_player_y < 170:
            mario_player_y = 115

    # Mario Collision With Normal Barrels
    if mario_player_x - 5 <= donkey_kong_player_normal_barrel_x + 8 and mario_player_y - 5 <= \
            donkey_kong_player_normal_barrel_y + 8 and \
            mario_player_x + 5 >= donkey_kong_player_normal_barrel_x - 8 and mario_player_y + 5 >= \
            donkey_kong_player_normal_barrel_y - 8:
        mario_player_alive = False

    # Luigi Collision

    # Side Walls And Bottom Floor
    if luigi_player_x - 1 <= 50:
        luigi_player_x = 50
    if luigi_player_x + 1 >= 450:
        luigi_player_x = 450
    if luigi_player_y <= 55:
        luigi_player_y = 55

    # Platform 1 (from bottom) Bottom Collision
    if (85 <= luigi_player_y + 1 <= 105) and luigi_player_x + 1 <= 400:
        luigi_player_y = 85

    # Platform 1 (from bottom) Top Collision
    if (85 <= luigi_player_y - 1 <= 115) and luigi_player_x + 1 <= 400:
        luigi_player_y = 115

    # Platform 1 (from bottom) Right Side Collision
    if (85 <= luigi_player_y - 1 <= 110) and luigi_player_x - 1 <= 400:
        luigi_player_x = 400

    # Platform 2 (from bottom) Bottom Collision
    if (145 <= luigi_player_y + 1 <= 155) and luigi_player_x - 1 >= 100:
        luigi_player_y = 145

    # Platform 2 (from bottom) Top Collision
    if (150 <= luigi_player_y - 1 <= 175) and luigi_player_x - 1 >= 100:
        luigi_player_y = 175

    # Platform 2 (from bottom) Side Collision
    if (150 <= luigi_player_y - 1 <= 165) and luigi_player_x + 1 >= 100:
        luigi_player_x = 100

    # Platform 3 (from bottom) Bottom Collision
    if (205 <= luigi_player_y + 1 <= 215) and luigi_player_x + 1 <= 400:
        luigi_player_y = 205

    # Platform 3 (from bottom) Top Collision
    if (205 <= luigi_player_y - 1 <= 235) and luigi_player_x + 1 <= 400:
        luigi_player_y = 235

    # Platform 3 (from bottom) Right Side Collision
    if (205 <= luigi_player_y - 1 <= 220) and luigi_player_x - 1 <= 400:
        luigi_player_x = 400

    # Platform 4 (from bottom) Bottom Collision
    if (265 <= luigi_player_y + 1 <= 275) and luigi_player_x - 1 >= 100:
        luigi_player_y = 265

    # Platform 4 (from bottom) Top Collision
    if (265 <= luigi_player_y - 1 <= 295) and luigi_player_x - 1 >= 100:
        luigi_player_y = 295

    # Platform 4 (from bottom) Side Collision
    if (265 <= luigi_player_y - 1 <= 285) and luigi_player_x + 1 >= 100:
        luigi_player_x = 100

    # Platform 5 (from bottom) Bottom Collision
    if (325 <= luigi_player_y + 1 <= 340) and luigi_player_x + 1 <= 400:
        luigi_player_y = 325

    # Platform 5 (from bottom) Top Collision
    if (325 <= luigi_player_y - 1 <= 355) and luigi_player_x + 1 <= 400:
        luigi_player_y = 355

    # Platform 5 (from bottom) Right Side Collision
    if (325 <= luigi_player_y - 1 <= 350) and luigi_player_x - 1 <= 400:
        luigi_player_x = 400

    # Platform 6 (from bottom) Bottom Collision
    if (385 <= luigi_player_y + 1 <= 395) and luigi_player_x - 1 >= 100:
        luigi_player_y = 385

    # Platform 6 (from bottom) Top Collision
    if (385 <= luigi_player_y - 1 <= 415) and luigi_player_x - 1 >= 100:
        luigi_player_y = 415

    # Platform 6 (from bottom) Side Collision
    if (385 <= luigi_player_y - 1 <= 405) and luigi_player_x + 1 >= 100:
        luigi_player_x = 100

    # Platform 7 (from bottom) Bottom Collision
    if (445 <= luigi_player_y + 1 <= 460) and luigi_player_x + 1 <= 400:
        luigi_player_y = 445

    # Platform 7 (from bottom) Top Collision
    if (445 <= luigi_player_y - 1 <= 475) and luigi_player_x + 1 <= 400:
        luigi_player_y = 475

    # Platform 7 (from bottom) Right Side Collision
    if (445 <= luigi_player_y - 1 <= 465) and luigi_player_x - 1 <= 400:
        luigi_player_x = 400

    # Platform 8 (from bottom) Bottom Collision
    if (505 <= luigi_player_y + 1 <= 520) and luigi_player_x - 1 >= 100:
        luigi_player_y = 505

    # Platform 8 (from bottom) Top Collision
    if (505 <= luigi_player_y - 1 <= 535) and luigi_player_x - 1 >= 100:
        luigi_player_y = 535

    # Platform 8 (from bottom) Side Collision
    if (505 <= luigi_player_y - 1 <= 525) and luigi_player_x + 1 >= 100:
        luigi_player_x = 100

    # Platform 9 (from bottom) Bottom Collision
    if (565 <= luigi_player_y + 1 <= 575) and luigi_player_x + 1 <= 400:
        luigi_player_y = 565

    # Platform 9 (from bottom) Top Collision
    if (565 <= luigi_player_y - 1 <= 595) and luigi_player_x + 1 <= 400:
        luigi_player_y = 595

    # Platform 9 (from bottom) Right Side Collision
    if (565 <= luigi_player_y - 1 <= 585) and luigi_player_x - 1 <= 400:
        luigi_player_x = 400

    # Luigi Collision WIth Normal Barrels
    if luigi_player_x - 5 <= donkey_kong_player_normal_barrel_x + 8 and \
            luigi_player_y - 5 <= donkey_kong_player_normal_barrel_y + 8 and \
            luigi_player_x + 5 >= donkey_kong_player_normal_barrel_x - 8 and luigi_player_y + 5 >= \
            donkey_kong_player_normal_barrel_y - 8:
        luigi_player_alive = False

    # Barrel Collision
    if donkey_kong_player_normal_barrel_x >= 445:
        donkey_kong_player_normal_barrel_x = 445


def jump():
    """
    Jump for the players

    :return:
    """
    global mario_player_touching_platform, mario_player_x, mario_player_y, mario_player_gravity, \
        mario_player_is_jump, mario_player_jump_counter

    global player_jump_speed

    mario_player_touching_platform = False
    mario_player_is_jump = True

    if mario_player_is_jump and mario_player_jump_counter >= -5:
        mario_player_gravity = 1
        if mario_player_jump_counter < 0:
            mario_player_gravity = -1
        mario_player_y -= mario_player_jump_counter ** 2 * 0.5 * mario_player_gravity
        mario_player_jump_counter -= 1
        print(mario_player_y)
    else:
        mario_player_is_jump = False
        mario_player_jump_counter = 5


def win_condition():
    """
    The win condition must be fulfilled to win

    :return:
    """
    arcade.draw_rectangle_outline(200, 650, 100, 10, arcade.color.NEON_CARROT)


def on_key_press(key, modifiers):
    """
    Checking for key presses

    :param key:
    :param modifiers:
    :return:
    """
    global mario_player_up_pressed, mario_player_down_pressed, mario_player_right_pressed, mario_player_left_pressed, \
        mario_player_alive

    global luigi_player_up_pressed, luigi_player_down_pressed, luigi_player_right_pressed, luigi_player_left_pressed, \
        luigi_player_alive

    global donkey_kong_player_normal_barrel_pressed, donkey_kong_player_invisible_barrel_pressed, \
        donkey_kong_player_mario_ladder_barrel_pressed, donkey_kong_player_luigi_ladder_barrel_pressed, \
        donkey_kong_player_big_barrel_pressed, donkey_kong_player_small_barrel_pressed, donkey_kong_player_alive

    # Mario Controls
    if key == arcade.key.W and mario_player_alive:
        mario_player_up_pressed = True
    if key == arcade.key.D and mario_player_alive:
        mario_player_right_pressed = True
    if key == arcade.key.A and mario_player_alive:
        mario_player_left_pressed = True
    if key == arcade.key.S and mario_player_alive:
        mario_player_down_pressed = True

    # Luigi Controls
    if key == arcade.key.UP and luigi_player_alive:
        luigi_player_up_pressed = True
    if key == arcade.key.RIGHT and luigi_player_alive:
        luigi_player_right_pressed = True
    if key == arcade.key.LEFT and luigi_player_alive:
        luigi_player_left_pressed = True
    if key == arcade.key.DOWN and luigi_player_alive:
        luigi_player_down_pressed = True

    # Donkey Kong Controls
    if key == arcade.key.U:
        donkey_kong_player_normal_barrel_pressed = True
    if key == arcade.key.I:
        donkey_kong_player_mario_ladder_barrel_pressed = True
    if key == arcade.key.O:
        donkey_kong_player_luigi_ladder_barrel_pressed = True
    if key == arcade.key.J:
        donkey_kong_player_big_barrel_pressed = True
    if key == arcade.key.K:
        donkey_kong_player_small_barrel_pressed = True
    if key == arcade.key.L:
        donkey_kong_player_invisible_barrel_pressed = True

    player()


def on_key_release(key, modifiers):
    """
    Checking for key releases

    :param key:
    :param modifiers:
    :return:
    """
    global mario_player_up_pressed, mario_player_down_pressed, mario_player_left_pressed, mario_player_right_pressed

    global luigi_player_up_pressed, luigi_player_down_pressed, luigi_player_left_pressed, luigi_player_right_pressed

    global donkey_kong_player_normal_barrel_pressed, donkey_kong_player_mario_ladder_barrel_pressed, \
        donkey_kong_player_luigi_ladder_barrel_pressed, donkey_kong_player_big_barrel_pressed, \
        donkey_kong_player_small_barrel_pressed, donkey_kong_player_invisible_barrel_pressed

    global velocity

    # To Stop Mario's Controls When The Player Lets Go Of The Key
    if key == arcade.key.W:
        mario_player_up_pressed = False
    if key == arcade.key.D:
        mario_player_right_pressed = False
        velocity = 0
    if key == arcade.key.A:
        mario_player_left_pressed = False
        velocity = 0
    if key == arcade.key.S:
        mario_player_down_pressed = False

    # To Stop Luigi's Controls When The Player Lets Go Of The Key
    if key == arcade.key.UP:
        luigi_player_up_pressed = False
    if key == arcade.key.RIGHT:
        luigi_player_right_pressed = False
    if key == arcade.key.LEFT:
        luigi_player_left_pressed = False
    if key == arcade.key.DOWN:
        luigi_player_down_pressed = False

    # To Stop Donkey Kong's Controls When The Player Lets Go Of The Key
    if key == arcade.key.U:
        donkey_kong_player_normal_barrel_pressed = False
    if key == arcade.key.I:
        donkey_kong_player_mario_ladder_barrel_pressed = False
    if key == arcade.key.O:
        donkey_kong_player_luigi_ladder_barrel_pressed = False
    if key == arcade.key.J:
        donkey_kong_player_big_barrel_pressed = False
    if key == arcade.key.K:
        donkey_kong_player_small_barrel_pressed = False
    if key == arcade.key.L:
        donkey_kong_player_invisible_barrel_pressed = True


def setup():
    """
    The final setup before the code is run

    :return:
    """

    arcade.open_window(screen_width, screen_height, screen_title)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


setup()
