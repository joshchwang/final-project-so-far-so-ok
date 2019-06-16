import arcade
import random

ttt_screen_width = 600
ttt_screen_height = 800
ttt_screen_title = "TicTacToe"


# Player 1 variables
ttt_player_1_top_left = False
ttt_player_1_top_middle = False
ttt_player_1_top_right = False

ttt_player_1_middle_left = False
ttt_player_1_middle_middle = False
ttt_player_1_middle_right = False

ttt_player_1_bottom_left = False
ttt_player_1_bottom_middle = False
ttt_player_1_bottom_right = False

ttt_player_1_score = 0

ttt_game_win_player_1 = False

ttt_player_1_big_score = 0

ttt_player_1_wins = False

ttt_player_1_game_win = False

# Player 1 win cases
ttt_win_player_1_bottom_row = False
ttt_win_player_1_middle_row = False
ttt_win_player_1_top_row = False

ttt_win_player_1_left_column = False
ttt_win_player_1_middle_column = False
ttt_win_player_1_right_column = False

ttt_win_player_1_diagonal_downward = False
ttt_win_player_1_diagonal_upward = False


# Player 2 variables
ttt_player_2_top_left = False
ttt_player_2_top_middle = False
ttt_player_2_top_right = False

ttt_player_2_middle_left = False
ttt_player_2_middle_middle = False
ttt_player_2_middle_right = False

ttt_player_2_bottom_left = False
ttt_player_2_bottom_middle = False
ttt_player_2_bottom_right = False

ttt_player_2_score = 0

ttt_game_win_player_2 = False

ttt_player_2_big_score = 0

ttt_player_2_wins = False

ttt_player_2_game_win = False

# Player 2 win cases
ttt_win_player_2_bottom_row = False
ttt_win_player_2_middle_row = False
ttt_win_player_2_top_row = False

ttt_win_player_2_left_column = False
ttt_win_player_2_middle_column = False
ttt_win_player_2_right_column = False

ttt_win_player_2_diagonal_downward = False
ttt_win_player_2_diagonal_upward = False


# Variables to determine which player has what box
# A value of 1 means that player 1 holds the space
# A value of 2 means that player 2 hold the space
ttt_taken_bottom_left = 0
ttt_taken_bottom_middle = 0
ttt_taken_bottom_right = 0

ttt_taken_middle_left = 0
ttt_taken_middle_middle = 0
ttt_taken_middle_right = 0

ttt_taken_top_left = 0
ttt_taken_top_middle = 0
ttt_taken_top_right = 0


ttt_win_condition = True
ttt_point_won = False
ttt_is_reset = False
ttt_max_score = 5

current_screen = 0

if random.randint(2, 3) == 2:
    ttt_player_1_turn = True
    ttt_player_2_turn = False
else:
    ttt_player_1_turn = False
    ttt_player_2_turn = True


# 3D list containing all the positions
# Includes 'O', 'X', box, and line positions
ttt_positions = [
    # O positions
    [
        # Bottom left
        [100, 100, 100],

        # Bottom middle
        [300, 100, 100],

        # Bottom right
        [500, 100, 100],

        # Middle left
        [100, 300, 100],

        # Middle middle
        [300, 300, 100],

        # Middle bottom
        [500, 300, 100],

        # Top left
        [100, 500, 100],

        # Top middle
        [300, 500, 100],

        # Top right
        [500, 500, 100]

    ],

    # X positions
    [
        # Bottom left
        [0, 0, 200, 200],
        [0, 200, 200, 0],

        # Bottom middle
        [200, 0, 400, 200],
        [200, 200, 400, 0],

        # Bottom right
        [400, 0, 600, 200],
        [400, 200, 600, 0],

        # Middle left
        [0, 200, 200, 400],
        [0, 400, 200, 200],

        # Middle middle
        [200, 200, 400, 400],
        [200, 400, 400, 200],

        # Middle right
        [400, 200, 600, 400],
        [400, 400, 600, 200],

        # Top left
        [0, 400, 200, 600],
        [0, 600, 200, 400],

        # Top middle
        [200, 400, 400, 600],
        [200, 600, 400, 400],

        # Top right
        [400, 400, 600, 600],
        [400, 600, 600, 400]

    ],

    # Box positions
    [
        # Bottom left
        [100, 100, 200, 200],

        # Bottom middle
        [300, 100, 200, 200],

        # Bottom right
        [500, 100, 200, 200],

        # Middle left
        [100, 300, 200, 200],

        # Middle middle
        [300, 300, 200, 200],

        # Middle bottom
        [500, 300, 200, 200],

        # Top left
        [100, 500, 200, 200],

        # Top middle
        [300, 500, 200, 200],

        # Top right
        [500, 500, 200, 200]

    ],

    # Line positions
    [
        # Bottom row
        [0, 100, 600, 100],

        # Middle row
        [0, 300, 600, 300],

        # Top row
        [0, 500, 600, 500],

        # Left column
        [100, 0, 100, 600],

        # Middle column
        [300, 0, 300, 600],

        # Right column
        [500, 0, 500, 600],

        # Downwards diagonal
        [0, 600, 600, 0],

        # Upwards diagonal
        [0, 0, 600, 600]

    ]
]


