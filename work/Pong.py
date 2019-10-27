import arcade
import random

# States
current_screen = 0
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
# 10 is win screen
# 11 is pause screen


# The current button that is activated
current_button = -2


# Screen variables
screen_width = 1000
screen_height = 600
screen_title = "Pong"


# Sound variables
play_sound = False
sound_persis = 'sound/persis.wav'

# States of modes
state_survival = False
state_endless = False

# Constant check conditions
player_win = False
is_win = True
is_playing = False
is_reset = False

# False is 1 player. True is 2 players
number_players = bool

# Used to set the screen into different modes
count = 0

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

# Velocity increases after hit
ball_velocity = 1
ball_velocity_check = False

# Determines the bouncing
ball_bounce_down = False
ball_bounce_up = True

# If ball type is False or 1 its for player 1. 2 or True is for player 2
if random.randint(0, 1) == 1:
    ball_type = False
else:
    ball_type = True

# Ball starting condition
if ball_type:
    ball_x = 250
else:
    ball_x = 750

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
score_high_score = 0

# To change the score from 10 to 100 smoothly
shift_pos = 0

# Dotted line position list
rectangle_list = [
                  8, 24, 40, 56,
                  72, 88, 104, 120,
                  136, 152, 166, 182,
                  198, 214, 230, 246,
                  262, 278, 294, 310,
                  326, 342, 358, 374,
                  390, 406, 422, 438,
                  454, 470, 486
]

# Buttons list value explanation: [x, y, w, h]
buttons = [
           [510, 320, 200, 100], [170, 480, 300, 200],
           [170, 260, 300, 200], [880, 530, 200, 100],
           [660, 530, 200, 100], [880, 410, 200, 100],
           [900, 70, 150, 100], [100, 70, 150, 100],
           [900, 70, 150, 100], [250, 555, 100, 50],
           [500, 300, 1000, 600], [250, 200, 200, 100],
           [750, 200, 200, 100]
]

# Button 2D list list
# 0 start button
# 1 two player mode button
# 2 one player mode button
# 3 normal mode button
# 4 survival mode button
# 5 endless mode button
# 6 how to play button
# 7 back button
# 8 next button
# 9 menu button
# 10 exit button
# 11 yes button
# 12 no button


# Delta time == 0.01 milliseconds
# 1 second = 0.01 x 100
# persis = 491 seconds
# 491 x 100
# = 49100
# so when delta time == 49100, restart persis
count_time = 0
time_check = 0


