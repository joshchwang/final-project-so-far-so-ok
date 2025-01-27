import arcade
import random

width = 20
height = 20
margin = 2
row_count = 24
column_count = 10
grid = []
screen_width = (width + margin) * column_count + margin + 200
screen_height = (height + margin) * row_count + margin

# inversions controls what inversion the block is,
# if the inversion is:
# 0 - Upright
# 1 - On its right side
# 2 - Upside down
# 3 - On its left side
inversions = 0

is_block_selected = False
x_pos_block = 0
y_pos_block = 0


pressed_turn_right = False
pressed_turn_left = False
pressed_turn_down = False

pressed_move_right = False
pressed_move_left = False
pressed_move_down = False


def on_update(delta_time):
    global pressed_turn_down, pressed_turn_right, pressed_turn_left
    global pressed_move_down, pressed_move_right, pressed_move_left

    global inversions

    if pressed_turn_right:
        if inversions == 3:
            inversions = 0
        else:
            inversions += 1

        pressed_turn_right = False
        print(inversions)

    if pressed_turn_left:
        if inversions == 0:
            inversions = 3
        else:
            inversions -= 1
        pressed_turn_left = False
        print(inversions)


def on_draw():
    arcade.start_render()

    for row in range(row_count):
        for column in range(column_count):
            color = arcade.color.BLACK
            if grid[row][column] == 0:
                color = arcade.color.BLACK
            elif grid[row][column] == 1:
                color = arcade.color.WHITE
            elif grid[row][column] == 2:
                color = arcade.color.CYAN
            elif grid[row][column] == 3:
                color = arcade.color.SUNGLOW
            elif grid[row][column] == 4:
                color = arcade.color.PURPLE_MOUNTAIN_MAJESTY
            elif grid[row][column] == 5:
                color = arcade.color.GREEN
            elif grid[row][column] == 6:
                color = arcade.color.BOSTON_UNIVERSITY_RED
            elif grid[row][column] == 7:
                color = arcade.color.CERULEAN_BLUE
            elif grid[row][column] == 8:
                color = arcade.color.UNIVERSITY_OF_TENNESSEE_ORANGE
            arcade.draw_rectangle_outline((margin + width) * column + margin + width / 2,
                                          (margin + height) * row + margin + height / 2,
                                          width, height, color)

    arcade.draw_rectangle_outline(screen_width - 100, screen_height - 120, 90, 90, arcade.color.WHITE)
    arcade.draw_rectangle_outline(screen_width - 100, screen_height - 120, 75, 75, arcade.color.WHITE)

    blocks(21, 5, inversions, 0)


def on_key_press(key, modifiers):
    global pressed_turn_down, pressed_turn_right, pressed_turn_left
    global pressed_move_down, pressed_move_right, pressed_move_left

    # Turning the block
    if key == arcade.key.A:
        pressed_turn_left = True

    if key == arcade.key.D:
        pressed_turn_right = True

    if key == arcade.key.S:
        pressed_turn_down = True

    # Moving the block
    if key == arcade.key.LEFT:
        pressed_move_left = True

    if key == arcade.key.RIGHT:
        pressed_move_right = True

    if key == arcade.key.DOWN:
        pressed_move_down = True


def on_key_release(key, modifiers):
    global pressed_turn_down, pressed_turn_right, pressed_turn_left
    global pressed_move_down, pressed_move_right, pressed_move_left

    # Turning the block
    if key == arcade.key.A:
        pressed_turn_left = False

    if key == arcade.key.D:
        pressed_turn_right = False

    if key == arcade.key.S:
        pressed_turn_down = False

    # Moving the block
    if key == arcade.key.LEFT:
        pressed_move_left = False

    if key == arcade.key.RIGHT:
        pressed_move_right = False

    if key == arcade.key.DOWN:
        pressed_move_down = False


def on_mouse_press(x, y, button, modifiers):
    pass


