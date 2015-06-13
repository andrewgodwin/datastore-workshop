import elasticsearch

# Get the IP address of the docker container "elasticsearch"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "elasticsearch"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
es = elasticsearch.Elasticsearch(host=host)

# Load in some documents
pokemon = {
    1: {
        "name": "Bulbasaur",
        "entry": "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon.",
    },
    2: {
        "name": "Ivysaur",
        "entry": "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.",
    },
    3: {
        "name": "Venusaur",
        "entry": "The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.",
    },
    4: {
        "name": "Charmander",
        "entry": "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.",
    },
    5: {
        "name": "Charmeleon",
        "entry": "When it swings its burning tail, it elevates the temperature to unbearably high levels.",
    },
}

for id, entry in pokemon.items():
    res = es.index(index="exampleidx", doc_type='pokemon', id=id, body=entry)


# Search for some stuff
print "Getting id 4:"
print es.get(index='exampleidx', doc_type='pokemon', id=4)

print "Searching for rain:"
print es.search(index="exampleidx", body={"query": {"match": {'name': 'ivysaur'}}})['hits']['hits']

print "Fuzzy searching for 'charrmanda':"
print es.search(index="exampleidx", body={"query": {"fuzzy_like_this_field" : { "name" : {"like_text": "charrmanda", "max_query_terms":5}}}})['hits']['hits']

print "Searching for plant in everything:"
print es.search(index="exampleidx", body={"query": {"multi_match": {"query": "plant", "fields": ["name", "entry"]}}})['hits']['hits']
