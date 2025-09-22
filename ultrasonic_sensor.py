from hcsr04sensor import sensor

class Sensor:
    def __init__(self, sensor_pins: tuple) -> None:
        self.sensor_module = sensor.Measurement(*sensor_pins)

    def scan(self) -> float:
        return self.sensor_module.raw_distance()
