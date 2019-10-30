import arcade

# Screen Variables
screen_width = 500
screen_height = 700
screen_title = "Donkey Kong"

def on_update(delta_time):
    """
    Updates the code constantly

    :param delta_time:
    :return:
    """
    pass


def on_draw():
    """
    Drawing everything

    :return:
    """
    pass


def collision():
    """
    Collision

    :return:
    """
    pass


def on_key_press(key, modifiers):
    """
    Checking for key presses

    :param key:
    :param modifiers:
    :return:
    """
    pass


def on_key_release(key, modifiers):
    """
    Checking for key releases

    :param key:
    :param modifiers:
    :return:
    """
    pass

def setup():
    """
    The final setup before the code is run

    :return:
    """

    arcade.open_window(screen_width, screen_height, screen_title)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()

if __name__ == "__main__":
    setup()
