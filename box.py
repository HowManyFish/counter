from ultrasonic_sensor import Sensor, averaged_scan
from led_flash import led_on
from influx_db import Transmitter
from statistics import mean

class Box:
    def __init__(self, sensors: list, mesurement_history_len: int) -> None:
        self.sensors: list = sensors
        self.sensor_calabrations: list[float] = list()
        self.mesurement_history_len = mesurement_history_len
        self.mesurement_history: list[list[float]] = list()

    def calabrate_sensors(self, number_scans: int) -> None:
        """
        sensor calabarations:

        mesured for each sensor then saved as invisual results in self.sensor_calabrations
        """
        if len(self.sensors) < 1:
            print("self.sensors must have atleast one sensor")

        sensor_calabrations = averaged_scan(self.sensors, number_scans)
        self.sensor_calabrations = [scan[0] for scan in sensor_calabrations]

        for _ in len(self.sensors):
            self.mesurement_history.append(list())

    def scan(self, transmitter: Transmitter) -> None:
        """
        scans for water height level

        it sans all sensors once and transmits a circular_mean_level and raw_level to the database
        """
        raw_height: list[float] = list()
        circular_mean_height: list[float] = list()

        for sensor_number, sensor in enumerate(self.sensors):
            scan = sensor.scan()

            if len(self.mesurement_history) > self.mesurement_history_len:
                self.mesurement_history[sensor_number].pop(0)

            print(self.mesurement_history)

            self.mesurement_history[sensor_number].append(scan)

            circular_mean_height.append(mean(self.mesurement_history[sensor_number]))
            raw_height.append(scan)

        led_on(0.5) # NOTE: flashes indecator led may slow speed of application due to blocking nature

        transmitter.send_data(mean(circular_mean_height), mean(raw_height), mean(self.sensor_calabrations))
