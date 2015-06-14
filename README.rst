Datastores, Python and You Workshop
===================================

This repository contains the working code for the Datastores, Python and You
workshop. Datastores themselves are contained inside Docker images.


Preparation
-----------

If you want to run the code here you'll need a Linux computer or virtual
machine - I suggest using Ubuntu and Vagrant to power it.

The system will need to have Docker installed; to do this on Linux, run::

    wget -qO- https://get.docker.com/ | sh

Recommended Python packages for debian-based systems (without these,
you'll need development headers and a compiler)::

    make
    python-psycopg2
    python-cryptography
    python-protobuf
    protobuf-compiler


Running
-------

First, run ``make build`` in the top-level directory - this will pull down
and compile all necessary Docker images to run the 6 examples that have
servers (Protocol Buffers and SQLite do not need them).

Then, ``cd`` into the directory of the datastore you want, and if it needs
a server, run ``make start``.

You can then run the examples directly using Python. If you wish to connect
to the server from a Python interactive shell, either copy the connection
code from the top of an example or use ``make getip`` to get the IP of the
server you should connect to.
