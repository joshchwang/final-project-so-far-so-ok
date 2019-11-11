import arcade

# Screen
screen_width = 500
screen_height = 700
screen_title = "Donkey Kong"

mario_pos_x = 65          # X pos
mario_pos_y = 55          # Y pos
mario_pressed_up = False     # Up press
mario_pressed_down = False     # Down press
mario_pressed_left = False     # Left press
mario_pressed_right = False     # Right press
mario_touching_ladder = False     # Touching ladder
mario_touching_platform = False     # Touching platform
mario_alive = True        # is alive

def mario():
    arcade.draw_rectangle_outline(mario_pos_x, mario_pos_y, 25, 25, arcade.color.RED)


def luigi():
    arcade.draw_rectangle_outline


def on_update(delta_time: float):
    """ Updates every 1/60 a second.

    Args:
        delta_time (float): increases by one everytime
                            it is called.

    """
    pass


def on_draw():
    """ Draws.
    """
    mario()


def collision():
    """ Collision detection.
    """
    # arcade.are_polygons_intersecting()
    pass


def on_key_press(key, modifiers):
    """ Key press functionality

    Args:
        key (int): Key that was hit.
        modifiers (int): If it was shift/ctrl/alt.
    """
    pass


def on_key_release(key, modifiers):
    """ Key release functionality.

    Args:
        key (int): Key that was hit.
        modifiers (int): If it was shift/ctrl/alt.
    """
    pass

def on_mouse_press(x: float, y: float, button: int,
                   modifiers: int):
    """ Mouse button functionality.

    Args:
        x (float): x position of the mouse.
        y (float): y position of the mouse.
        button (int): What button was hit. One of:
                      arcade.MOUSE_BUTTON_LEFT,
                      arcade.MOUSE_BUTTON_RIGHT,
                      arcade.MOUSE_BUTTON_MIDDLE
        modifiers (int): Shift/click, ctrl/click, etc.
    """
    pass


def on_mouse_release(x: float, y: float, button: int,
                     modifiers: int):
    """ Mouse button functionality.

    Args:
    x (float): nothing.
    y (float): nothing.
    button (int): nothing.
    modifiers (int): nothing.
    """

def setup():
    """ The final setup before the code is run.
    """

    arcade.open_window(screen_width, screen_height,
                       screen_title)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


if __name__ == "__main__":
    setup()
