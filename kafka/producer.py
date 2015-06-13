import kafka

# Get the IP address of the docker container "postgresql"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "kafka"]))[0]["NetworkSettings"]["IPAddress"]

client = kafka.KafkaClient('%s:9092' % host)
client.ensure_topic_exists("tasks")
producer = kafka.SimpleProducer(client)

# Send message loop
while True:
    message = raw_input("> ")
    producer.send_messages("tasks", message)
