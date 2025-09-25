import influxdb_client, random, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.rest import ApiException
from influxdb_client.client.write_api import SYNCHRONOUS
from urllib3.exceptions import ReadTimeoutError

class Transmitter:

    def __init__(self, token: str, org: str, url: str, bucket: str, device_name: str) -> None:

        self.token = token
        self.org = org
        self.url = url
        self.bucket = bucket
        self.write_api = None
        self.device_name = device_name
        self.points: list[Point] = list()

    def initalise_conection(self):
        """ connect to the database """
        client = influxdb_client.InfluxDBClient(url=self.url, token=self.token, org=self.org)

        self.write_api = client.write_api(write_options=SYNCHRONOUS)

    def send_data(self, circular_mean_height: float, raw_height: float, inital_calabration: float) -> None:
        """send the data to the Database"""
        self.points.append(
            Point("height")
                .tag("device_name", self.device_name)
                .field("inital_calabration", inital_calabration)
                .field("circular_mean_height", round(float(circular_mean_height),6))
                .field("raw_height", raw_height)
                .time(int(time.time()*10**9), write_precision=WritePrecision.NS)
            )

        if len(self.points) == 10:
            print("\n sending data\n")
            for i in range(10):
                try:
                    self.write_api.write(bucket=self.bucket, org=self.org, record=self.points)
                    self.points = list()
                    return
                except (ApiException, ReadTimeoutError) as error:
                    print(f"Requrest Error\n{error}")

            print("Failed to continue max retries met")
            exit(1)
