.PHONY: clean-containers

clean-containers:
	docker rm `docker ps -a -q`

clean-images:
	docker images | grep "<none>" | awk '{ print "docker rmi " $3 }' | bash 

build:
	make -C redis build
	make -C riak build
	make -C postgresql build
	make -C kafka build
	make -C elasticsearch build
	make -C neo4j build

stop:
	-make -C redis stop
	-make -C riak stop
	-make -C postgresql stop
	-make -C kafka stop
	-make -C elasticsearch stop
	-make -C neo4j stop
