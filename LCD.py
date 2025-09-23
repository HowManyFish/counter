from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
import time

serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=5, gpio_CS=8)
device = ssd1306(serial, width=128, height=64)

# Fill screen completely
device.clear()
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="white")

time.sleep(5)

# Clear screen
device.clear()
