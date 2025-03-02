import sys
import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

def clear_oled():
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)
    device.clear()

if __name__ == "__main__":
    try:
        clear_oled()
        time.sleep(1)  # Ensure the display is cleared
    except Exception as e:
        print(f"Error clearing OLED: {e}", file=sys.stderr)