def on_update(delta_time):
    """
    Updates the entirety of the code
    and insures it running

    :param delta_time:
    :return:
    """

    # Pong globals
    global player_1_up_pressed, player_1_down_pressed, player_1_y, player_1_x

    global player_2_up_pressed, player_2_down_pressed, player_2_y, player_2_x

    global ball_x, ball_y, ball_bounce_up, ball_bounce_down, ball_type, ball_velocity, ball_velocity_check

    global score_player_1, score_player_2, score_ai, score_lives_player_1, score_lives_player_2, score_endless, \
        score_cap_player_1, score_cap_player_2, score_cap_ai, score_high_score

    global is_ai, ai_x, ai_y, ai_up, ai_down

    global current_screen, player_win

    global count, shift_pos

    global is_win, is_playing, is_reset

    global state_survival, state_endless

    global time_check

    # Background music reset check
    time_check += 1

    # Player 1 movement
    if player_1_up_pressed and player_1_y + 50 <= 490 and is_playing:
        player_1_y += 5
    if player_1_down_pressed and player_1_y - 50 >= 0 and is_playing:
        player_1_y -= 5

    # Player 2 movement
    if player_2_up_pressed and player_2_y + 50 <= 490 and not is_ai and is_playing:
        player_2_y += 5
    if player_2_down_pressed and player_2_y - 50 >= 0 and not is_ai and is_playing:
        player_2_y -= 5

    if ai_y + 50 >= 500 and is_ai and is_playing:
        ai_y = 445
    if ai_y - 50 <= 0 and is_ai and is_playing:
        ai_y = 50

    # Ball bouncing off of the divider and the bottom
    if ball_bounce_up and is_playing:
        ball_y += 5 + ball_velocity
    if ball_bounce_down and is_playing:
        ball_y -= 5 + ball_velocity

    # Ball bouncing off of the players
    if ball_type and is_playing:
        ball_x += 5 + ball_velocity
    if not ball_type and is_playing:
        ball_x -= 5 + ball_velocity

    # Increasing ball velocity
    if ball_velocity_check and is_playing:
        ball_velocity_check += 1
        ball_velocity_check = False

    # Same ball velocity
    if not ball_velocity_check and state_endless and is_playing:
        ball_velocity_check = 1

    # Check if the ball bounces off screen player 1
    if ball_x < 0 and not is_ai and not state_survival and not state_endless and is_playing:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_player_2 += 1

        if score_player_2 == score_cap_player_2 and is_win:
            current_screen = 10
            player_win = True
            is_win = False

    # Checking if the ball bounces off screen player 2
    if ball_x > 1000 and not is_ai and not state_survival and not state_endless and is_playing:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity = 1
        score_player_1 += 1

        if score_player_1 == score_cap_player_1 and is_win:
            current_screen = 10
            player_win = False
            is_win = False

    # Checking if the ball bounces off screen player 1
    if ball_x < 0 and is_ai and not state_survival and not state_endless and is_playing:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_ai += 1

        if score_ai == score_cap_ai and is_win:
            current_screen = 9
            is_win = False

    # Checking if the ball bounces off screen AI
    if ball_x > 1000 and is_ai and not state_survival and not state_endless and is_playing:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity = 1
        score_player_1 += 1

        if score_player_1 == score_cap_player_1:
            current_screen = 10
            player_win = False

    # Checking if the ball bounces off screen player 1 survival
    if ball_x < 0 and not is_ai and state_survival and not state_endless and is_playing:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_player_1 -= 1

        if score_player_1 == 0 and is_win:
            current_screen = 10
            player_win = True
            is_win = False

    # Checking if the ball bounces off screen player 2 survival
    if ball_x > 1000 and not is_ai and state_survival and not state_endless and is_playing:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity = 1
        score_player_2 -= 1

        if score_player_2 == 0 and is_win:
            current_screen = 10
            player_win = False
            is_win = False

    # Checking if the ball bounces off screen player 1 survival
    if ball_x < 0 and is_ai and state_survival and not state_endless and is_playing:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1
        score_player_1 -= 1

        if score_player_1 == 0 and is_win:
            current_screen = 9
            is_win = False

    # Checking if the ball bounces off screen AI survival
    if ball_x > 1000 and is_ai and state_survival and not state_endless and is_playing:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity = 1
        score_ai -= 1

        if score_ai == 0 and is_win:
            current_screen = 10
            player_win = False
            is_win = False

    if state_survival and is_ai and count == 0 and not state_endless and is_playing:
        score_player_1 = 3
        score_ai = 3
        count = 1

    if state_survival and not is_ai and count == 0 and not state_endless and is_playing:
        score_player_1 = 3
        score_player_2 = 3
        count = 1

    # Checking if the ball bounces off screen player 1 endless
    if ball_x < 0 and is_ai and state_endless and not state_survival and is_playing:
        ball_x = 250
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = True
        ball_velocity_check = False
        ball_velocity = 1

        if score_player_1 >= score_high_score:
            score_high_score = score_player_1

        current_screen = 9

    # Checking if the ball bounces off screen AI endless
    if ball_x > 1000 and is_ai and state_endless and not state_survival and is_playing:
        ball_x = 750
        ball_y = 250
        ball_bounce_up = False
        ball_bounce_down = False
        ball_type = False
        ball_velocity_check = False
        ball_velocity_check = 1

        score_player_1 += 1

    if state_endless and not state_survival and is_ai and count == 0 and is_playing:
        score_player_1 = 0
        score_ai = 0
        count = 3

    # Resetting everything to their original booleans / positions
    reset(is_reset)

    # Checking collision
    collision()


def on_draw():
    """
    Draws everything onto screens.
    Only runs certain code depending
    on the value of current_screen.

    :return:
    """

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
        two_player_screen()

    if current_screen == 5:
        one_player_screen()

    if current_screen == 6:
        survival_two_player_screen()

    if current_screen == 7:
        survival_one_player_screen()

    if current_screen == 8:
        endless_screen()

    if current_screen == 9:
        game_over_screen()

    if current_screen == 10:
        win_screen(player_win)

    if current_screen == 11:
        pause_screen()

    button_click_action(current_screen, current_button)


def on_key_press(key, modifiers):
    """
    Takes key inputs.

    :param key:
    :param modifiers:
    :return:
    """

    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    global is_ai

    global is_playing

    # Player 1 key input
    if key == arcade.key.W and is_playing:
        player_1_up_pressed = True
    if key == arcade.key.S and is_playing:
        player_1_down_pressed = True

    # Player 2 key input
    if key == arcade.key.UP and not is_ai and is_playing:
        player_2_up_pressed = True
    if key == arcade.key.DOWN and not is_ai and is_playing:
        player_2_down_pressed = True


def on_key_release(key, modifiers):
    """
    Runs after the release of the key.

    :param key:
    :param modifiers:
    :return:
    """

    global player_1_up_pressed, player_1_down_pressed

    global player_2_up_pressed, player_2_down_pressed

    global is_ai

    global is_playing

    # Player 1 key output
    if key == arcade.key.W and is_playing:
        player_1_up_pressed = False
    if key == arcade.key.S and is_playing:
        player_1_down_pressed = False

    # Player 2 key output
    if key == arcade.key.UP and not is_ai and is_playing:
        player_2_up_pressed = False
    if key == arcade.key.DOWN and not is_ai and is_playing:
        player_2_down_pressed = False