def on_update(delta_time):
    global ttt_player_1_top_left, ttt_player_1_top_middle, ttt_player_1_top_right
    global ttt_player_1_middle_left, ttt_player_1_middle_middle, ttt_player_1_middle_right
    global ttt_player_1_bottom_left, ttt_player_1_bottom_middle, ttt_player_1_bottom_right

    global ttt_win_player_1_bottom_row, ttt_win_player_1_middle_row, ttt_win_player_1_top_row
    global ttt_win_player_1_left_column, ttt_win_player_1_middle_column, ttt_win_player_1_right_column
    global ttt_win_player_1_diagonal_downward, ttt_win_player_1_diagonal_upward

    global ttt_game_win_player_1, ttt_player_1_score, ttt_player_1_turn, ttt_player_1_big_score, \
        ttt_player_1_wins, ttt_player_1_game_win

    global ttt_player_2_top_left, ttt_player_2_top_middle, ttt_player_2_top_right
    global ttt_player_2_middle_left, ttt_player_2_middle_middle, ttt_player_2_middle_right
    global ttt_player_2_bottom_left, ttt_player_2_bottom_middle, ttt_player_2_bottom_right

    global ttt_win_player_2_bottom_row, ttt_win_player_2_middle_row, ttt_win_player_2_top_row
    global ttt_win_player_2_left_column, ttt_win_player_2_middle_column, ttt_win_player_2_right_column
    global ttt_win_player_2_diagonal_downward, ttt_win_player_2_diagonal_upward

    global ttt_game_win_player_2, ttt_player_2_score, ttt_player_2_turn, ttt_player_2_big_score, \
        ttt_player_2_wins, ttt_player_2_game_win

    global ttt_taken_top_left, ttt_taken_top_middle, ttt_taken_top_right
    global ttt_taken_middle_left, ttt_taken_middle_middle, ttt_taken_middle_right
    global ttt_taken_bottom_left, ttt_taken_bottom_middle, ttt_taken_bottom_right

    global ttt_win_condition, ttt_point_won, ttt_is_reset, ttt_max_score, current_screen

    ttt_reset(ttt_is_reset)

    if ttt_player_1_game_win:
        current_screen = 12
        ttt_player_1_game_win = False

    if ttt_player_2_game_win:
        current_screen = 13
        ttt_player_2_game_win = False

    # Player 1 checks

    # Player 1 checking bottom row
    if ttt_player_1_bottom_left and ttt_player_1_bottom_middle and ttt_player_1_bottom_right \
            and not ttt_player_2_bottom_left and not ttt_player_2_bottom_middle and not \
            ttt_player_2_bottom_right and ttt_win_condition:
        ttt_win_player_1_bottom_row = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking middle row
    if ttt_player_1_middle_left and ttt_player_1_middle_middle and ttt_player_1_middle_right \
            and not ttt_player_2_middle_left and not ttt_player_2_middle_middle and not \
            ttt_player_2_middle_right and ttt_win_condition:
        ttt_win_player_1_middle_row = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking top row
    if ttt_player_1_top_left and ttt_player_1_top_middle and ttt_player_1_top_right \
            and not ttt_player_2_top_left and not ttt_player_2_top_middle and not \
            ttt_player_2_top_right and ttt_win_condition:
        ttt_win_player_1_top_row = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking left column
    if ttt_player_1_bottom_left and ttt_player_1_middle_left and ttt_player_1_top_left \
            and not ttt_player_2_bottom_left and not ttt_player_2_middle_left and not \
            ttt_player_2_top_left and ttt_win_condition:
        ttt_win_player_1_left_column = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking middle column
    if ttt_player_1_bottom_middle and ttt_player_1_middle_middle and ttt_player_1_top_middle \
            and not ttt_player_2_bottom_middle and not ttt_player_2_middle_middle and not \
            ttt_player_2_top_middle and ttt_win_condition:
        ttt_win_player_1_middle_column = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking right column
    if ttt_player_1_bottom_right and ttt_player_1_middle_right and ttt_player_1_top_right \
            and not ttt_player_2_bottom_right and not ttt_player_2_middle_right and not \
            ttt_player_2_top_right and ttt_win_condition:
        ttt_win_player_1_right_column = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking downward diagonal
    if ttt_player_1_top_left and ttt_player_1_middle_middle and ttt_player_1_bottom_right \
            and not ttt_player_2_top_left and not ttt_player_2_middle_middle and not \
            ttt_player_2_bottom_right and ttt_win_condition:
        ttt_win_player_1_diagonal_downward = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 1 checking upward diagonal
    if ttt_player_1_bottom_left and ttt_player_1_middle_middle and ttt_player_1_top_right \
            and not ttt_player_2_bottom_left and not ttt_player_2_middle_middle and not \
            ttt_player_2_top_right and ttt_win_condition:
        ttt_win_player_1_diagonal_upward = True
        ttt_game_win_player_1 = True
        ttt_win_condition = False
        ttt_player_1_wins = True

    # Player 2 checks

    # Player 2 checking bottom row
    if ttt_player_2_bottom_left and ttt_player_2_bottom_middle and ttt_player_2_bottom_right \
            and not ttt_player_1_bottom_left and not ttt_player_1_bottom_middle and not \
            ttt_player_1_bottom_right and ttt_win_condition:
        ttt_win_player_2_bottom_row = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking middle row
    if ttt_player_2_middle_left and ttt_player_2_middle_middle and ttt_player_2_middle_right \
            and not ttt_player_1_middle_left and not ttt_player_1_middle_middle and not \
            ttt_player_1_middle_right and ttt_win_condition:
        ttt_win_player_2_middle_row = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking top row
    if ttt_player_2_top_left and ttt_player_2_top_middle and ttt_player_2_top_right \
            and not ttt_player_1_top_left and not ttt_player_1_top_middle and not \
            ttt_player_1_top_right and ttt_win_condition:
        ttt_win_player_2_top_row = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking left column
    if ttt_player_2_bottom_left and ttt_player_2_middle_left and ttt_player_2_top_left \
            and not ttt_player_1_bottom_left and not ttt_player_1_middle_left and not \
            ttt_player_1_top_left and ttt_win_condition:
        ttt_win_player_2_left_column = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking middle column
    if ttt_player_2_bottom_middle and ttt_player_2_middle_middle and ttt_player_2_top_middle \
            and not ttt_player_1_bottom_middle and not ttt_player_1_middle_middle and not \
            ttt_player_1_top_middle and ttt_win_condition:
        ttt_win_player_2_middle_column = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking right column
    if ttt_player_2_bottom_right and ttt_player_2_middle_right and ttt_player_2_top_right \
            and not ttt_player_1_bottom_right and not ttt_player_1_middle_right and not \
            ttt_player_1_top_right and ttt_win_condition:
        ttt_win_player_2_right_column = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking downward diagonal
    if ttt_player_2_top_left and ttt_player_2_middle_middle and ttt_player_2_bottom_right \
            and not ttt_player_1_top_left and not ttt_player_1_middle_middle and not \
            ttt_player_1_bottom_right and ttt_win_condition:
        ttt_win_player_2_diagonal_downward = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Player 2 checking upward diagonal
    if ttt_player_2_bottom_left and ttt_player_2_middle_middle and ttt_player_2_top_right \
            and not ttt_player_1_bottom_left and not ttt_player_1_middle_middle and not \
            ttt_player_1_top_right and ttt_win_condition:
        ttt_win_player_2_diagonal_upward = True
        ttt_game_win_player_2 = True
        ttt_win_condition = False
        ttt_player_2_wins = True

    # Checking if it's a draw
    if ttt_taken_bottom_left != 0 and ttt_taken_bottom_middle != 0 and ttt_taken_bottom_right != 0 \
            and ttt_taken_middle_left != 0 and ttt_taken_middle_middle != 0 and ttt_taken_middle_right != 0 \
            and ttt_taken_top_right != 0 and ttt_taken_top_middle != 0 and ttt_taken_top_left != 0:
        ttt_point_won = True

        if random.randint(4, 5) == 4:
            ttt_player_1_turn = True
            ttt_player_2_turn = False
        else:
            ttt_player_1_turn = False
            ttt_player_2_turn = True


