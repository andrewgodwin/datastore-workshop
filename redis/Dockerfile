FROM phusion/baseimage:0.9.16

MAINTAINER Andrew Godwin andrew@aeracode.org

# Install Redis
RUN apt-get update && apt-get install -y redis-server

# Open port
EXPOSE 6379

# Run Redis
CMD ["/usr/bin/redis-server"]
