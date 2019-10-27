import arcade

# the width and height of the window
WIDTH = 500
HEIGHT = 500

# displays the current screen
# if this variable is changed, the screen will change too
# 0 == inital screen
# 1 == next screen
current_screen = 0

# turns true when button is clicked
button_screen_0 = False

def on_update(delta_time):
    # current_screen is globaled because we change the value of current_screen = 0 to current_screen = 1
    global current_screen

    # if the current_screen is 0 (inital screen)and the button on the screen is clicked:
    if current_screen == 0 and button_screen_0:
        # change the current_screen to 1 (change it to the next screen)
        current_screen = 1


def on_draw():
    arcade.start_render()
    
    # if the current_screen is 0, draw the inital screen
    if current_screen == 0:
        inital_screen()

    # if the current_screen is 1, draw the next screen
    if current_screen == 1:
        next_screen()


def on_mouse_press(x, y, button, modifiers):
    # button_screen_0 is globaled because we change it from "False" to "True"
    global button_screen_0

    # This checks the box that's drawn for any mouse presses:
    if (100 < x < 400) and (100 < y < 400):
        # Therefore turning the button_screen_0 to "True", which means the button has been pressed
        button_screen_0 = True


# The inital screen function
def inital_screen():
    arcade.draw_rectangle_filled(250, 250, 300, 300, arcade.color.WHITE)
    arcade.draw_text("Inital Screen", 250, 250, arcade.color.BLACK, 20, 200, "center", 'Arial', True, False, "center", "center")


# The next screen function
def next_screen():
    arcade.draw_rectangle_filled(250, 250, 300, 300, arcade.color.LIGHT_BLUE)
    arcade.draw_text("Next Screen", 250, 250, arcade.color.BLACK, 20, 200, "center", 'Arial', True, False, "center", "center")


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
