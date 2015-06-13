.PHONY: build run

build:
	docker build -t workshop/riak .

start:
	docker run --name riak1 -d workshop/riak
	docker run --name riak2 -d workshop/riak

stop:
	docker rm -f riak1
	docker rm -f riak2

getip:
	docker inspect riak1 | grep IPAddress

shell1:
	docker exec -i -t riak1 bash

shell2:
	docker exec -i -t riak2 bash

# How to cluster:
# make getip
# make shell2
# /usr/sbin/riak-admin cluster join riak@<ip>
# /usr/sbin/riak-admin cluster plan
# /usr/sbin/riak-admin cluster commit

# Setting up bucket type:
# make shell1
# /usr/sbin/riak-admin bucket-type create counters '{"props":{"datatype":"counter"}}'
# /usr/sbin/riak-admin bucket-type activate counters
