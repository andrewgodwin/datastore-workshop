.PHONY: clean-containers

clean-containers:
	docker rm `docker ps -a -q`

clean-images:
	docker images | grep "<none>" | awk '{ print "docker rmi " $3 }' | bash 

build:
	make -C redis build
	make -C riak build
	make -C postgresql build