def on_mouse_press(x, y, button, modifiers):
    """
    Takes input for mouse click

    :param x:
    :param y:
    :param button:
    :param modifiers:
    :return:
    """

    global current_screen, current_button

    global buttons

    if current_screen == 0:

        # Start button Pong
        if buttons[0][0] - 100 < x < buttons[0][0] + 100 \
                and buttons[0][1] - 50 < y < buttons[0][1] + 50:
            current_button = 0

    if current_screen == 1:

        # Two player mode button
        if buttons[1][0] - 150 < x < buttons[1][0] + 150 \
                and buttons[1][1] - 100 < y < buttons[1][1] + 100:
            current_button = 0

        # One player mode button
        if buttons[2][0] - 150 < x < buttons[2][0] + 150 and \
                buttons[2][1] - 100 < y < buttons[2][1] + 100:
            current_button = 1

        # Normal mode button
        if buttons[3][0] - 100 < x < buttons[3][0] + 100 and \
                buttons[3][1] - 50 < y < buttons[3][1] + 50:
            current_button = 2

        # Survival mode button
        if buttons[4][0] - 100 < x < buttons[4][0] + 100 and \
                buttons[4][1] - 50 < y < buttons[4][1] + 50:
            current_button = 3

        # Endless mode button
        if buttons[5][0] - 100 < x < buttons[5][0] + 100 and \
                buttons[5][1] - 50 < y < buttons[5][1] + 50:
            current_button = 4

        # How to play button
        if buttons[6][0] - 75 < x < buttons[6][0] + 75 and \
                buttons[6][1] - 50 < y < buttons[6][1] + 50:
            current_button = 5

        # Back button
        if buttons[7][0] - 75 < x < buttons[7][0] + 75 and \
                buttons[7][1] - 50 < y < buttons[7][1] + 50:
            current_button = 6

    if current_screen == 2:

        # Back button
        if buttons[7][0] - 75 < x < buttons[7][0] + 75 and \
                buttons[7][1] - 50 < y < buttons[7][1] + 50:
            current_button = 0

        # Next button
        if buttons[8][0] - 75 < x < buttons[8][0] + 75 and \
                buttons[8][1] - 50 < y < buttons[8][1] + 50:
            current_button = 1

    if current_screen == 3:

        # Back button
        if buttons[7][0] - 75 < x < buttons[7][0] + 75 and \
                buttons[7][1] - 50 < y < buttons[7][1] + 50:
            current_button = -1

    if current_screen == 4 or current_screen == 5 or current_screen == 6 \
            or current_screen == 7 or current_screen == 8:

        # Menu Button
        if buttons[9][0] - 50 < x < buttons[9][0] + 50 and \
                buttons[9][1] - 25 < y < buttons[9][1] + 25:
            current_button = 0

    if current_screen == 9 or current_screen == 10:

        # Yes button
        if buttons[11][0] - 100 < x < buttons[11][0] + 100 and \
                buttons[11][1] - 50 < y < buttons[11][1] + 50:
            current_button = 0

        # No button
        if buttons[12][0] - 100 < x < buttons[12][0] + 100 and \
                buttons[12][1] - 50 and buttons[12][1] + 50:
            current_button = 1

    if current_screen == 11:

        # Exit button
        if buttons[10][0] - 500 < x < buttons[10][0] + 500 and \
                buttons[10][1] - 300 < y < buttons[10][1] + 300:
            current_button = -1


