.PHONY: build start stop getip

build:
	docker build -t workshop/postgresql .

start:
	docker run --name postgresql -d workshop/postgresql

stop:
	docker rm -f -v postgresql

getip:
	docker inspect postgresql | grep IPAddress

shell:
	docker exec -i -t postgresql psql -Upostgres
