import arcade
import random

# Screen Variables
screen_width = 500
screen_height = 700
screen_title = "Donkey Kong"

# Physic Variables
gravity = 5
player_movement_speed = 5
player_jump_speed = 0.01
normal_barrel_movement_speed = 7
ladder_barrel_movement_speed = 7

# Player Variables
player_x = 50
player_y = 55
player_up_pressed = False
player_down_pressed = False
player_left_pressed = False
player_right_pressed = False
player_on_ladder = False
touching_platform = True

# Game Aspect Variables
lives = 3
points_score = 0


def on_update(delta_time):
    global player_up_pressed, player_down_pressed, player_left_pressed, player_right_pressed, player_y, player_x, touching_platform
    if player_up_pressed and touching_platform or player_up_pressed and player_on_ladder:
        player_y += 2
    if player_down_pressed:
        player_y -= 2
    if player_right_pressed:
        player_x += 2
    if player_left_pressed:
        player_x -= 2

    collision()


def normal_barrel():
    arcade.draw_rectangle_outline(50, 595, 10, 10, arcade.color.FRENCH_BEIGE)


def ladder_barrel():
    pass


def ladder():
    pass


def jump():
    global touching_platform, player_x, player_y, player_jump_speed, gravity
    touching_platform = False


def collision():
    global player_x, player_y

    # Collision for the two walls and the bottom floor
    if player_x - 1 <= 50:
        player_x = 50
    if player_x + 1 >= 450:
        player_x = 450
    if player_y <= 55:
        player_y = 55

    # Platform 1 (from bottom) Bottom Collision
    if (85 <= player_y + 1 <= 105) and player_x + 1 <= 400:
        player_y = 85

    # Platform 1 (from bottom) Top Collision
    if (85 <= player_y - 1 <= 115) and player_x + 1 <= 400:
        player_y = 115

    # Platform 1 (from bottom) Right Side Collision
    if (85 <= player_y - 1 <= 110) and player_x - 1 <= 400:
        player_x = 400

    # Platform 2 (from bottom) Bottom Collision
    if (145 <= player_y + 1 <= 155) and player_x - 1 >= 100:
        player_y = 145

    # Platform 2 (from bottom) Top Collision
    if (150 <= player_y - 1 <= 175) and player_x - 1 >= 100:
        player_y = 175

    # Platform 2 (from bottom) Side Collision
    if (150 <= player_y - 1 <= 165) and player_x + 1 >= 100:
        player_x = 100

    # Platform 3 (from bottom) Bottom Collision
    if (205 <= player_y + 1 <= 215) and player_x + 1 <= 400:
        player_y = 205

    # Platform 3 (from bottom) Top Collision
    if (205 <= player_y - 1 <= 235) and player_x + 1 <= 400:
        player_y = 235

    # Platform 3 (from bottom) Right Side Collision
    if (205 <= player_y - 1 <= 220) and player_x - 1 <= 400:
        player_x = 400

    # Platform 4 (from bottom) Bottom Collision
    if (265 <= player_y + 1 <= 275) and player_x - 1 >= 100:
        player_y = 265

    # Platform 4 (from bottom) Top Collision
    if (265 <= player_y - 1 <= 295) and player_x - 1 >= 100:
        player_y = 295

    # Platform 4 (from bottom) Side Collision
    if (265 <= player_y - 1 <= 285) and player_x + 1 >= 100:
        player_x = 100

    # Platform 5 (from bottom) Bottom Collision
    if (325 <= player_y + 1 <= 340) and player_x + 1 <= 400:
        player_y = 325

    # Platform 5 (from bottom) Top Collision
    if (325 <= player_y - 1 <= 355) and player_x + 1 <= 400:
        player_y = 355

    # Platform 5 (from bottom) Right Side Collision
    if (325 <= player_y - 1 <= 350) and player_x - 1 <= 400:
        player_x = 400

    # Platform 6 (from bottom) Bottom Collision
    if (385 <= player_y + 1 <= 395) and player_x - 1 >= 100:
        player_y = 385

    # Platform 6 (from bottom) Top Collision
    if (385 <= player_y - 1 <= 415) and player_x - 1 >= 100:
        player_y = 415

    # Platform 6 (from bottom) Side Collision
    if (385 <= player_y - 1 <= 405) and player_x + 1 >= 100:
        player_x = 100

    # Platform 7 (from bottom) Bottom Collision
    if (445 <= player_y + 1 <= 460) and player_x + 1 <= 400:
        player_y = 445

    # Platform 7 (from bottom) Top Collision
    if (445 <= player_y - 1 <= 475) and player_x + 1 <= 400:
        player_y = 475

    # Platform 7 (from bottom) Right Side Collision
    if (445 <= player_y - 1 <= 465) and player_x - 1 <= 400:
        player_x = 400

    # Platform 8 (from bottom) Bottom Collision
    if (505 <= player_y + 1 <= 520) and player_x - 1 >= 100:
        player_y = 505

    # Platform 8 (from bottom) Top Collision
    if (505 <= player_y - 1 <= 535) and player_x - 1 >= 100:
        player_y = 535

    # Platform 8 (from bottom) Side Collision
    if (505 <= player_y - 1 <= 525) and player_x + 1 >= 100:
        player_x = 100

    # Platform 9 (from bottom) Bottom Collision
    if (565 <= player_y + 1 <= 575) and player_x + 1 <= 400:
        player_y = 565

    # Platform 9 (from bottom) Top Collision
    if (565 <= player_y - 1 <= 595) and player_x + 1 <= 400:
        player_y = 595

    # Platform 9 (from bottom) Right Side Collision
    if (565 <= player_y - 1 <= 585) and player_x - 1 <= 400:
        player_x = 400


def donkey_kong():
    pass


def win_condition():
    pass


def on_draw():
    global player_x, player_y
    arcade.start_render()

    # The player
    arcade.draw_rectangle_outline(player_x, player_y, 10, 10, arcade.color.WHITE)

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

    normal_barrel()


def on_key_press(key, modifiers):
    global player_up_pressed, player_down_pressed, player_right_pressed, player_left_pressed

    # Player Controls
    if key == arcade.key.UP or key == arcade.key.W:
        player_up_pressed = True
    if key == arcade.key.RIGHT or key == arcade.key.D:
        player_right_pressed = True
    if key == arcade.key.LEFT or key == arcade.key.A:
        player_left_pressed = True
    if key == arcade.key.DOWN or key == arcade.key.S:
        player_down_pressed = True


def on_key_release(key, modifiers):
    global player_up_pressed, player_down_pressed, player_left_pressed, player_right_pressed, player_x, player_y

    # To Stop Player Controls When They Let Go Of The Key
    if key == arcade.key.UP or key == arcade.key.W:
        player_up_pressed = False
    if key == arcade.key.RIGHT or key == arcade.key.D:
        player_right_pressed = False
    if key == arcade.key.LEFT or key == arcade.key.A:
        player_left_pressed = False
    if key == arcade.key.DOWN or arcade.key.S:
        player_down_pressed = False


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