def button_click_action(screen, button):
    """
    After a mouse clicks on a button,
    this function activates and takes
    an input, which will change the game
    according to what each button does.

    :param screen:
    :param button:
    :return:
    """

    global current_screen

    global number_players

    global state_survival, state_endless

    global buttons

    if screen == 0:

        # Start button
        if button == 0:
            arcade.draw_rectangle_outline(buttons[0][0], buttons[0][1],
                                          buttons[0][2], buttons[0][3],
                                          arcade.color.YELLOW)
            current_screen = 1

    if screen == 1:

        # Two player button
        if button == 0:
            arcade.draw_rectangle_outline(buttons[1][0], buttons[1][1],
                                          buttons[1][2], buttons[1][3],
                                          arcade.color.GREEN)
            number_players = True

        # One player button
        if button == 1:
            arcade.draw_rectangle_outline(buttons[2][0], buttons[2][1],
                                          buttons[2][2], buttons[2][3],
                                          arcade.color.BLUE)
            number_players = False

        # Normal mode button
        if button == 2:
            arcade.draw_rectangle_outline(buttons[3][0], buttons[3][1],
                                          buttons[3][2], buttons[3][3],
                                          arcade.color.CYAN)
            state_survival = False
            state_endless = False

            # 2 player mode
            if number_players:
                current_screen = 4

            # 1 player mode
            if not number_players:
                current_screen = 5

        # Survival mode button
        if button == 3:
            arcade.draw_rectangle_outline(buttons[4][0], buttons[4][1],
                                          buttons[4][2], buttons[4][3],
                                          arcade.color.RED)

            state_survival = True
            state_endless = False

            # 2 player mode
            if number_players:
                current_screen = 6

            # 1 player mode
            if not number_players:
                current_screen = 7

        # Endless mode button
        if button == 4:
            arcade.draw_rectangle_outline(buttons[5][0], buttons[5][1],
                                          buttons[5][2], buttons[5][3],
                                          arcade.color.PURPLE)
            current_screen = 8

        # How to play button
        if button == 5:
            arcade.draw_rectangle_outline(buttons[6][0], buttons[6][1],
                                          buttons[6][2], buttons[6][3],
                                          arcade.color.YELLOW)
            current_screen = 2

        # Back button
        if button == 6:
            arcade.draw_rectangle_outline(buttons[7][0], buttons[7][1],
                                          buttons[7][2], buttons[7][3],
                                          arcade.color.RED)
            current_screen = 0

    if screen == 2:

        # Back button
        if button == 0:
            arcade.draw_rectangle_outline(buttons[7][0], buttons[7][1],
                                          buttons[7][2], buttons[7][3],
                                          arcade.color.RED)
            current_screen = 1

        # Next button
        if button == 1:
            arcade.draw_rectangle_outline(buttons[8][0], buttons[8][1],
                                          buttons[8][2], buttons[8][3],
                                          arcade.color.ORANGE)
            current_screen = 3

    if screen == 3:

        # Back button
        if button == -1:
            arcade.draw_rectangle_outline(buttons[7][0], buttons[7][1],
                                          buttons[7][2], buttons[7][3],
                                          arcade.color.RED)
            current_screen = 2

    if screen == 4 or screen == 5 or screen == 6 or screen == 7 or screen == 8:

        # Menu button
        if button == 0:
            arcade.draw_rectangle_outline(buttons[9][0], buttons[9][1],
                                          buttons[9][2], buttons[9][3],
                                          arcade.color.UNIVERSITY_OF_TENNESSEE_ORANGE)
            current_screen = 11

    if screen == 9 or screen == 10:

        # Yes button
        if button == 0:
            arcade.draw_rectangle_outline(buttons[11][0], buttons[11][1],
                                          buttons[11][2], buttons[11][3],
                                          arcade.color.PINK)
            current_screen = 1

        # No button
        if button == 1:
            arcade.draw_rectangle_outline(buttons[12][0], buttons[12][1],
                                          buttons[12][2], buttons[12][3],
                                          arcade.color.GO_GREEN)
            current_screen = 1

    if screen == 11:

        # Exit button
        if button == -1:
            arcade.draw_rectangle_outline(buttons[10][0], buttons[10][1],
                                          buttons[10][2], buttons[10][3],
                                          arcade.color.COSMIC_LATTE)
            current_screen = 1


def collision():
    """
    Checks the collision of everything.
    :return:
    """

    global player_1_x, player_1_y, score_player_1

    global player_2_x, player_2_y

    global ball_x, ball_y, ball_bounce_up, ball_bounce_down, ball_type, ball_velocity, ball_velocity_check

    global is_ai, ai_x, ai_y, score_ai

    global state_survival, state_endless

    global play_sound

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
    if (player_1_x - 10 <= ball_x <= player_1_x + 10) and (player_1_y - 50 <= ball_y <= player_1_y) \
            and not state_survival and not state_endless:
        ball_type = True
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 0.1

    if (player_1_x - 10 <= ball_x - 1 <= player_1_x + 10) and (player_1_y <= ball_y <= player_1_y + 50) \
            and not state_survival and not state_endless:
        ball_type = True
        ball_bounce_down = False
        ball_bounce_up = True
        ball_velocity_check = True
        ball_velocity += 0.1

    # Ball collision with player 1 survival
    if (player_1_x - 10 <= ball_x <= player_1_x + 10) and (player_1_y - 50 <= ball_y <= player_1_y) \
            and state_survival and not state_endless:
        ball_type = True
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 0.1

    if (player_1_x - 10 <= ball_x - 1 <= player_1_x + 10) and (player_1_y <= ball_y <= player_1_y + 50) \
            and state_survival and not state_endless:
        ball_type = True
        ball_bounce_down = False
        ball_bounce_up = True
        ball_velocity_check = True
        ball_velocity += 0.1

    # Ball collision with player 1 endless
    if (player_1_x - 10 <= ball_x <= player_1_x + 10) and (player_1_y - 50 <= ball_y <= player_1_y) \
            and not state_survival and state_endless:
        ball_type = True
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 0.1

    if (player_1_x - 10 <= ball_x - 1 <= player_1_x + 10) and (player_1_y <= ball_y <= player_1_y + 50) \
            and not state_survival and state_endless:
        ball_type = True
        ball_bounce_down = False
        ball_bounce_up = True
        ball_velocity_check = True
        ball_velocity += 0.1

    # Ball collision with player 2
    if (player_2_x - 10 <= ball_x + 1 <= player_2_x + 10) and (player_2_y - 50 <= ball_y <= player_2_y) and not is_ai:
        ball_type = False
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 0.1

    if (player_2_x - 10 <= ball_x + 1 <= player_2_x + 10) and (player_2_y <= ball_y <= player_2_y + 50) and not is_ai:
        ball_type = False
        ball_bounce_up = True
        ball_bounce_down = False
        ball_velocity_check = True
        ball_velocity += 0.1

    # Ball collision with AI
    if (ai_x - 10 <= ball_x + 1 <= ai_x + 10) and (ai_y - 50 <= ball_y <= ai_y) and is_ai:
        ball_type = False
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        ball_velocity += 0.1

    if (ai_x - 10 <= ball_x + 1 <= ai_x + 10) and (ai_y <= ball_y <= ai_y + 50) and is_ai:
        ball_type = False
        ball_bounce_up = True
        ball_bounce_down = False
        ball_velocity_check = True
        ball_velocity += 0.1

    # Ball collision with player 1 endless mode
    if (player_1_x - 10 <= ball_x <= player_1_x + 10) and (player_1_y - 50 <= ball_y <= player_1_y) \
            and state_endless and is_ai:
        ball_type = True
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True
        score_player_1 += 1

    if (player_1_x - 10 <= ball_x - 1 < player_1_x + 10) and (player_1_y <= ball_y <= player_1_y + 50) \
            and state_endless and is_ai:
        ball_type = True
        ball_bounce_down = False
        ball_bounce_up = True
        ball_velocity_check = True
        score_player_1 += 1

    # Ball collision with AI
    if (ai_x - 10 <= ball_x + 1 <= ai_x + 10) and (ai_y - 50 <= ball_y <= ai_y) and is_ai:
        ball_type = False
        ball_bounce_up = False
        ball_bounce_down = True
        ball_velocity_check = True

    if (ai_x - 10 <= ball_x + 1 <= ai_x + 10) and (ai_y <= ball_y <= ai_y + 50) and is_ai:
        ball_type = False
        ball_bounce_up = True
        ball_bounce_down = False
        ball_velocity_check = True

    if ai_y + 50 >= 500 and is_ai and state_endless and not state_survival:
        ai_y = 445
    if ai_y - 50 <= 0 and is_ai and state_endless and not state_survival:
        ai_y = 50


