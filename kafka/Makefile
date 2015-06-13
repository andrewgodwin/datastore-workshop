.PHONY: build start stop getip

build:
	docker build -t workshop/kafka .

start:
	docker run --name kafka -d workshop/kafka

stop:
	docker rm -f kafka

getip:
	docker inspect kafka | grep IPAddress

shell:
	docker exec -i -t kafka bash
