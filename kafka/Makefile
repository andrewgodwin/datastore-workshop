.PHONY: build start stop getip

build:
	docker build -t workshop/kafka .

start:
	docker run --name kafka -p 2181:2181 -p 9092:9092 -d workshop/kafka

stop:
	docker rm -f kafka

getip:
	docker inspect kafka | grep IPAddress

shell:
	docker exec -i -t kafka bash
