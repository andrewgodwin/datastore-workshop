all: addresses_pb2.py

addresses_pb2.py: addresses.proto
	protoc --python_out=. addresses.proto
