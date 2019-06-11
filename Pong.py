import arcade
import random

# Screen Variables
screen_width = 1000
screen_height = 600
screen_title = "Pong"

# States
start_screen = 0
instructions_screen = 1
game_1_player_ai_screen = 2      # ------------- 1 player
game_2_player_screen = 3       # --------------- 2 player
game_survival = 4   # -------------------- 2 or 1 player
game_endless = 5   # --------------- endless is 1 player
game_over_screen = 6   # -------------- game over screen
screens_list = [start_screen, instructions_screen,
                game_1_player_ai_screen, game_2_player_screen,
                game_survival, game_endless, game_over_screen]

# States Booleans
start_screen_ = True

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

# Ai Variables
is_ai = True
ai_x = 950
ai_y = 250
ai_up = False
ai_down = False

# Ball Variables
ball_x = 500
ball_y = 250

# If ball type is False or 1 its for player 1. 2 or True is for player 2.
if random.randint(0, 1) == 1:
    ball_type = False
else:
    ball_type = True

# Ball Starting Condition
if ball_type:
    ball_x = 250
else:
    ball_x = 750

# Velocity increases after hit
ball_velocity = 1
ball_velocity_check = False

# Determines the bouncing
ball_bounce_down = False
ball_bounce_up = True

# Score
score_player_1 = 9
score_player_2 = 9
score_ai = 9
score_endless = 0
score_lives_player_1 = 0
score_lives_player_2 = 0

# Dotted Line Position List
rectangle_list = [8, 24, 40, 56, 72, 88, 104,
                  120, 136, 152, 166, 182, 198,
                  214, 230, 246, 262, 278, 294,
                  310, 326, 342, 358, 374, 390,
                  406, 422, 438, 454, 470, 486]


def on_update(delta_time):
    global player_1_up_pressed, player_1_down_pressed, player_1_y

    global player_2_up_pressed, player_2_down_pressed, player_2_y

    global ball_x, ball_y, ball_bounce_up, ball_bounce_down, ball_type, ball_velocity, ball_velocity_check

    global score_player_1, score_player_2, score_lives_player_1, score_lives_player_2, score_endless

    global is_ai, ai_x, ai_y

    global start_screen

    # Player 1 Movement
    if player_1_up_pressed and player_1_y + 50 <= 490:
        player_1_y += 5
    if player_1_down_pressed and player_1_y - 50 >= 0:
        player_1_y -= 5

    # Player 2 Movement
    if player_2_up_pressed and player_2_y + 50 <= 490 and not is_ai:
        player_2_y += 5
    if player_2_down_pressed and player_2_y - 50 >= 0 and not is_ai:
        player_2_y -= 5

    if ai_y + 50 <= 490 and is_ai:
        pass
    if ai_y - 59 >= 0 and is_ai:
        pass

    # Ball Bouncing off of the Divider and the Bottom
    if ball_bounce_up:
        ball_y += 5 + ball_velocity
    if ball_bounce_down:
        ball_y -= 5 + ball_velocity

    # Ball Bouncing off of the Players
    if ball_type:
        ball_x += 5 + ball_velocity
    if not ball_type:
        ball_x -= 5 + ball_velocity

    # Increasing Ball Velocity
    if ball_velocity_check:
        ball_velocity_check += 1
        ball_velocity_check = False

    # Check if the Ball Bounces Off Screen Player 1
    if ball_x < 0:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_player_2 += 1

    # Checking if the Ball Bounces Off Screen Player 2
    if ball_x > 1000:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity = 1
        score_player_1 += 1

    collision()


