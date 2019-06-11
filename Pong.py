import arcade
import random

# Screen variables
screen_width = 1000
screen_height = 600
screen_title = "Pong"

# States
current_screen = 3
# Current screen value determines what screen the game will go into
# 0 is start screen
# 1 is mode screen
# 2 is how to play (instruction screen)
# 3 is instruction screen
# 4 is 2 player mode
# 5 is 1 player mode against ai
# 6 is survival mode (2 players)
# 7 is survival mode (1 player against ai)
# 8 is endless mode
# 9 is game over screen

# States booleans
# WORK IN PROGRESS -----------------------------------------------------------------------------------------------

# Player 1 variables
player_1_x = 50
player_1_y = 250
player_1_up_pressed = False
player_1_down_pressed = False

# Player 2 variables
player_2_x = 950
player_2_y = 250
player_2_up_pressed = False
player_2_down_pressed = False

# Ai variables
is_ai = True
ai_x = 950
ai_y = 250
ai_up = False
ai_down = False

# Ball variables
ball_x = 500
ball_y = 250

# If ball type is False or 1 its for player 1. 2 or True is for player 2.
if random.randint(0, 1) == 1:
    ball_type = False
else:
    ball_type = True

# Ball starting condition
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
score_player_1 = 0
score_player_2 = 0
score_ai = 0
score_endless = 0
score_lives_player_1 = 0
score_lives_player_2 = 0
score_cap_player_1 = 5
score_cap_player_2 = 5
score_cap_ai = 5

# To change the score from 10 to 100 smoothly
shift_pos = 0

# Dotted line position list
rectangle_list = [8, 24, 40, 56, 72, 88, 104,
                  120, 136, 152, 166, 182, 198,
                  214, 230, 246, 262, 278, 294,
                  310, 326, 342, 358, 374, 390,
                  406, 422, 438, 454, 470, 486]

# Button lists


def on_update(delta_time):
    global player_1_up_pressed, player_1_down_pressed, player_1_y

    global player_2_up_pressed, player_2_down_pressed, player_2_y

    global ball_x, ball_y, ball_bounce_up, ball_bounce_down, ball_type, ball_velocity, ball_velocity_check

    global score_player_1, score_player_2, score_ai, score_lives_player_1, score_lives_player_2, score_endless

    global is_ai, ai_x, ai_y

    # Player 1 movement
    if player_1_up_pressed and player_1_y + 50 <= 490:
        player_1_y += 5
    if player_1_down_pressed and player_1_y - 50 >= 0:
        player_1_y -= 5

    # Player 2 movement
    if player_2_up_pressed and player_2_y + 50 <= 490 and not is_ai:
        player_2_y += 5
    if player_2_down_pressed and player_2_y - 50 >= 0 and not is_ai:
        player_2_y -= 5

    if ai_y + 50 >= 500 and is_ai:
        ai_y = 445
    if ai_y - 50 <= 0 and is_ai:
        ai_y = 50

    # Ball bouncing off of the divider and the bottom
    if ball_bounce_up:
        ball_y += 5 + ball_velocity
    if ball_bounce_down:
        ball_y -= 5 + ball_velocity

    # Ball bouncing off of the players
    if ball_type:
        ball_x += 5 + ball_velocity
    if not ball_type:
        ball_x -= 5 + ball_velocity

    # Increasing ball velocity
    if ball_velocity_check:
        ball_velocity_check += 1
        ball_velocity_check = False

    # Check if the ball bounces off screen player 1
    if ball_x < 0 and not is_ai:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_player_2 += 1

    # Checking if the ball bounces off screen player 2
    if ball_x > 1000 and not is_ai:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity = 1
        score_player_1 += 1

    # Checking if the ball bounces off screen player 1
    if ball_x < 0 and is_ai:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_ai += 1

    # Checking if the ball bounces off screen AI
    if ball_x > 1000 and is_ai:
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

    global shift_pos, current_screen

    arcade.start_render()

    if current_screen == 0:
        start_screen()

    if current_screen == 1:
        mode_screen()

    if current_screen == 2:
        how_to_play_screen()

    if current_screen == 3:
        instruction_screen()

    if current_screen == 4:
        # Player 1
        arcade.draw_rectangle_outline(player_1_x, player_1_y, 10, 100, arcade.color.WHITE)

        if not is_ai:
            # Player 2
            arcade.draw_rectangle_outline(player_2_x, player_2_y, 10, 100, arcade.color.WHITE)

        if is_ai and 400 <= ball_x:
            # AI
            arcade.draw_rectangle_outline(ai_x, ai_y, 10, 100, arcade.color.RED)
            ai()

        if is_ai and 500 > ball_x:
            arcade.draw_rectangle_outline(ai_x, ai_y, 10, 100, arcade.color.RED)

        # Ball
        arcade.draw_rectangle_outline(ball_x, ball_y, 10, 10, arcade.color.WHITE)

        # Divider
        arcade.draw_rectangle_outline(500, 500, 1000, 10, arcade.color.WHITE)

        # Dotted line
        for i in rectangle_list:
            arcade.draw_rectangle_outline(500, i, 10, 15, arcade.color.WHITE)

        # Player 1 text -------------------------- Replace string condition with variable for ability to choose name
        arcade.draw_text("Player 1", 10, 580, arcade.color.WHITE, 12)

        if not is_ai:
            # Player 2 text -------------------------- Replace string condition with variable for ability to choose name
            arcade.draw_text("Player 2", 940, 580, arcade.color.WHITE, 12)

        if is_ai:
            # AI text
            arcade.draw_text("AI", 980, 580, arcade.color.RED, 12)

        # Player 1 score
        if score_player_1 < 10:
            arcade.draw_text(str(score_player_1), 430, 525, arcade.color.WHITE, 70)

        if score_player_1 >= 100:
            arcade.draw_text(str(score_player_1), 330, 525, arcade.color.WHITE, 70)
            shift_pos = 50

        if score_player_1 >= 10:
            arcade.draw_text(str(score_player_1), 380 - shift_pos, 525, arcade.color.WHITE, 70)

        if not is_ai:
            # Player 2 Sc==score
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

    # Player 1 key input
    if key == arcade.key.W:
        player_1_up_pressed = True
    if key == arcade.key.S:
        player_1_down_pressed = True

    # Player 2 key input
    if key == arcade.key.UP and not is_ai:
        player_2_up_pressed = True
    if key == arcade.key.DOWN and not is_ai:
        player_2_down_pressed = True


