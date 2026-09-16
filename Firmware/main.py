import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Tap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
macros = Macros()
encoders = EncoderHandler()
keyboard.modules = [macros, encoders]
keyboard.extensions = [MediaKeys()]

keyboard.row_pins = (board.D7, board.D10)
keyboard.col_pins = (board.D9, board.D8, board.D6)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

git_add = KC.MACRO("git add .", Tap(KC.ENTER))
git_commit = KC.MACRO('git commit -m "update"', Tap(KC.ENTER))
git_push = KC.MACRO("git push", Tap(KC.ENTER))
keyboard.keymap = [[
    git_add, git_commit, git_push,
    KC.A, KC.B, KC.C,
]]

encoders.pins = (
    (board.D0, board.D1, board.D2),
    (board.D3, board.D4, board.D5),
)
encoders.map = [(
    (KC.UP, KC.DOWN, KC.MUTE),
    (KC.PGUP, KC.PGDN, KC.MEDIA_PLAY_PAUSE),
)]

print("Hackpad Git keymap starting: Add / Commit / Push; A / B / C")
if __name__ == "__main__":
    keyboard.go()
