def on_button_pressed_a():
    radio.send_string("Start")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("Stop")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_string("Hello!")
basic.forever(on_forever)