def ai():
    """
    The AI code for everything.

    :return:
    """

    global ai_y, ball_y

    global state_survival, state_endless

    if ball_y >= ai_y and state_survival and not state_endless:
        ai_y += 6

    if ball_y <= ai_y and state_survival and not state_endless:
        ai_y -= 6

    if ball_y >= ai_y and state_endless and not state_survival:
        ai_y += 6

    if ball_y <= ai_y and state_endless and not state_survival:
        ai_y -= 6

    if ball_y >= ai_y and not state_survival and not state_endless:
        ai_y += 6

    if ball_y <= ai_y and not state_survival and not state_endless:
        ai_y -= 6


def start_screen():
    """
    Holds all the code for
    the start screen.

    :return:
    """

    global is_playing

    global state_survival, state_endless

    global buttons

    is_playing = False
    state_survival = False
    state_endless = False

    arcade.draw_text("P O N G", 300, 500, arcade.color.PURPLE_MOUNTAIN_MAJESTY, 100)

    arcade.draw_rectangle_outline(buttons[0][0], buttons[0][1], buttons[0][2],
                                  buttons[0][3], arcade.color.TURQUOISE)
    arcade.draw_text("S T A R T", 420, 300, arcade.color.TURQUOISE, 40)

    # The players
    arcade.draw_rectangle_outline(100, 200, 25, 200, arcade.color.GUPPIE_GREEN, 1, 15)
    arcade.draw_rectangle_outline(900, 400, 25, 200, arcade.color.REDWOOD, 1, 15)

    # The ball
    arcade.draw_rectangle_filled(510, 315, 40, 40, arcade.color.BLUE_SAPPHIRE, 15)


