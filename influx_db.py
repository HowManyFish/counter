import influxdb_client, random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from urllib3.exceptions import ReadTimeoutError

class Transmitter:

    def __init__(self,token,org,url,bucket,device_name):

        self.token = token
        self.org = org
        self.url = url
        self.bucket = bucket
        self.write_api = None
        self.device_name = device_name

    def initalise_conection(self):
        """ connect to the database """
        client = influxdb_client.InfluxDBClient(url=self.url, token=self.token, org=self.org)

        self.write_api = client.write_api(write_options=SYNCHRONOUS)

    def send_data(self,weight_fish,water_level,weight_total: float):
        """send the data to the Database"""
        print("function running")

        point = (
            Point("Weight")
                .tag("Device", self.device_name)
                .field("Weight Total", round(float(weight_total),6))
                .field("Water Level", round(float(water_level),6))
            )

        while True:
            try:
                self.write_api.write(bucket=self.bucket, org=self.org, record=point)
                break
            except ReadTimeoutError as error:
                print(f"Requrest Timeout\n{error}")
