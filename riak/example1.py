import riak

# Get the IP address of the docker container "riak1"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "riak1"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
client = riak.RiakClient(protocol='http', host=host, http_port=8098)

print "Pinging..."
print client.ping()

print "Setting key..."
bucket = client.bucket("phrases")
key1 = bucket.new("first", data="hello world")
key1.store()

print "Getting key..."
print bucket.get("first").data

print "Deleting key..."
bucket.get("first").delete()