def mode_screen():
    """
    Holds the code for the
    mode selection screen.

    :return:
    """

    global is_playing

    global state_survival, state_endless

    global buttons, is_reset

    is_playing = False
    state_survival = False
    state_endless = False

    # 2 player mode
    arcade.draw_rectangle_outline(buttons[1][0], buttons[1][1], buttons[1][2],
                                  buttons[1][3], arcade.color.WHITE)
    arcade.draw_text("2 Players", 140, 480, arcade.color.WHITE)

    # 1 player mode
    arcade.draw_rectangle_outline(buttons[2][0], buttons[2][1], buttons[2][2],
                                  buttons[2][3], arcade.color.RED)
    arcade.draw_text("1 Player", 140, 260, arcade.color.RED)

    # Normal mode
    arcade.draw_rectangle_outline(buttons[3][0], buttons[3][1], buttons[3][2],
                                  buttons[3][3], arcade.color.ORANGE)
    arcade.draw_text("Normal Mode", 805, 520, arcade.color.ORANGE, 20)

    # Survival mode
    arcade.draw_rectangle_outline(buttons[4][0], buttons[4][1], buttons[4][2],
                                  buttons[4][3], arcade.color.BLUE)
    arcade.draw_text("Survival Mode", 585, 520, arcade.color.BLUE, 20)

    # Endless mode
    arcade.draw_rectangle_outline(buttons[5][0], buttons[5][1], buttons[5][2],
                                  buttons[5][3], arcade.color.YELLOW)
    arcade.draw_text("Endless Mode", 805, 400, arcade.color.YELLOW, 20)

    # How to play button
    arcade.draw_rectangle_outline(buttons[6][0], buttons[6][1], buttons[6][2],
                                  buttons[6][3], arcade.color.PURPLE)
    arcade.draw_text("HOW TO", 855, 75, arcade.color.PURPLE, 20)
    arcade.draw_text("PLAY", 875, 50, arcade.color.PURPLE, 20)

    # Back button
    arcade.draw_rectangle_outline(buttons[7][0], buttons[7][1], buttons[7][2],
                                  buttons[7][3], arcade.color.GREEN)
    arcade.draw_text("BACK", 55, 60, arcade.color.GREEN, 30)

    # Small pong game

    # The players
    arcade.draw_rectangle_outline(400, 450, 10, 100, arcade.color.ELECTRIC_YELLOW, 1, -15)
    arcade.draw_rectangle_outline(850, 260, 10, 100, arcade.color.INTERNATIONAL_ORANGE, 1, -15)

    # The ball
    arcade.draw_rectangle_outline(600, 350, 10, 10, arcade.color.VIVID_VIOLET)

    is_reset = True


def how_to_play_screen():
    """
    Holds the code for the
    how to play screen.

    :return:
    """

    global is_playing

    global state_survival, state_endless

    global buttons

    is_playing = False
    state_survival = False
    state_endless = False

    arcade.draw_text("HOW TO PLAY", 100, 500, arcade.color.BRONZE, 100)

    arcade.draw_text("Player 1:", 100, 430, arcade.color.PINK, 20)

    arcade.draw_text("Use the 'W' key to move up", 100, 400, arcade.color.PINK, 20)
    arcade.draw_text("Use the 'S' key to move down", 100, 370, arcade.color.PINK, 20)

    arcade.draw_text("Player 2:", 500, 430, arcade.color.PURPLE, 20)

    arcade.draw_text("Use the up arrow to move up", 500, 400, arcade.color.PURPLE, 20)
    arcade.draw_text("Use the down arrow to move down", 500, 370, arcade.color.PURPLE, 20)

    # Back button
    arcade.draw_rectangle_outline(buttons[7][0], buttons[7][1], buttons[7][2],
                                  buttons[7][3], arcade.color.GREEN)
    arcade.draw_text("BACK", 55, 60, arcade.color.GREEN, 30)

    # Next button
    arcade.draw_rectangle_outline(buttons[8][0], buttons[8][1], buttons[8][2],
                                  buttons[8][3], arcade.color.BLUE)
    arcade.draw_text("NEXT", 855, 60, arcade.color.BLUE, 30)


def instruction_screen():
    """
    Holds the code for the
    instruction screen.

    :return:
    """

    global is_playing

    global state_survival, state_endless

    global buttons

    is_playing = False
    state_survival = False
    state_endless = False

    arcade.draw_text("THE DIFFERENT MODES", 50, 500, arcade.color.BRONZE, 70)

    arcade.draw_text("1 Player Mode:", 50, 430, arcade.color.PINK, 20)

    arcade.draw_text("This mode pits the", 50, 400, arcade.color.PINK, 20)
    arcade.draw_text("player against an ai", 50, 370, arcade.color.PINK, 20)

    arcade.draw_text("2 Player Mode:", 50, 240, arcade.color.PURPLE, 20)

    arcade.draw_text("This mode pits two players", 50, 210, arcade.color.PURPLE, 20)
    arcade.draw_text("against one another", 50, 180, arcade.color.PURPLE, 20)

    arcade.draw_text("Normal Mode:", 350, 350, arcade.color.BITTER_LEMON, 20)

    arcade.draw_text("This mode pits two players", 350, 320, arcade.color.BITTER_LEMON, 20)
    arcade.draw_text("against each other or one", 350, 290, arcade.color.BITTER_LEMON, 20)
    arcade.draw_text("player against an ai", 350, 260, arcade.color.BITTER_LEMON, 20)

    arcade.draw_text("Survival Mode:", 650, 430, arcade.color.RED, 20)

    arcade.draw_text("This mode is essentially", 650, 400, arcade.color.RED, 20)
    arcade.draw_text("a survival of the fittest", 650, 370, arcade.color.RED, 20)

    arcade.draw_text("Endless Mode", 650, 240, arcade.color.BLUE, 20)

    arcade.draw_text("This mode pits the player", 650, 210, arcade.color.BLUE, 20)
    arcade.draw_text("against an impossible ai", 650, 180, arcade.color.BLUE, 20)

    # Back button
    arcade.draw_rectangle_outline(buttons[7][0], buttons[7][1], buttons[7][2],
                                  buttons[7][3], arcade.color.GREEN)
    arcade.draw_text("BACK", 55, 60, arcade.color.GREEN, 30)


