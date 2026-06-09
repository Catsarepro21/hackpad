import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode

keyboard = KMKKeyboard()

macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules = [macros, encoder_handler]

# --- MATRIX CONFIG ---
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
# Format: (PAD_A, PAD_B, BUTTON_PIN)
# Change the GP pins below to match your actual hardware layout
encoder_handler.pins = (
    (board.GP14, board.GP15, board.GP16), 
    (board.GP17, board.GP18, board.GP19), 
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
# Replace GP1 and GP0 with your board's specific SCL and SDA pins
i2c_bus = busio.I2C(board.GP1, board.GP0) 

oled_ext = Oled(
    i2c_bus,
    features=[], 
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

# Screen coordinates: (column, row, text)
oled_ext.write_ln(0, 0, "HACKPAD v1.0")
oled_ext.write_ln(0, 1, "Ready")

if __name__ == "__main__":
    keyboard.go()