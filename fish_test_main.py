from sensor_module import Sensor
from measurement_controller import MeasurementController

if __name__ == "__main__":
    a = Sensor((23, 24))
    b = Sensor((20, 21))
    c = MeasurementController([a, b])
    print(c.gattling_gun(5))