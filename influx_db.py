import influxdb_client, os, random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

def send_data(token,org,url,bucket,weight):
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    point = (
        Point("Weight")
            .tag("Device", "Pi")
            .field("Weight", weight)
        )

    write_api.write(bucket=bucket, org=org, record=point)
