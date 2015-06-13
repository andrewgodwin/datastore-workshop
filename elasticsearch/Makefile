.PHONY: build start stop getip

build:
	docker pull elasticsearch:1.6

start:
	docker run --name elasticsearch -d elasticsearch:1.6

stop:
	docker rm -f -v elasticsearch

getip:
	docker inspect elasticsearch | grep IPAddress

shell:
	docker exec -i -t elasticsearch bash