def two_player_screen():
    """
    Holds the code for a two
    player game.

    :return:
    """

    global shift_pos

    global is_ai, is_playing

    global state_survival, state_endless

    global buttons

    is_ai = False
    is_playing = True
    state_survival = False
    state_endless = False

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

    # Menu
    arcade.draw_rectangle_outline(buttons[9][0], buttons[9][1], buttons[9][2],
                                  buttons[9][3], arcade.color.CERULEAN)
    arcade.draw_text("MENU", 215, 545, arcade.color.CERULEAN, 20)


def one_player_screen():
    """
    Holds the code for a one
    player game against an ai.

    :return:
    """

    global shift_pos

    global is_ai, is_playing

    global state_survival, state_endless

    global buttons

    is_ai = True
    is_playing = True
    state_survival = False
    state_endless = False

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

    # Menu
    arcade.draw_rectangle_outline(buttons[9][0], buttons[9][1], buttons[9][2],
                                  buttons[9][3], arcade.color.CERULEAN)
    arcade.draw_text("MENU", 215, 545, arcade.color.CERULEAN, 20)


def survival_two_player_screen():
    """
    Holds the code for a two
    player survival game.

    :return:
    """

    global score_player_1, score_player_2

    global shift_pos

    global is_ai, is_playing

    global state_survival, state_endless

    global buttons

    is_playing = True
    is_ai = False
    state_survival = True
    state_endless = False

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

    # Menu
    arcade.draw_rectangle_outline(buttons[9][0], buttons[9][1], buttons[9][2],
                                  buttons[9][3], arcade.color.CERULEAN)
    arcade.draw_text("MENU", 215, 545, arcade.color.CERULEAN, 20)


