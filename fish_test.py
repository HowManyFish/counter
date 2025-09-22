from hcsr04sensor import sensor
from time import sleep

class Sensor:
    def __init__(self, sensor_pins:tuple) -> None:
        self.sensor_module = sensor.Measurement(*sensor_pins)
    def scan(self) -> float:
        return self.sensor_module.raw_distance()

class MeasurementController:
    def __init__(self, sensors: list[Sensor]) -> None:
        self.sensors = sensors

    def gattling_gun(self, rounds: int) -> (float, [float]):
        """does {rounds} of rounds of measurement the it maths it"""
        distances = []

        for n in range(rounds):
            for n in range(rounds):
                for sensor in self.sensors:
                    distances.append(sensor.scan())
        
        avg = sum(distances) / len(distances)
        return avg, distances

a = Sensor((23, 24))
b = Sensor((20, 21))
c = MeasurementController([a, b])
print(c.gattling_gun(5))