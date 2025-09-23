from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas

# SPI setup (update pins if needed)
serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=5, gpio_CS=8)

device = ssd1306(serial, width=128, height=64)

with canvas(device) as draw:
    draw.text((10, 20), "Hello Pi!", fill="white")

