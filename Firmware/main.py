import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digitalio import DigitalioScanner
from kmk.extensions.peg_oled import Oled, OledDisplayMode, OledReactionType
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Pins matrix
# Order of pins mapped to keys: SW2, SW3, SW4, SW5, SW6, SW7, SW1(S1 button)
# All switches pull down to GND when pressed
keyboard.matrix = DigitalioScanner(
    pins=[board.D2, board.D1, board.D0, board.D3, board.D4, board.D7, board.D10],
    value_when_pressed=False, # False means Active Low (connecting to GND)
    pull=True
)

# rotry encoder config
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# SW1 A -> pin D9, SW1 B -> pin D8
encoder_handler.pins = (
    (board.D9, board.D8, None, False), # (pin_A, pin_B, click_pin, inverted)
)

# Oled configurations
# J1 VCC -> 3V3, GND -> GND, SCL -> D5, SDA -> D4
oled_ext = Oled(
    OledDisplayMode.TXT,
    to_display=OledReactionType.LAYER,
    device_address=0x3C # Standard I2C address for SSD1306 OLEDs
)
keyboard.extensions.append(oled_ext)

# Keymap definitions
# Matches the order specified in DigitalioScanner + Encoder turns
keyboard.keymap = [
    [
        # Physical Keys: SW2,  SW3,  SW4,  SW5,  SW6,  SW7,  SW1 Click
                        KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.MUTE
    ]
]

# Encoder rotation maps: [ (Counter-Clockwise, Clockwise) ]
encoder_handler.map = [
    [ (KC.VOLD, KC.VOLU) ] # Layer 0: Vol Down / Vol Up
]

if __name__ == '__main__':
    keyboard.go()