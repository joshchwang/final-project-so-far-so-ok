import arcade
import random

# Screen Variables
screen_width = 1000
screen_height = 600
screen_title = "Pong"

# Player 1 Variables
player_1_x = 50
player_1_y = 250
player_1_up_pressed = False
player_1_down_pressed = False

# Player 2 Variables
player_2_x = 950
player_2_y = 250
player_2_up_pressed = False
player_2_down_pressed = False

# Ball Variables

# If ball type is 1 its for player 1. 2 is for player 2.
ball_type = random.randint(1, 2)

ball_x = 500
ball_y = 250

# Velocity increases after hit
ball_velocity = 1

if ball_type == 1:
    ball_x = 250
else:
    ball_x = 750


def on_update(delta_time):
    global player_1_up_pressed, player_1_down_pressed, player_1_y

    global player_2_up_pressed, player_2_down_pressed, player_2_y

    global ball_x, ball_y

    # Player 1 Movement
    if player_1_up_pressed and player_1_y + 50 <= 490:
        player_1_y += 5
    if player_1_down_pressed and player_1_y - 50 >= 0:
        player_1_y -= 5

    # Player 2 Movement
    if player_2_up_pressed and player_2_y + 50 <= 490:
        player_2_y += 5
    if player_2_down_pressed and player_2_y - 50 >= 0:
        player_2_y -= 5

    ball_x -= 1
    ball_y += 1


def on_draw():
    arcade.start_render()

    # Player 1
    arcade.draw_rectangle_outline(player_1_x, player_1_y, 10, 100, arcade.color.WHITE)

    # Player 2
    arcade.draw_rectangle_outline(player_2_x, player_2_y, 10, 100, arcade.color.WHITE)

    # Ball
    arcade.draw_rectangle_outline(ball_x, ball_y, 10, 10, arcade.color.WHITE)

    # Top Divider
    arcade.draw_rectangle_outline(500, 500, 1000, 10, arcade.color.WHITE)

    # Player 1 Text -------------------------- Replace string condition with variable for ability to choose name
    arcade.draw_text("Player 1", 10, 580, arcade.color.CANDY_APPLE_RED, 12)

    # Player 2 Text -------------------------- Replace string condition with variable for ability to choose name
    arcade.draw_text("Player 2", 940, 580, arcade.color.APPLE_GREEN, 12)


def on_key_press(key, modifiers):
    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    # Player 1 Key Input
    if key == arcade.key.W:
        player_1_up_pressed = True
    if key == arcade.key.S:
        player_1_down_pressed = True

    # Player 2 Key Input
    if key == arcade.key.UP:
        player_2_up_pressed = True
    if key == arcade.key.DOWN:
        player_2_down_pressed = True


def on_key_release(key, modifiers):
    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    # Player 1 Key Output
    if key == arcade.key.W:
        player_1_up_pressed = False
    if key == arcade.key.S:
        player_1_down_pressed = False

    # Player 2 Key Output
    if key == arcade.key.UP:
        player_2_up_pressed = False
    if key == arcade.key.DOWN:
        player_2_down_pressed = False


def collision():
    global player_1_x, player_1_y

    global player_2_x, player_2_y

    global ball_x, ball_y

    # Ball Collision With


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
