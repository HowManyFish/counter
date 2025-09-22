from ultrasonic_sensor import Sensor

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