def on_key_release(key, modifiers):
    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    global is_ai

    # Player 1 key output
    if key == arcade.key.W:
        player_1_up_pressed = False
    if key == arcade.key.S:
        player_1_down_pressed = False

    # Player 2 key output
    if key == arcade.key.UP and not is_ai:
        player_2_up_pressed = False
    if key == arcade.key.DOWN and not is_ai:
        player_2_down_pressed = False


def on_mouse_press(x, y, button, modifiers):
    global current_screen

    # if current_screen == 0:


def collision():
    global player_1_x, player_1_y

    global player_2_x, player_2_y

    global ball_x, ball_y, ball_bounce_up, ball_bounce_down, ball_type, ball_velocity, ball_velocity_check

    global is_ai, ai_x, ai_y

    # Ball collision with divider
    if ball_y + 1 > 490:
        ball_y = 490
        ball_bounce_up = False
        ball_bounce_down = True

    # Ball collision with bottom of screen
    if ball_y - 1 < 5:
        ball_y = 5
        ball_bounce_down = False
        ball_bounce_up = True

    # Ball collision with player 1
    if (player_1_x - 10 <= ball_x <= player_1_x + 10) and (player_1_y - 50 <= ball_y <= player_1_y):
        ball_type = True
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 1

    if (player_1_x - 10 <= ball_x - 1 < player_1_x + 10) and (player_1_y <= ball_y <= player_1_y + 50):
        ball_type = True
        ball_bounce_down = False
        ball_bounce_up = True
        ball_velocity_check = True
        ball_velocity += 1

    # Ball collision with player 2
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

    # Ball collision with AI
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


def ai():

    global ai_y, ball_y

    if ball_y >= ai_y:
        ai_y += 15

    if ball_y <= ai_y:
        ai_y -= 5


# def score_caps(score_1, score_2, condition):
    # global score_cap_player_1, score_cap_player_2, score_cap_ai

    # if score_1 == score_cap_player_1:
        # return 1

    # if score_2 == score_cap_player_2 and not condition:
        # return 2

    # if score_2 == score_cap_ai and condition:
        # return 3


def start_screen():
    arcade.draw_text("P O N G", 300, 500, arcade.color.PURPLE_MOUNTAIN_MAJESTY, 100)

    arcade.draw_rectangle_outline(510, 320, 200, 100, arcade.color.TURQUOISE)
    arcade.draw_text("S T A R T", 420, 300, arcade.color.TURQUOISE, 40)


