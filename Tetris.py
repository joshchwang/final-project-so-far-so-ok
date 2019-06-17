import arcade
import random

screen_width = 600
screen_height = 800

blocks = [
    # I block - cyan
    [
        # Upright
        [40, 160],

        # Turned
        [160, 40]
    ],

    # O block - golden yellow
    [
        # Doesn't need more then one given value
        # Because it's a 4 x 4 block
        [160, 160]
    ],

    # T block -

]


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()

    # Divider between the future blocks and the game
    arcade.draw_rectangle_outline(400, 400, 10, 800, arcade.color.WHITE)

    # Top Divider between points and whatnot and the game
    arcade.draw_rectangle_outline(195, 720, 400, 10, arcade.color.WHITE)

    # The next box
    arcade.draw_rectangle_outline(503, 650, 160, 160, arcade.color.WHITE)
    arcade.draw_rectangle_outline(503, 650, 150, 150, arcade.color.WHITE)
    arcade.draw_text("N E X T", 430, 745, arcade.color.WHITE, 40)

    arcade.draw_rectangle_outline(20, 80, 40, 160, arcade.color.GOLDEN_YELLOW)


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

    arcade.run()


if __name__ == '__main__':
    setup()
