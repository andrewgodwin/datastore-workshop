from py2neo import Node, Graph, Relationship

# Get the IP address of the docker container "neo4j"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "neo4j"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
graph = Graph("http://%s:7474/db/data/" % host)

# Make some nodes
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
cleo = Node("Pet", name="Cleo", species="Dog")
dan = Node("Person", name="Dan")

graph.create(Relationship(alice, "KNOWS", bob))
graph.create(Relationship(bob, "KNOWS", alice))
graph.create(Relationship(bob, "KNOWS", dan))
graph.create(Relationship(alice, "OWNS", cleo))

print "All people:"
for record in graph.cypher.execute("MATCH (p:Person) RETURN p.name AS name"):
    print(record.name)

print "People who know someone who know Dan:"
for record in graph.cypher.execute("MATCH (p)-[:KNOWS]->(q)-[:KNOWS]->(r {name:'Dan'}) RETURN p.name AS name"):
    print(record.name)
