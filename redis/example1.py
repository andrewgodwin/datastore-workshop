import redis

# Get the IP address of the docker container "redis"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "redis"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
client = redis.StrictRedis(host=host, port=6379)

print "Setting key..."
client.set("key", "hello world")

print "Getting key..."
print client.get("key")

print "Deleting key..."
client.delete("key")
