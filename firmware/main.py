import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# TODO: remember to put the correct pins!!!!!
PINS = [board.1, board.2, board.3, board.4, board.5, board.6, board.7, board.8]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# TODO: find out what funny things you can make with these
# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.F20]
]

if __name__ == '__main__':
    keyboard.go()