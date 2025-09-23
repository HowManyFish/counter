import influxdb_client, os, random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "fishy"
url = "https://us-central1-1.gcp.cloud2.influxdata.com"
bucket="Test"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

point = (
    Point("Weight")
        .tag("Device", "Pi")
        .field("Weight", random.randint(1, 10)
    )
)

write_api.write(bucket=bucket, org=org, record=point)
