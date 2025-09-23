import influxdb_client, random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

def send_data(token,org,url,bucket,weight):
    print("function running")
    print(token)
    print(weight)
    print(org)
    print(url)
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    point = (
        Point("Weight")
            .tag("Device", "Pi")
            .field("Weight", weight)
        )

    print(point)
    
    write_api.write(bucket=bucket, org=org, record=point)
