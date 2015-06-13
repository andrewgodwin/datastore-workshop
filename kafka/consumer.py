import kafka

# Get the IP address of the docker container "postgresql"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "kafka"]))[0]["NetworkSettings"]["IPAddress"]

client = kafka.KafkaClient('%s:9092' % host)
consumer = kafka.SimpleConsumer(client, topic="tasks", group="group1", auto_commit=False)

for message in consumer:
    print message
