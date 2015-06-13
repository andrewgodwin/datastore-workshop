.PHONY: build start stop getip

build:
	docker pull kbastani/docker-neo4j

start:
	docker run --name neo4j -d kbastani/docker-neo4j

stop:
	docker rm -f -v neo4j

getip:
	docker inspect neo4j | grep IPAddress

shell:
	docker exec -i -t neo4j shell
