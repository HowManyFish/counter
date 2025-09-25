from hcsr04sensor import sensor
from statistics import mean

def averaged_scan(sensors: list, number_scans: int) -> list[(float, list[float])]:
    output: list[(float, list[float])] = list()

    for i in range(len(sensors)):
        output.insert(i, (0.0, list()))

    for scan in range(number_scans):
        for sensor_id, sensor in enumerate(sensors):
            output[sensor_id][1].append(sensor.scan())

    for index, sensor_scan in enumerate(output):
        output.insert(index, (mean(sensor_scan[1]), sensor_scan[1]))

    return output


class Sensor:
    def __init__(self, sensor_pins: tuple) -> None:
        self.sensor_pins = sensor_pins
        self.sensor_module = sensor.Measurement(*sensor_pins)

    def scan(self) -> float:
        try:
            return (self.sensor_module.raw_distance() / 100)
        except:
            print(f"sensor Error: Pins {self.sensor_pins}")