def mode_screen():
    # 2 player mode
    arcade.draw_rectangle_outline(170, 480, 300, 200, arcade.color.WHITE)
    arcade.draw_text("2 Players", 140, 480, arcade.color.WHITE)

    # 1 player mode
    arcade.draw_rectangle_outline(170, 260, 300, 200, arcade.color.RED)
    arcade.draw_text("1 Player", 140, 260, arcade.color.RED)

    # Normal mode
    arcade.draw_rectangle_outline(880, 530, 200, 100, arcade.color.ORANGE)
    arcade.draw_text("Normal Mode", 805, 520, arcade.color.ORANGE, 20)

    # Survival mode
    arcade.draw_rectangle_outline(660, 530, 200, 100, arcade.color.BLUE)
    arcade.draw_text("Survival Mode", 585, 520, arcade.color.BLUE, 20)

    # Endless mode
    arcade.draw_rectangle_outline(880, 410, 200, 100, arcade.color.YELLOW)
    arcade.draw_text("Endless Mode", 805, 400, arcade.color.YELLOW, 20)

    # How to play button
    arcade.draw_rectangle_outline(900, 70, 150, 100, arcade.color.PURPLE)
    arcade.draw_text("HOW TO", 855, 75, arcade.color.PURPLE, 20)
    arcade.draw_text("PLAY", 875, 50, arcade.color.PURPLE, 20)

    # Back button
    arcade.draw_rectangle_outline(100, 70, 150, 100, arcade.color.GREEN)
    arcade.draw_text("BACK", 55, 60, arcade.color.GREEN, 30)


def how_to_play_screen():
    arcade.draw_text("HOW TO PLAY", 100, 500, arcade.color.BRONZE, 100)

    arcade.draw_text("Player 1:", 100, 430, arcade.color.PINK, 20)

    arcade.draw_text("Use the 'W' key to move up", 100, 400, arcade.color.PINK, 20)
    arcade.draw_text("Use the 'S' key to move down", 100, 370, arcade.color.PINK, 20)

    arcade.draw_text("Player 2:", 500, 430, arcade.color.PURPLE, 20)

    arcade.draw_text("Use the up arrow to move up", 500, 400, arcade.color.PURPLE, 20)
    arcade.draw_text("Use the down arrow to move down", 500, 370, arcade.color.PURPLE, 20)

    # Back button
    arcade.draw_rectangle_outline(100, 70, 150, 100, arcade.color.GREEN)
    arcade.draw_text("BACK", 55, 60, arcade.color.GREEN, 30)

    # Next button
    arcade.draw_rectangle_outline(900, 70, 150, 100, arcade.color.BLUE)
    arcade.draw_text("NEXT", 855, 60, arcade.color.BLUE, 30)


def instruction_screen():
    arcade.draw_text("THE DIFFERENT MODES", 50, 500, arcade.color.BRONZE, 70)
    arcade.draw_text("1 Player Mode:", 50, 430, arcade.color.PINK, 20)

    arcade.draw_text("This mode pits the", 50, 400, arcade.color.PINK, 20)
    arcade.draw_text("player against an ai", 50, 370, arcade.color.PINK, 20)

    arcade.draw_text("2 Player Mode:", 50, 240, arcade.color.PURPLE, 20)

    arcade.draw_text("This mode pits two players", 50, 210, arcade.color.PURPLE, 20)
    arcade.draw_text("against one another", 50, 180, arcade.color.PURPLE, 20)

    arcade.draw_text("Survival Mode:", 650, 430, arcade.color.RED, 20)

    arcade.draw_text("This mode is essentially", 650, 400, arcade.color.RED, 20)
    arcade.draw_text("a survival of the fittest", 650, 370, arcade.color.RED, 20)

    arcade.draw_text("Endless Mode", 650, 240, arcade.color.BLUE, 20)

    arcade.draw_text("This mode pits the player", 650, 210, arcade.color.BLUE, 20)
    arcade.draw_text("against an impossible ai", 650, 180, arcade.color.BLUE, 20)

    # Back button
    arcade.draw_rectangle_outline(100, 70, 150, 100, arcade.color.GREEN)
    arcade.draw_text("BACK", 55, 60, arcade.color.GREEN, 30)


def setup():

    arcade.open_window(screen_width, screen_height, screen_title)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


setup()
