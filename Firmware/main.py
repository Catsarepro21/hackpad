import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledData

keyboard = KMKKeyboard()

macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules = [macros, encoder_handler]

# --- MATRIX CONFIG ---
# 3 MX mechanical switches
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- GIT MACROS ---
GIT_ADD = KC.M("git add .\n")
GIT_COMMIT = KC.M('git commit -m "update"\n')
GIT_PUSH = KC.M("git push\n")

keyboard.keymap = [
    [GIT_ADD, GIT_COMMIT, GIT_PUSH],
]

# --- ROTARY ENCODERS ---
# Seeed Studio XIAO RP2040 Pin Mapping:
# Encoder 1: D6 (A), D7 (B), D8 (Push Button)
# Encoder 2: D9 (A), D10 (B), None (or shared D8)
encoder_handler.pins = (
    (board.D6, board.D7, board.D8), 
    (board.D9, board.D10, None), 
)

# Format: ((Enc1_Left, Enc1_Right, Enc1_Click), (Enc2_Left, Enc2_Right, Enc2_Click))
# Arrow keys/Page up down are used here to handle scrolling through git diffs/logs
encoder_handler.map = [
    (
        (KC.UP, KC.DOWN, KC.MUTE),          
        (KC.PGUP, KC.PGDN, KC.MEDIA_PLAY_PAUSE), 
    ),
]

# --- OLED DISPLAY (I2C) ---
# Seeed Studio XIAO RP2040 hardware I2C pins (D4 = SDA, D5 = SCL)
i2c_bus = busio.I2C(board.SCL, board.SDA) 

oled_data = OledData(
    corner_one={
        0: OledDisplayMode.TXT,
        1: "HACKPAD v1.0",
    },
    corner_two={
        0: OledDisplayMode.TXT,
        1: "Ready",
    },
)

oled_ext = Oled(
    oled_data,
    toDisplay=OledDisplayMode.TXT,
    flip=False,
    i2c=i2c_bus,
)
keyboard.extensions.append(oled_ext)

if __name__ == "__main__":
    keyboard.go()