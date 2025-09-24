from hcsr04sensor import sensor

class Sensor:
    def __init__(self, sensor_pins: tuple) -> None:
        self.sensor_pins = sensor_pins
        self.sensor_module = sensor.Measurement(*sensor_pins)

    def scan(self) -> float:
        try:
            return self.sensor_module.raw_distance()
        except:
            print(f"sensor Error: Pins {self.sensor_pins}")