def on_draw():
    global ttt_player_1_top_left, ttt_player_1_top_middle, ttt_player_1_top_right
    global ttt_player_1_middle_left, ttt_player_1_middle_middle, ttt_player_1_middle_right
    global ttt_player_1_bottom_left, ttt_player_1_bottom_middle, ttt_player_1_bottom_right

    global ttt_win_player_1_bottom_row, ttt_win_player_1_middle_row, ttt_win_player_1_top_row
    global ttt_win_player_1_left_column, ttt_win_player_1_middle_column, ttt_win_player_1_right_column
    global ttt_win_player_1_diagonal_downward, ttt_win_player_1_diagonal_upward

    global ttt_player_1_score, ttt_game_win_player_1, ttt_player_1_big_score

    global ttt_player_2_top_left, ttt_player_2_top_middle, ttt_player_2_top_right
    global ttt_player_2_middle_left, ttt_player_2_middle_middle, ttt_player_2_middle_right
    global ttt_player_2_bottom_left, ttt_player_2_bottom_middle, ttt_player_2_bottom_right

    global ttt_win_player_2_bottom_row, ttt_win_player_2_middle_row, ttt_win_player_2_top_row
    global ttt_win_player_2_left_column, ttt_win_player_2_middle_column, ttt_win_player_2_right_column
    global ttt_win_player_2_diagonal_downward, ttt_win_player_2_diagonal_upward

    global ttt_player_2_score, ttt_game_win_player_2, ttt_player_2_big_score

    global ttt_positions

    global ttt_point_won

    arcade.start_render()

    # Drawing the separation divider lines
    arcade.draw_line(200, 0, 200, 600, arcade.color.WHITE, 5)
    arcade.draw_line(400, 0, 400, 600, arcade.color.WHITE, 5)
    arcade.draw_line(0, 200, 600, 200, arcade.color.WHITE, 5)
    arcade.draw_line(0, 400, 600, 400, arcade.color.WHITE, 5)
    arcade.draw_line(0, 600, 600, 600, arcade.color.WHITE, 5)

    arcade.draw_text(str(ttt_player_1_score), 10, 700, arcade.color.RED, 100)
    arcade.draw_text(str(ttt_player_1_big_score), 130, 620, arcade.color.UNIVERSITY_OF_TENNESSEE_ORANGE, 200)

    arcade.draw_text(str(ttt_player_2_score), 520, 700, arcade.color.BLUE, 100)
    arcade.draw_text(str(ttt_player_2_big_score), 330, 620, arcade.color.PURPLE_MOUNTAIN_MAJESTY, 200)

    # Player 1 'O'

    # Player 1 bottom left
    if ttt_player_1_bottom_left:
        arcade.draw_circle_outline(ttt_positions[0][0][0],
                                   ttt_positions[0][0][1],
                                   ttt_positions[0][0][2],
                                   arcade.color.WHITE, 5)

    # Player 1 bottom middle
    if ttt_player_1_bottom_middle:
        arcade.draw_circle_outline(ttt_positions[0][1][0],
                                   ttt_positions[0][1][1],
                                   ttt_positions[0][1][2],
                                   arcade.color.WHITE, 5)

    # Player 1 bottom right
    if ttt_player_1_bottom_right:
        arcade.draw_circle_outline(ttt_positions[0][2][0],
                                   ttt_positions[0][2][1],
                                   ttt_positions[0][2][2],
                                   arcade.color.WHITE, 5)

    # Player 1 middle left
    if ttt_player_1_middle_left:
        arcade.draw_circle_outline(ttt_positions[0][3][0],
                                   ttt_positions[0][3][1],
                                   ttt_positions[0][3][2],
                                   arcade.color.WHITE, 5)

    # Player 1 middle middle
    if ttt_player_1_middle_middle:
        arcade.draw_circle_outline(ttt_positions[0][4][0],
                                   ttt_positions[0][4][1],
                                   ttt_positions[0][4][2],
                                   arcade.color.WHITE, 5)

    # Player 1 middle right
    if ttt_player_1_middle_right:
        arcade.draw_circle_outline(ttt_positions[0][5][0],
                                   ttt_positions[0][5][1],
                                   ttt_positions[0][5][2],
                                   arcade.color.WHITE, 5)

    # Player 1 top left
    if ttt_player_1_top_left:
        arcade.draw_circle_outline(ttt_positions[0][6][0],
                                   ttt_positions[0][6][1],
                                   ttt_positions[0][6][2],
                                   arcade.color.WHITE, 5)

    # Player 1 top middle
    if ttt_player_1_top_middle:
        arcade.draw_circle_outline(ttt_positions[0][7][0],
                                   ttt_positions[0][7][1],
                                   ttt_positions[0][7][2],
                                   arcade.color.WHITE, 5)

    # Player 1 top right
    if ttt_player_1_top_right:
        arcade.draw_circle_outline(ttt_positions[0][8][0],
                                   ttt_positions[0][8][1],
                                   ttt_positions[0][8][2],
                                   arcade.color.WHITE, 5)

    # Player 1 checking bottom row win
    if ttt_win_player_1_bottom_row:
        arcade.draw_line(ttt_positions[3][0][0],
                         ttt_positions[3][0][1],
                         ttt_positions[3][0][2],
                         ttt_positions[3][0][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking middle row win
    if ttt_win_player_1_middle_row:
        arcade.draw_line(ttt_positions[3][1][0],
                         ttt_positions[3][1][1],
                         ttt_positions[3][1][2],
                         ttt_positions[3][1][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking top row win
    if ttt_win_player_1_top_row:
        arcade.draw_line(ttt_positions[3][2][0],
                         ttt_positions[3][2][1],
                         ttt_positions[3][2][2],
                         ttt_positions[3][2][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking left column win
    if ttt_win_player_1_left_column:
        arcade.draw_line(ttt_positions[3][3][0],
                         ttt_positions[3][3][1],
                         ttt_positions[3][3][2],
                         ttt_positions[3][3][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking middle column win
    if ttt_win_player_1_middle_column:
        arcade.draw_line(ttt_positions[3][4][0],
                         ttt_positions[3][4][1],
                         ttt_positions[3][4][2],
                         ttt_positions[3][4][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking right column win
    if ttt_win_player_1_right_column:
        arcade.draw_line(ttt_positions[3][5][0],
                         ttt_positions[3][5][1],
                         ttt_positions[3][5][2],
                         ttt_positions[3][5][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking downward diagonal win
    if ttt_win_player_1_diagonal_downward:
        arcade.draw_line(ttt_positions[3][6][0],
                         ttt_positions[3][6][1],
                         ttt_positions[3][6][2],
                         ttt_positions[3][6][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Player 1 checking upward diagonal win
    if ttt_win_player_1_diagonal_upward:
        arcade.draw_line(ttt_positions[3][7][0],
                         ttt_positions[3][7][1],
                         ttt_positions[3][7][2],
                         ttt_positions[3][7][3],
                         arcade.color.RED, 5)
        ttt_point_won = True

        if ttt_game_win_player_1:
            ttt_player_1_score += 1
            ttt_game_win_player_1 = False

    # Drawing player 2 'X'

    # Player 2 bottom left
    if ttt_player_2_bottom_left:
        arcade.draw_line(ttt_positions[1][0][0],
                         ttt_positions[1][0][1],
                         ttt_positions[1][0][2],
                         ttt_positions[1][0][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][1][0],
                         ttt_positions[1][1][1],
                         ttt_positions[1][1][2],
                         ttt_positions[1][1][3],
                         arcade.color.WHITE, 5)

    # Player 2 bottom middle
    if ttt_player_2_bottom_middle:
        arcade.draw_line(ttt_positions[1][2][0],
                         ttt_positions[1][2][1],
                         ttt_positions[1][2][2],
                         ttt_positions[1][2][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][3][0],
                         ttt_positions[1][3][1],
                         ttt_positions[1][3][2],
                         ttt_positions[1][3][3],
                         arcade.color.WHITE, 5)

    # Player 2 bottom right
    if ttt_player_2_bottom_right:
        arcade.draw_line(ttt_positions[1][4][0],
                         ttt_positions[1][4][1],
                         ttt_positions[1][4][2],
                         ttt_positions[1][4][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][5][0],
                         ttt_positions[1][5][1],
                         ttt_positions[1][5][2],
                         ttt_positions[1][5][3],
                         arcade.color.WHITE, 5)

    # Player 2 middle left
    if ttt_player_2_middle_left:
        arcade.draw_line(ttt_positions[1][6][0],
                         ttt_positions[1][6][1],
                         ttt_positions[1][6][2],
                         ttt_positions[1][6][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][7][0],
                         ttt_positions[1][7][1],
                         ttt_positions[1][7][2],
                         ttt_positions[1][7][3],
                         arcade.color.WHITE, 5)

    # Player 2 middle middle
    if ttt_player_2_middle_middle:
        arcade.draw_line(ttt_positions[1][8][0],
                         ttt_positions[1][8][1],
                         ttt_positions[1][8][2],
                         ttt_positions[1][8][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][9][0],
                         ttt_positions[1][9][1],
                         ttt_positions[1][9][2],
                         ttt_positions[1][9][3],
                         arcade.color.WHITE, 5)

    # Player 2 middle right
    if ttt_player_2_middle_right:
        arcade.draw_line(ttt_positions[1][10][0],
                         ttt_positions[1][10][1],
                         ttt_positions[1][10][2],
                         ttt_positions[1][10][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][11][0],
                         ttt_positions[1][11][1],
                         ttt_positions[1][11][2],
                         ttt_positions[1][11][3],
                         arcade.color.WHITE, 5)

    # Player 2 top left
    if ttt_player_2_top_left:
        arcade.draw_line(ttt_positions[1][12][0],
                         ttt_positions[1][12][1],
                         ttt_positions[1][12][2],
                         ttt_positions[1][12][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][13][0],
                         ttt_positions[1][13][1],
                         ttt_positions[1][13][2],
                         ttt_positions[1][13][3],
                         arcade.color.WHITE, 5)

    # Player 2 top middle
    if ttt_player_2_top_middle:
        arcade.draw_line(ttt_positions[1][14][0],
                         ttt_positions[1][14][1],
                         ttt_positions[1][14][2],
                         ttt_positions[1][14][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][15][0],
                         ttt_positions[1][15][1],
                         ttt_positions[1][15][2],
                         ttt_positions[1][15][3],
                         arcade.color.WHITE, 5)

    # Player 2 top right
    if ttt_player_2_top_right:
        arcade.draw_line(ttt_positions[1][16][0],
                         ttt_positions[1][16][1],
                         ttt_positions[1][16][2],
                         ttt_positions[1][16][3],
                         arcade.color.WHITE, 5)

        arcade.draw_line(ttt_positions[1][17][0],
                         ttt_positions[1][17][1],
                         ttt_positions[1][17][2],
                         ttt_positions[1][17][3],
                         arcade.color.WHITE, 5)

    # Player 2 checking bottom row win
    if ttt_win_player_2_bottom_row:
        arcade.draw_line(ttt_positions[3][0][0],
                         ttt_positions[3][0][1],
                         ttt_positions[3][0][2],
                         ttt_positions[3][0][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking middle row win
    if ttt_win_player_2_middle_row:
        arcade.draw_line(ttt_positions[3][1][0],
                         ttt_positions[3][1][1],
                         ttt_positions[3][1][2],
                         ttt_positions[3][1][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking top row win
    if ttt_win_player_2_top_row:
        arcade.draw_line(ttt_positions[3][2][0],
                         ttt_positions[3][2][1],
                         ttt_positions[3][2][2],
                         ttt_positions[3][2][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking left column win
    if ttt_win_player_2_left_column:
        arcade.draw_line(ttt_positions[3][3][0],
                         ttt_positions[3][3][1],
                         ttt_positions[3][3][2],
                         ttt_positions[3][3][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking middle column win
    if ttt_win_player_2_middle_column:
        arcade.draw_line(ttt_positions[3][4][0],
                         ttt_positions[3][4][1],
                         ttt_positions[3][4][2],
                         ttt_positions[3][4][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking right column win
    if ttt_win_player_2_right_column:
        arcade.draw_line(ttt_positions[3][5][0],
                         ttt_positions[3][5][1],
                         ttt_positions[3][5][2],
                         ttt_positions[3][5][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking downward diagonal win
    if ttt_win_player_2_diagonal_downward:
        arcade.draw_line(ttt_positions[3][6][0],
                         ttt_positions[3][6][1],
                         ttt_positions[3][6][2],
                         ttt_positions[3][6][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False

    # Player 2 checking upward diagonal win
    if ttt_win_player_2_diagonal_upward:
        arcade.draw_line(ttt_positions[3][7][0],
                         ttt_positions[3][7][1],
                         ttt_positions[3][7][2],
                         ttt_positions[3][7][3],
                         arcade.color.BLUE, 5)
        ttt_point_won = True

        if ttt_game_win_player_2:
            ttt_player_2_score += 1
            ttt_game_win_player_2 = False


def on_mouse_press(x, y, button, modifiers):
    global ttt_player_1_top_left, ttt_player_1_top_middle, ttt_player_1_top_right
    global ttt_player_1_middle_left, ttt_player_1_middle_middle, ttt_player_1_middle_right
    global ttt_player_1_bottom_left, ttt_player_1_bottom_middle, ttt_player_1_bottom_right

    global ttt_player_1_turn

    global ttt_player_2_top_left, ttt_player_2_top_middle, ttt_player_2_top_right
    global ttt_player_2_middle_left, ttt_player_2_middle_middle, ttt_player_2_middle_right
    global ttt_player_2_bottom_left, ttt_player_2_bottom_middle, ttt_player_2_bottom_right

    global ttt_taken_top_left, ttt_taken_top_middle, ttt_taken_top_right
    global ttt_taken_middle_left, ttt_taken_middle_middle, ttt_taken_middle_right
    global ttt_taken_bottom_left, ttt_taken_bottom_middle, ttt_taken_bottom_right

    global ttt_player_2_turn

    global ttt_point_won, ttt_is_reset

    global ttt_positions

    # Player 1
    if ttt_positions[2][0][0] - 100 < x < ttt_positions[2][0][0] + 100 and \
            ttt_positions[2][0][1] - 100 < y < ttt_positions[2][0][1] + 100 \
            and ttt_player_1_turn and ttt_taken_bottom_left == 0 and not ttt_point_won:
        ttt_player_1_bottom_left = True
        ttt_player_2_bottom_left = False
        ttt_taken_bottom_left = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][1][0] - 100 < x < ttt_positions[2][1][0] + 100 and \
            ttt_positions[2][1][1] - 100 < y < ttt_positions[2][1][1] + 100 \
            and ttt_player_1_turn and ttt_taken_bottom_middle == 0 and not ttt_point_won:
        ttt_player_1_bottom_middle = True
        ttt_player_2_bottom_middle = False
        ttt_taken_bottom_middle = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][2][0] - 100 < x < ttt_positions[2][2][0] + 100 and \
            ttt_positions[2][2][1] - 100 < y < ttt_positions[2][2][1] + 100 \
            and ttt_player_1_turn and ttt_taken_bottom_right == 0 and not ttt_point_won:
        ttt_player_1_bottom_right = True
        ttt_player_2_bottom_right = False
        ttt_taken_bottom_right = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][3][0] - 100 < x < ttt_positions[2][3][0] + 100 and \
            ttt_positions[2][3][1] - 100 < y < ttt_positions[2][3][1] + 100 \
            and ttt_player_1_turn and ttt_taken_middle_left == 0 and not ttt_point_won:
        ttt_player_1_middle_left = True
        ttt_player_2_middle_left = False
        ttt_taken_middle_left = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][4][0] - 100 < x < ttt_positions[2][4][0] + 100 and \
            ttt_positions[2][4][1] - 100 < y < ttt_positions[2][4][1] + 100 \
            and ttt_player_1_turn and ttt_taken_middle_middle == 0 and not ttt_point_won:
        ttt_player_1_middle_middle = True
        ttt_player_2_middle_middle = False
        ttt_taken_middle_middle = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][5][0] - 100 < x < ttt_positions[2][5][0] + 100 and \
            ttt_positions[2][5][1] - 100 < y < ttt_positions[2][5][1] + 100 \
            and ttt_player_1_turn and ttt_taken_middle_right == 0 and not ttt_point_won:
        ttt_player_1_middle_right = True
        ttt_player_2_middle_right = False
        ttt_taken_middle_right = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][6][0] - 100 < x < ttt_positions[2][6][0] + 100 and \
            ttt_positions[2][6][1] - 100 < y < ttt_positions[2][6][1] + 100 \
            and ttt_player_1_turn and ttt_taken_top_left == 0 and not ttt_point_won:
        ttt_player_1_top_left = True
        ttt_player_2_top_left = False
        ttt_taken_top_left = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][7][0] - 100 < x < ttt_positions[2][7][0] + 100 and \
            ttt_positions[2][7][1] - 100 < y < ttt_positions[2][7][1] + 100 \
            and ttt_player_1_turn and ttt_taken_top_middle == 0 and not ttt_point_won:
        ttt_player_1_top_middle = True
        ttt_player_2_top_middle = False
        ttt_taken_top_middle = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    if ttt_positions[2][8][0] - 100 < x < ttt_positions[2][8][0] + 100 and \
            ttt_positions[2][8][1] - 100 < y < ttt_positions[2][8][1] + 100 \
            and ttt_player_1_turn and ttt_taken_top_right == 0 and not ttt_point_won:
        ttt_player_1_top_right = True
        ttt_player_2_top_right = False
        ttt_taken_top_right = 1
        ttt_player_2_turn = True
        ttt_player_1_turn = False

    # Player 2
    if ttt_positions[2][0][0] - 100 < x < ttt_positions[2][0][0] + 100 and \
            ttt_positions[2][0][1] - 100 < y < ttt_positions[2][0][1] + 100 \
            and ttt_player_2_turn and ttt_taken_bottom_left == 0 and not ttt_point_won:
        ttt_player_2_bottom_left = True
        ttt_player_1_bottom_left = False
        ttt_taken_bottom_left = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][1][0] - 100 < x < ttt_positions[2][1][0] + 100 and \
            ttt_positions[2][1][1] - 100 < y < ttt_positions[2][1][1] + 100 \
            and ttt_player_2_turn and ttt_taken_bottom_middle == 0 and not ttt_point_won:
        ttt_player_2_bottom_middle = True
        ttt_player_1_bottom_middle = False
        ttt_taken_bottom_middle = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][2][0] - 100 < x < ttt_positions[2][2][0] + 100 and \
            ttt_positions[2][2][1] - 100 < y < ttt_positions[2][2][1] + 100 \
            and ttt_player_2_turn and ttt_taken_bottom_right == 0 and not ttt_point_won:
        ttt_player_2_bottom_right = True
        ttt_player_1_bottom_right = False
        ttt_taken_bottom_right = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][3][0] - 100 < x < ttt_positions[2][3][0] + 100 and \
            ttt_positions[2][3][1] - 100 < y < ttt_positions[2][3][1] + 100 \
            and ttt_player_2_turn and ttt_taken_middle_left == 0 and not ttt_point_won:
        ttt_player_2_middle_left = True
        ttt_player_1_middle_left = False
        ttt_taken_middle_left = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][4][0] - 100 < x < ttt_positions[2][4][0] + 100 and \
            ttt_positions[2][4][1] - 100 < y < ttt_positions[2][4][1] + 100 \
            and ttt_player_2_turn and ttt_taken_middle_middle == 0 and not ttt_point_won:
        ttt_player_2_middle_middle = True
        ttt_player_1_middle_middle = False
        ttt_taken_middle_middle = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][5][0] - 100 < x < ttt_positions[2][5][0] + 100 and \
            ttt_positions[2][5][1] - 100 < y < ttt_positions[2][5][1] + 100\
            and ttt_player_2_turn and ttt_taken_middle_right == 0 and not ttt_point_won:
        ttt_player_2_middle_right = True
        ttt_player_1_middle_right = False
        ttt_taken_middle_right = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][6][0] - 100 < x < ttt_positions[2][6][0] + 100 and \
            ttt_positions[2][6][1] - 100 < y < ttt_positions[2][6][1] + 100 \
            and ttt_player_2_turn and ttt_taken_top_left == 0 and not ttt_point_won:
        ttt_player_2_top_left = True
        ttt_player_1_top_left = False
        ttt_taken_top_left = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][7][0] - 100 < x < ttt_positions[2][7][0] + 100 and \
            ttt_positions[2][7][1] - 100 < y < ttt_positions[2][7][1] + 100 \
            and ttt_player_2_turn and ttt_taken_top_middle == 0 and not ttt_point_won:
        ttt_player_2_top_middle = True
        ttt_player_1_top_middle = False
        ttt_taken_top_middle = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if ttt_positions[2][8][0] - 100 < x < ttt_positions[2][8][0] + 100 and \
            ttt_positions[2][8][1] - 100 < y < ttt_positions[2][8][1] + 100 \
            and ttt_player_2_turn and ttt_taken_top_right == 0 and not ttt_point_won:
        ttt_player_2_top_right = True
        ttt_player_1_top_right = False
        ttt_taken_top_right = 2
        ttt_player_1_turn = True
        ttt_player_2_turn = False

    if 0 < x < 600 and 0 < y < 600 and ttt_point_won:
        ttt_is_reset = True


def ttt_reset(resetting):
    global ttt_player_1_top_left, ttt_player_1_top_middle, ttt_player_1_top_right
    global ttt_player_1_middle_left, ttt_player_1_middle_middle, ttt_player_1_middle_right
    global ttt_player_1_bottom_left, ttt_player_1_bottom_middle, ttt_player_1_bottom_right

    global ttt_win_player_1_bottom_row, ttt_win_player_1_middle_row, ttt_win_player_1_top_row
    global ttt_win_player_1_left_column, ttt_win_player_1_middle_column, ttt_win_player_1_right_column
    global ttt_win_player_1_diagonal_downward, ttt_win_player_1_diagonal_upward

    global ttt_player_2_top_left, ttt_player_2_top_middle, ttt_player_2_top_right
    global ttt_player_2_middle_left, ttt_player_2_middle_middle, ttt_player_2_middle_right
    global ttt_player_2_bottom_left, ttt_player_2_bottom_middle, ttt_player_2_bottom_right

    global ttt_win_player_2_bottom_row, ttt_win_player_2_middle_row, ttt_win_player_2_top_row
    global ttt_win_player_2_left_column, ttt_win_player_2_middle_column, ttt_win_player_2_right_column
    global ttt_win_player_2_diagonal_downward, ttt_win_player_2_diagonal_upward

    global ttt_taken_bottom_left, ttt_taken_bottom_middle, ttt_taken_bottom_right
    global ttt_taken_middle_left, ttt_taken_middle_middle, ttt_taken_middle_right
    global ttt_taken_top_left, ttt_taken_top_middle, ttt_taken_top_right

    global ttt_game_win_player_1, ttt_game_win_player_2, ttt_win_condition, ttt_point_won

    global ttt_player_1_score, ttt_max_score, ttt_player_1_big_score
    global ttt_player_2_score, ttt_player_2_big_score

    global ttt_player_1_game_win, ttt_player_2_game_win
    global ttt_player_1_turn, ttt_player_2_turn

    global ttt_is_reset

    if resetting:
        # Player 1 variables
        ttt_player_1_top_left = False
        ttt_player_1_top_middle = False
        ttt_player_1_top_right = False

        ttt_player_1_middle_left = False
        ttt_player_1_middle_middle = False
        ttt_player_1_middle_right = False

        ttt_player_1_bottom_left = False
        ttt_player_1_bottom_middle = False
        ttt_player_1_bottom_right = False

        # Player 1 win cases
        ttt_win_player_1_bottom_row = False
        ttt_win_player_1_middle_row = False
        ttt_win_player_1_top_row = False

        ttt_win_player_1_left_column = False
        ttt_win_player_1_middle_column = False
        ttt_win_player_1_right_column = False

        ttt_win_player_1_diagonal_downward = False
        ttt_win_player_1_diagonal_upward = False

        # Player 2 variables
        ttt_player_2_top_left = False
        ttt_player_2_top_middle = False
        ttt_player_2_top_right = False

        ttt_player_2_middle_left = False
        ttt_player_2_middle_middle = False
        ttt_player_2_middle_right = False

        ttt_player_2_bottom_left = False
        ttt_player_2_bottom_middle = False
        ttt_player_2_bottom_right = False

        # Player 2 win cases
        ttt_win_player_2_bottom_row = False
        ttt_win_player_2_middle_row = False
        ttt_win_player_2_top_row = False

        ttt_win_player_2_left_column = False
        ttt_win_player_2_middle_column = False
        ttt_win_player_2_right_column = False

        ttt_win_player_2_diagonal_downward = False
        ttt_win_player_2_diagonal_upward = False

        # Variables to determine which player has what box
        # A value of 1 means that player 1 holds the space
        # A value of 2 means that player 2 hold the space
        ttt_taken_bottom_left = 0
        ttt_taken_bottom_middle = 0
        ttt_taken_bottom_right = 0

        ttt_taken_middle_left = 0
        ttt_taken_middle_middle = 0
        ttt_taken_middle_right = 0

        ttt_taken_top_left = 0
        ttt_taken_top_middle = 0
        ttt_taken_top_right = 0

        ttt_game_win_player_1 = False
        ttt_game_win_player_2 = False
        ttt_win_condition = True
        ttt_point_won = False

        if ttt_player_1_score == ttt_max_score:
            ttt_player_1_big_score += 1
            ttt_player_1_score = 0
            ttt_player_2_score = 0

        if ttt_player_2_score == ttt_max_score:
            ttt_player_2_big_score += 1
            ttt_player_1_score = 0
            ttt_player_2_score = 0

        if ttt_player_1_big_score == 5:
            ttt_player_1_game_win = True

        if ttt_player_2_big_score == 5:
            ttt_player_2_game_win = True

        who_won_player_1 = False
        who_won_player_2 = False

        if ttt_player_1_wins and who_won_player_1 and not who_won_player_2:
            ttt_player_1_turn = False
            ttt_player_2_turn = True
            who_won_player_1 = True
            who_won_player_2 = False

        if ttt_player_2_wins and who_won_player_2 and not who_won_player_1:
            ttt_player_1_turn = True
            ttt_player_2_turn = False
            who_won_player_2 = True
            who_won_player_1 = False

        ttt_is_reset = False


def setup():
    arcade.open_window(ttt_screen_width, ttt_screen_height, ttt_screen_title)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_mouse_press = on_mouse_press

    arcade.run()


setup()