def survival_one_player_screen():
    """
    Holds the code for a one
    player survival game
    against an ai.

    :return:
    """

    global score_player_1, score_ai

    global shift_pos

    global is_ai, is_playing

    global state_survival, state_endless

    global buttons

    is_ai = True
    state_survival = True
    state_endless = False
    is_playing = True

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
        # Player 2 Score
        arcade.draw_text(str(score_player_2), 520, 525, arcade.color.WHITE, 70)

    if is_ai:
        # AI
        arcade.draw_text(str(score_ai), 520, 525, arcade.color.RED, 70)

    # Colon
    arcade.draw_rectangle_filled(500, 570, 10, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(500, 540, 10, 10, arcade.color.WHITE)

    # Menu
    arcade.draw_rectangle_outline(buttons[9][0], buttons[9][1], buttons[9][2],
                                  buttons[9][3], arcade.color.CERULEAN)
    arcade.draw_text("MENU", 215, 545, arcade.color.CERULEAN, 20)


def endless_screen():
    """
    Holds the code for an
    endless game against an
    impossible ai, therefore
    making it endless.

    :return:
    """

    global score_player_1, score_ai

    global shift_pos

    global state_survival, state_endless

    global ai_y

    global is_ai, is_playing

    global buttons

    is_ai = True
    state_survival = False
    state_endless = True
    is_playing = True

    # Player 1
    arcade.draw_rectangle_outline(player_1_x, player_1_y, 10, 100, arcade.color.WHITE)

    if not is_ai:
        # Player 2
        arcade.draw_rectangle_outline(player_2_x, player_2_y, 10, 100, arcade.color.WHITE)

    if is_ai and 500 <= ball_x:
        # AI
        arcade.draw_rectangle_outline(ai_x, ball_y, 10, 100, arcade.color.RED)
        ai_y = ball_y
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
        # Player 2 score
        arcade.draw_text(str(score_player_2), 520, 525, arcade.color.WHITE, 70)

    if is_ai:
        # AI
        arcade.draw_text(str(score_ai), 520, 525, arcade.color.RED, 70)

    # Colon
    arcade.draw_rectangle_filled(500, 570, 10, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(500, 540, 10, 10, arcade.color.WHITE)

    # Menu
    arcade.draw_rectangle_outline(buttons[9][0], buttons[9][1], buttons[9][2],
                                  buttons[9][3], arcade.color.CERULEAN)
    arcade.draw_text("MENU", 215, 545, arcade.color.CERULEAN, 20)


def game_over_screen():
    """
    Holds the code to draw
    the game over screen.

    :return:
    """

    global is_playing, shift_pos

    global state_survival, state_endless

    global buttons, is_reset

    global score_high_score

    is_playing = False

    if state_endless:
        if score_high_score < 10:
            arcade.draw_text(str(score_high_score), 460, 200, arcade.color.AO, 100)

        if score_high_score >= 100:
            arcade.draw_text(str(score_high_score), 400, 200, arcade.color.AO, 100)
            shift_pos = 30

        if score_high_score >= 10:
            arcade.draw_text(str(score_high_score), 430 - shift_pos, 200, arcade.color.AO, 100)

    arcade.draw_text("YOU LOSE", 230, 500, arcade.color.CANDY_APPLE_RED, 100)
    arcade.draw_text("PLAY AGAIN?", 330, 400, arcade.color.SAPPHIRE, 50)

    # Yes button
    arcade.draw_rectangle_outline(buttons[11][0], buttons[11][1], buttons[11][2],
                                  buttons[11][3], arcade.color.GREEN)
    arcade.draw_text("YES", 230, 190, arcade.color.GREEN, 20)

    # No button
    arcade.draw_rectangle_outline(buttons[12][0], buttons[12][1], buttons[12][2],
                                  buttons[12][3], arcade.color.RED)
    arcade.draw_text("NO", 735, 190, arcade.color.RED, 20)


def win_screen(winner):
    """
    Holds the code for
    drawing the win screen.

    :param winner:
    :return:
    """

    global is_playing

    global buttons, is_reset

    global state_survival, state_endless

    is_playing = False
    state_survival = False
    state_endless = False

    # Player 1 win code
    if not winner:
        arcade.draw_text("PLAYER 1 WINS", 80, 500, arcade.color.PURPLE_MOUNTAIN_MAJESTY, 100)
        arcade.draw_text("PLAY AGAIN?", 330, 400, arcade.color.SAPPHIRE, 50)

    # Player 2 win code
    if winner:
        arcade.draw_text("PLAYER 2 WINS", 80, 500, arcade.color.UNIVERSITY_OF_TENNESSEE_ORANGE, 100)
        arcade.draw_text("PLAY AGAIN?", 330, 400, arcade.color.RED_DEVIL, 50)

    # Yes button
    arcade.draw_rectangle_outline(buttons[11][0], buttons[11][1], buttons[11][2],
                                  buttons[11][3], arcade.color.GREEN)
    arcade.draw_text("YES", 230, 190, arcade.color.GREEN, 20)

    # No button
    arcade.draw_rectangle_outline(buttons[12][0], buttons[12][1], buttons[12][2],
                                  buttons[12][3], arcade.color.RED)
    arcade.draw_text("NO", 735, 190, arcade.color.RED, 20)

    is_reset = True


def pause_screen():
    """
    Holds the code to draw
    the pause screen.

    :return:
    """

    global is_playing

    global buttons

    is_playing = False

    # Exit button
    arcade.draw_rectangle_outline(buttons[10][0], buttons[10][1], buttons[10][2],
                                  buttons[10][3], arcade.color.GHOST_WHITE)
    arcade.draw_text("EXIT", 275, 240, arcade.color.GHOST_WHITE, 200)


def reset(am_reset):
    """
    Resets everything to their
    original positions.
    (Referring to game aspects)

    :param am_reset:
    :return:
    """

    global is_reset, count, shift_pos

    global state_survival, state_endless, player_win, is_win, is_playing

    global player_1_x, player_1_y, player_1_up_pressed, player_1_down_pressed

    global player_2_x, player_2_y, player_2_up_pressed, player_2_down_pressed

    global is_ai, ai_x, ai_y, ai_up, ai_down

    global ball_x, ball_y, ball_type, ball_velocity, ball_velocity_check, ball_bounce_up, ball_bounce_down

    global score_player_1, score_player_2, score_ai, score_endless, score_lives_player_1, score_lives_player_2

    global score_cap_player_1, score_cap_player_2, score_cap_ai, score_high_score

    if am_reset:
        count = 0
        state_survival = False
        state_endless = False
        player_win = False
        is_win = True
        is_playing = False

        player_1_x = 50
        player_1_y = 250
        player_1_up_pressed = False
        player_1_down_pressed = False

        player_2_x = 950
        player_2_y = 250
        player_2_up_pressed = False
        player_2_down_pressed = False

        is_ai = True
        ai_x = 950
        ai_y = 250
        ai_up = False
        ai_down = False

        ball_x = 500
        ball_y = 250

        if random.randint(0, 1) == 1:
            ball_type = False
        else:
            ball_type = True

        if ball_type:
            ball_x = 250
        else:
            ball_x = 750

        ball_velocity = 1
        ball_velocity_check = False

        ball_bounce_down = False
        ball_bounce_up = True

        score_player_1 = 0
        score_player_2 = 0
        score_ai = 0
        score_endless = 0
        score_lives_player_1 = 0
        score_lives_player_2 = 0
        score_cap_player_1 = 5
        score_cap_player_2 = 5
        score_cap_ai = 5
        score_high_score = 0

        shift_pos = 0

        is_reset = False


def music(time):
    """
    Holds the code in order
    to run background music.

    Be warned, I'm told
    it's quite loud.

    :param time:
    :return:
    """

    global count_time

    # Resets the music when it ends
    if time == 49100 * count_time:
        arcade.play_sound(sound_persis)
        count_time += 1


def setup():
    """
    Holds the code that
    enables the game to
    function and run.

    :return:
    """

    global time_check

    arcade.open_window(screen_width, screen_height, screen_title)

    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    music(time_check)

    arcade.run()


setup()
