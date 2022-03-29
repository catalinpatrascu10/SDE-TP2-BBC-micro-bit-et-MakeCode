def on_button_pressed_a():
    list2[randint(0, len(list2))].show_image(0)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

list2: List[Image] = []
list2 = [images.icon_image(IconNames.HEART),
    images.icon_image(IconNames.TSHIRT),
    images.icon_image(IconNames.LEFT_TRIANGLE),
    images.icon_image(IconNames.YES)]