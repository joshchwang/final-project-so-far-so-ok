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


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()

    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] == 0:
                color = arcade.color.WHITE
            elif grid[row][column] == 1:
                color = arcade.color.BLACK
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


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


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