def on_draw():
    global rectangle_list

    global ball_y

    global is_ai, ai_x, ai_y

    arcade.start_render()

    # Player 1
    arcade.draw_rectangle_outline(player_1_x, player_1_y, 10, 100, arcade.color.WHITE)

    if not is_ai:
        # Player 2
        arcade.draw_rectangle_outline(player_2_x, player_2_y, 10, 100, arcade.color.WHITE)

    if is_ai:
        # AI
        arcade.draw_rectangle_outline(ai_x, ball_y, 10, 100, arcade.color.RED)
        ai_y = ball_y

    # Ball
    arcade.draw_rectangle_outline(ball_x, ball_y, 10, 10, arcade.color.WHITE)

    # Divider
    arcade.draw_rectangle_outline(500, 500, 1000, 10, arcade.color.WHITE)

    # Dotted Line
    for i in rectangle_list:
        arcade.draw_rectangle_outline(500, i, 10, 15, arcade.color.WHITE)

    # Player 1 Text -------------------------- Replace string condition with variable for ability to choose name
    arcade.draw_text("Player 1", 10, 580, arcade.color.WHITE, 12)

    if not is_ai:
        # Player 2 Text -------------------------- Replace string condition with variable for ability to choose name
        arcade.draw_text("Player 2", 940, 580, arcade.color.WHITE, 12)

    if is_ai:
        # AI Text
        arcade.draw_text("AI", 980, 580, arcade.color.RED, 12)

    # Player 1 Score
    if score_player_1 < 10:
        arcade.draw_text(str(score_player_1), 430, 525, arcade.color.WHITE, 70)

    if score_player_1 >= 10:
        arcade.draw_text(str(score_player_1), 380, 525, arcade.color.WHITE, 70)

    if not is_ai:
        # Player 2 Score
        arcade.draw_text(str(score_player_2), 520, 525, arcade.color.WHITE, 70)

    if is_ai:
        # AI
        arcade.draw_text(str(score_ai), 520, 525, arcade.color.RED, 70)

    # Colon
    arcade.draw_rectangle_filled(500, 570, 10, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(500, 540, 10, 10, arcade.color.WHITE)


def on_key_press(key, modifiers):
    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    global is_ai

    # Player 1 Key Input
    if key == arcade.key.W:
        player_1_up_pressed = True
    if key == arcade.key.S:
        player_1_down_pressed = True

    # Player 2 Key Input
    if key == arcade.key.UP and not is_ai:
        player_2_up_pressed = True
    if key == arcade.key.DOWN and not is_ai:
        player_2_down_pressed = True


def on_key_release(key, modifiers):
    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    global is_ai

    # Player 1 Key Output
    if key == arcade.key.W:
        player_1_up_pressed = False
    if key == arcade.key.S:
        player_1_down_pressed = False

    # Player 2 Key Output
    if key == arcade.key.UP and not is_ai:
        player_2_up_pressed = False
    if key == arcade.key.DOWN and not is_ai:
        player_2_down_pressed = False


def collision():
    global player_1_x, player_1_y

    global player_2_x, player_2_y

    global ball_x, ball_y, ball_bounce_up, ball_bounce_down, ball_type, ball_velocity, ball_velocity_check

    global is_ai, ai_x, ai_y

    # Ball Collision With Divider
    if ball_y + 1 > 490:
        ball_y = 490
        ball_bounce_up = False
        ball_bounce_down = True

    # Ball Collision With Bottom Of Screen
    if ball_y - 1 < 5:
        ball_y = 5
        ball_bounce_down = False
        ball_bounce_up = True

    # Ball Collision With Player 1
    if (player_1_x - 10 <= ball_x <= player_1_x + 10) and (player_1_y - 50 <= ball_y <= player_1_y):
        ball_type = True
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 1

    if (player_1_x - 10 <= ball_x - 1 < player_1_x + 10) and (player_1_y <= ball_y <= player_1_y + 50) :
        ball_type = True
        ball_bounce_down = False
        ball_bounce_up = True
        ball_velocity_check = True
        ball_velocity += 1

    # Ball Collision With Player 2
    if (player_2_x - 10 <= ball_x + 1 <= player_2_x + 10) and (player_2_y - 50 <= ball_y <= player_2_y) and not is_ai:
        ball_type = False
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 1

    if (player_2_x - 10 <= ball_x + 1 <= player_2_x + 10) and (player_2_y <= ball_y <= player_2_y + 50) and not is_ai:
        ball_type = False
        ball_bounce_up = True
        ball_bounce_down = False
        ball_velocity_check = True
        ball_velocity += 1

    # Ball Collision With AI
    if (ai_x - 10 <= ball_x + 1 <= ai_x + 10) and (ai_y - 50 <= ball_y <= ai_y) and is_ai:
        ball_type = False
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 1

    if (ai_x - 10 <= ball_x + 1 <= ai_x + 10) and (ai_y <= ball_y <= ai_y + 50) and is_ai:
        ball_type = False
        ball_bounce_up = True
        ball_bounce_down = False
        ball_velocity_check = True
        ball_velocity += 1


def start_screen():

    arcade.draw_rectangle_outline(500, 300, 1000, 600, arcade.color.RED)



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
