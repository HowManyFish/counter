from ultrasonic_sensor import Sensor, averaged_scan
from led_flash import led_on
from influx_db import Transmitter

class Box:
    def __init__(self, sensors: list[Sensor], mesurement_history_len: int) -> None:
        self.sensors: list[Sensor] = sensors
        self.sensor_calabrations: list[float] = list()
        self.mesurement_history_len = mesurement_history_len
        self.mesurement_history: list[list[float]] = list()

    def calabrate_sensors(self) -> None:
        """
        sensor calabarations:

        mesured for each sensor then saved as invisual results in self.sensor_calabrations
        """
        if len(self.sensors) < 1:
            print("self.sensors must have atleast one sensor")

        for sensor in self.sensors:
            sensor_calabrations = averaged_scan(self.sensors, 5)
            self.sensor_calabrations = [scan[0] for scan in sensor_calabrations]

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
                self.mesurement_history.pop(0)

            self.mesurement_history[sensor_number].append(scan)

            circular_mean_height.append(mean(self.mesurement_history))
            raw_height.append(scan)

        led_on(1) # NOTE: flashes indecator led may slow speed of application due to blocking nature

        transmitter.send_data(mean(circular_mean_height), mean(raw_height))