def collision(row, column, block, invert):
    global is_block_selected

    # 'I' Block
    if block == 0:
        if invert == 0 or invert == 2:
            if grid[row - 2][column] <= 0:
                grid[row][column] = grid[row + 1][column]
                is_block_selected = False
        if invert == 1 or invert == 3:
            if grid[row - 1][column - 2] <= 0:
                is_block_selected = False

    # 'O' Block
    if block == 1:
        if row - 2 <= 0:
            row += 1
            is_block_selected = False

    # 'T' Block
    if block == 2:
        if invert == 0:
            if row - 1 <= 0:
                is_block_selected = False
        if invert == 1:
            if row - 2 <= 0:
                row += 1
                is_block_selected = False
        if invert == 2:
            if row - 2 <= 0:
                row += 1
                is_block_selected = False
        if invert == 3:
            if row - 2 <= 0:
                row += 1
                is_block_selected = False

    # S' Block
    if block == 3:
        if invert == 0 or invert == 2:
            if row - 2 <= 0:
                row = 0
                is_block_selected = False
        if invert == 1 or invert == 3:
            pass


def block_i(row, column, invert):
    # Upright or inverted
    if invert == 0 or invert == 2:
        # Drawing the other inversion state into neutral cells
        grid[row][column - 2] = 0
        grid[row][column - 1] = 0
        grid[row][column + 1] = 0

        # Drawing the inversion state
        grid[row - 1][column] = 2
        grid[row][column] = 2
        grid[row + 1][column] = 2
        grid[row + 2][column] = 2

    # Left or right
    if invert == 1 or invert == 3:
        # Drawing the other inversion state into neutral cells
        grid[row - 1][column] = 0
        grid[row + 1][column] = 0
        grid[row + 2][column] = 0

        # Drawing the inversion state
        grid[row][column - 2] = 2
        grid[row][column - 1] = 2
        grid[row][column] = 2
        grid[row][column + 1] = 2


def block_o(row, column):
    grid[row][column] = 3
    grid[row - 1][column] = 3
    grid[row][column + 1] = 3
    grid[row - 1][column + 1] = 3


def block_t(row, column, invert):
    # Upright
    if invert == 0:
        # Drawing the other inversion states into neutral cells
        grid[row - 1][column] = 0

        # Drawing the inversion state
        grid[row][column - 1] = 4
        grid[row][column] = 4
        grid[row][column + 1] = 4
        grid[row + 1][column] = 4

    # On its right side
    if invert == 1:
        # Drawing the other inversion states into neutral cells
        grid[row][column - 1] = 0

        # Drawing the inversion state
        grid[row + 1][column] = 4
        grid[row][column] = 4
        grid[row - 1][column] = 4
        grid[row][column + 1] = 4

    # Inverted
    if invert == 2:
        # Drawing the other inversion states into neutral cells
        grid[row + 1][column] = 0

        # Drawing the inversion state
        grid[row][column - 1] = 4
        grid[row][column] = 4
        grid[row][column + 1] = 4
        grid[row - 1][column] = 4

    # On its left side
    if invert == 3:
        # Drawing the other inversion states into neutral cells
        grid[row][column + 1] = 0

        # Drawing the inversion state
        grid[row + 1][column] = 4
        grid[row][column] = 4
        grid[row - 1][column] = 4
        grid[row][column - 1] = 4


def block_s(row, column, invert):
    # Upright or inverted
    if invert == 0 or invert == 2:
        # Drawing the other inversion state into neutral cells
        grid[row + 1][column] = 0
        grid[row - 1][column + 1] = 0

        # Drawing the inversion state
        grid[row - 1][column - 1] = 5
        grid[row - 1][column] = 5
        grid[row][column] = 5
        grid[row][column + 1] = 5

    if invert == 1 or invert == 3:
        # Drawing the other inversion state into neutral cells
        grid[row - 1][column - 1] = 0
        grid[row - 1][column] = 0

        # Drawing the inversion state
        grid[row + 1][column] = 5
        grid[row][column] = 5
        grid[row][column + 1] = 5
        grid[row - 1][column + 1] = 5


def block_z(row, column, invert):
    # Upright or inverted
    if invert == 0 or invert == 2:
        # Drawing the other inversion state into neutral cells
        grid[row][column + 1] = 0
        grid[row + 1][column + 1] = 0

        # Drawing the inversion state
        grid[row][column - 1] = 6
        grid[row][column] = 6
        grid[row - 1][column] = 6
        grid[row - 1][column + 1] = 6

    if invert == 1 or invert == 3:
        # Drawing the other inversion state into neutral cells
        grid[row][column - 1] = 0
        grid[row - 1][column + 1] = 0

        # Drawing the inversion state
        grid[row - 1][column] = 6
        grid[row][column] = 6
        grid[row][column + 1] = 6
        grid[row + 1][column + 1] = 6


