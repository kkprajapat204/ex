def on_pin_pressed_p0():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

basic.show_icon(IconNames.SCISSORS)

def on_forever():
    pass
basic.forever(on_forever)
