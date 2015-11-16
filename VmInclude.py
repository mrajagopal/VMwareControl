#!/usr/bin/python
from pysphere import VIServer, VIApiException, VIException


def connectToHost(host, hostUsername, hostPassword):
    # create server object
    server = VIServer()

    try:
        server.connect(host, hostUsername, hostPassword)
        return server

    except VIApiException:
        raise
