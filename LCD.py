from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas

# Explicit 4-wire SPI setup
serial = spi(
    port=0,           # SPI bus
    device=0,         # CE0
    gpio_DC=25,       # Data/Command
    gpio_RST=5,       # Reset
    gpio_CS=8         # Chip select
)

device = ssd1306(serial, width=128, height=64)

with canvas(device) as draw:
    draw.text((30, 25), "1234", fill="white")