def block_j(row, column, invert):
    # Upright
    if invert == 0:
        # Drawing the other inversion states into neutral cells
        grid[row + 1][column - 1] = 0
        grid[row][column - 1] = 0
        grid[row][column + 1] = 0
        grid[row - 1][column + 1] = 0

        # Drawing the inversion state
        grid[row - 1][column - 1] = 7
        grid[row - 1][column] = 7
        grid[row][column] = 7
        grid[row + 1][column] = 7

    # On its right side
    if invert == 1:
        # Drawing the other inversion states into neutral cells
        grid[row - 1][column - 1] = 0
        grid[row - 1][column] = 0
        grid[row + 1][column] = 0
        grid[row + 1][column + 1] = 0

        # Drawing the inversion state
        grid[row + 1][column - 1] = 7
        grid[row][column - 1] = 7
        grid[row][column] = 7
        grid[row][column + 1] = 7

    # Inverted
    if invert == 2:
        # Drawing the other inversion states into neutral cells
        grid[row + 1][column - 1] = 0
        grid[row][column - 1] = 0
        grid[row][column + 1] = 0
        grid[row - 1][column + 1] = 0

        # Drawing the inversion state
        grid[row - 1][column] = 7
        grid[row][column] = 7
        grid[row + 1][column] = 7
        grid[row + 1][column + 1] = 7

    # On its left side
    if invert == 3:
        # Drawing the other inversion states into neutral cells
        grid[row - 1][column - 1] = 0
        grid[row - 1][column] = 0
        grid[row + 1][column] = 0
        grid[row + 1][column + 1] = 0

        # Drawing the inversion state
        grid[row][column - 1] = 7
        grid[row][column] = 7
        grid[row][column + 1] = 7
        grid[row - 1][column + 1] = 7


def block_l(row, column, invert):
    # Upright
    if invert == 0:
        # Drawing the other inversion states into neutral cells
        grid[row - 1][column - 1] = 0
        grid[row][column - 1] = 0
        grid[row][column + 1] = 0
        grid[row + 1][column + 1] = 0

        # Drawing the inversion state
        grid[row + 1][column] = 8
        grid[row][column] = 8
        grid[row - 1][column] = 8
        grid[row - 1][column + 1] = 8

    # On its right side
    if invert == 1:
        # Drawing the other inversion states into neutral cells
        grid[row + 1][column - 1] = 0
        grid[row + 1][column] = 0
        grid[row - 1][column] = 0
        grid[row - 1][column + 1] = 0

        # Drawing the inversion state
        grid[row - 1][column - 1] = 8
        grid[row][column - 1] = 8
        grid[row][column] = 8
        grid[row][column + 1] = 8

    # Inverted
    if invert == 2:
        # Drawing the other inversion states into neutral cells
        grid[row - 1][column - 1] = 0
        grid[row][column - 1] = 0
        grid[row][column + 1] = 0
        grid[row + 1][column + 1] = 0

        # Drawing the inversion state
        grid[row + 1][column - 1] = 8
        grid[row + 1][column] = 8
        grid[row][column] = 8
        grid[row - 1][column] = 8

    # On its left side
    if invert == 3:
        # Drawing the other inversion states into neutral cells
        grid[row + 1][column - 1] = 0
        grid[row + 1][column] = 0
        grid[row - 1][column] = 0
        grid[row - 1][column + 1] = 0

        # Drawing the inversion state
        grid[row][column - 1] = 8
        grid[row][column] = 8
        grid[row][column + 1] = 8
        grid[row + 1][column + 1] = 8


def blocks(row, column, invert, block):
    # 'I' Block
    if block == 0:
        block_i(row, column, invert)

    # 'O' Block
    if block == 1:
        block_o(row, column)

    # 'T' Block
    if block == 2:
        block_t(row, column, invert)

    # 'S' Block
    if block == 3:
        block_s(row, column, invert)

    # 'Z' Block
    if block == 4:
        block_z(row, column, invert)

    # 'J' Block
    if block == 5:
        block_j(row, column, invert)

    # 'L' Block
    if block == 6:
        block_l(row, column, invert)


def setup():
    arcade.open_window(screen_width, screen_height, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    # create a 10 x 10 2D list of numbers

    # --- Populate grid the grid
    # Loop for each row
    for row in range(row_count):
        # For each row, create a list that will
        # represent an entire row
        grid.append([])
        # Loop for each column
        for column in range(column_count):
            # Add a the number zero to the current row
            grid[row].append(0)

    arcade.run()


if __name__ == '__main__':
    setup()
