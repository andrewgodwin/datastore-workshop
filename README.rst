Datastores, Python and You Workshop
===================================

This repository contains the working code for the Datastores, Python and You
workshop. Datastores themselves are contained inside Docker images.

Preparation
-----------

If you want to run the code here you'll need a Linux computer or virtual
machine - I suggest using Ubuntu and Vagrant to power it.

The system will need to have Docker installed; to do this on Linux, run

    wget -qO- https://get.docker.com/ | sh

Recommended Python packages for debian-based systems (without these,
you'll need development headers and a compiler):

    python-psycopg2
    python-cryptography
    python-protobuf
    protobuf-compiler
