import redis

# Get the IP address of the docker container "redis"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "redis"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
client = redis.StrictRedis(host=host, port=6379)

print "Adding things to lists..."
client.delete("colours")
client.rpush("colours", "white", "red", "blue")
client.lpush("colours", "green", "yellow")

print "Printing list..."
print client.lrange("colours", 0, -1)

print "Popping from list..."
print client.lpop("colours")
