import arcade
import random

# Screen Variables
screen_width = 500
screen_height = 700
screen_title = "Donkey Kong"

# Physic Variables
gravity = 5
velocity = 0.1
player_movement_speed = 5
player_jump_speed = 0.01
normal_barrel_movement_speed = 7
ladder_barrel_movement_speed = 7

# Player Variables
mario_player_x = 50
mario_player_y = 55
mario_player_up_pressed = False
mario_player_down_pressed = False
mario_player_left_pressed = False
mario_player_right_pressed = False
mario_player_on_ladder = False
mario_player_touching_platform = True

# Normal Barrel Variables
normal_barrel_x = 50
normal_barrel_y = 595

# Game Aspect Variables
mario_player_lives = 3
total_points_score = 0
mario_player_alive = True


def on_update(delta_time):
    global mario_player_up_pressed, mario_player_down_pressed, mario_player_left_pressed, mario_player_right_pressed, mario_player_y, mario_player_x, mario_player_touching_platform
    if mario_player_up_pressed and mario_player_touching_platform or mario_player_up_pressed and mario_player_on_ladder:
        mario_player_y += 2
    if mario_player_down_pressed:
        mario_player_y -= 2
    if mario_player_right_pressed:
        mario_player_x += 2
    if mario_player_left_pressed:
        mario_player_x -= 2

    collision()


def normal_barrel():
    arcade.draw_rectangle_outline(50, 595, 10, 10, arcade.color.FRENCH_BEIGE)


def ladder_barrel():
    pass


def ladder():
    pass


def jump():
    global mario_player_touching_platform, mario_player_x, mario_player_y, player_jump_speed, gravity
    mario_player_touching_platform = False


def collision():
    global mario_player_x, mario_player_y, mario_player_alive, normal_barrel_x, normal_barrel_y

    # Collision for the two walls and the bottom floor
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

    # Player Collision With Normal Barrels
    if mario_player_x - 5 <= normal_barrel_x + 5 and mario_player_y - 5 <= normal_barrel_y + 5 and \
            mario_player_x + 5 >= normal_barrel_x - 5 and mario_player_y + 5 >= normal_barrel_y - 5:
        mario_player_alive = False


def donkey_kong():
    pass


def win_condition():
    pass


def player():
    global mario_player_x, mario_player_y, mario_player_alive, normal_barrel_x, normal_barrel_y
    # The player
    arcade.draw_rectangle_outline(mario_player_x, mario_player_y, 10, 10, arcade.color.RED)

    # Player State
    if not mario_player_alive:
        mario_player_x = mario_player_x
        mario_player_y = mario_player_y


def on_draw():
    global mario_player_x, mario_player_y
    arcade.start_render()

    # Left and Right Walls
    arcade.draw_rectangle_outline(20, screen_height / 2, 50, 700, arcade.color.RUSTY_RED)
    arcade.draw_rectangle_outline(480, screen_height / 2, 50, 700, arcade.color.RUSTY_RED)
    # Bottom Floor
    arcade.draw_rectangle_outline(screen_width / 2, 25, 500, 50, arcade.color.RUSTY_RED)

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

    player()

    normal_barrel()


def on_key_press(key, modifiers):
    global mario_player_up_pressed, mario_player_down_pressed, mario_player_right_pressed, mario_player_left_pressed, mario_player_alive

    # Player Controls
    if key == arcade.key.UP and mario_player_alive or key == arcade.key.W and mario_player_alive:
        mario_player_up_pressed = True
    if key == arcade.key.RIGHT and mario_player_alive or key == arcade.key.D and mario_player_alive:
        mario_player_right_pressed = True
    if key == arcade.key.LEFT and mario_player_alive or key == arcade.key.A and mario_player_alive:
        mario_player_left_pressed = True
    if key == arcade.key.DOWN and mario_player_alive or key == arcade.key.S and mario_player_alive:
        mario_player_down_pressed = True


def on_key_release(key, modifiers):
    global mario_player_up_pressed, mario_player_down_pressed, mario_player_left_pressed, mario_player_right_pressed, mario_player_x, mario_player_y

    # To Stop Player Controls When They Let Go Of The Key
    if key == arcade.key.UP or key == arcade.key.W:
        mario_player_up_pressed = False
    if key == arcade.key.RIGHT or key == arcade.key.D:
        mario_player_right_pressed = False
    if key == arcade.key.LEFT or key == arcade.key.A:
        mario_player_left_pressed = False
    if key == arcade.key.DOWN or arcade.key.S:
        mario_player_down_pressed = False


def setup():

    arcade.open_window(screen_width, screen_height, screen_title)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


setup()
