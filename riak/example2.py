import riak

# Get the IP address of the docker container "riak1"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "riak1"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
client = riak.RiakClient(protocol='http', host=host, http_port=8098)

print "Incrementing counter a bit..."
bucket = client.bucket_type("counters").bucket("hits")
key = bucket.new("homepage")
key.increment()
key.increment(3)
key.store()

print "Reading counter value..."
print bucket.get("homepage").value
