import kafka
import time

# Get the IP address of the docker container "postgresql"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "kafka"]))[0]["NetworkSettings"]["IPAddress"]

client = kafka.KafkaClient('%s:9092' % host)
client.ensure_topic_exists("tasks")

# It needs some time to settle and pick a topic leader
print "Waiting for Kafka to settle..."
time.sleep(3)
producer = kafka.SimpleProducer(client)

# Send message loop
while True:
    message = raw_input("> ")
    producer.send_messages("tasks", message)
