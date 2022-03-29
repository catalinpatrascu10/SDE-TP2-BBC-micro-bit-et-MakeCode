index = 0

def on_button_pressed_a():
    global index
    index = 4
    while index >= 0:
        led.plot(index, index)
        basic.pause(500)
        index += -1
        led.plot(index, index)
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)
