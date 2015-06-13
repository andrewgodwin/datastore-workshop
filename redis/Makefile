.PHONY: build start stop getip

build:
	docker build -t workshop/redis .

start:
	docker run --name redis -d workshop/redis

stop:
	docker rm -f redis

getip:
	docker inspect redis | grep IPAddress

shell:
	docker exec -i -t redis bash
