#!/usr/bin/python

import sys
import socket
import ipaddress

DEFAULT_PORT = 80

USAGE = """\
Verify the Hosts of a given Network.

{} <net>
  <net> - Network used to generate IP address list.\
"""

if __name__ == "__main__":
    """
    """
    if len(sys.argv) == 2:
        network = sys.argv[1]
        address = ipaddress.ip_network(network)
        up = {}
        down = {}
        for addr in address:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((addr.exploded, DEFAULT_PORT))
                up[addr] = DEFAULT_PORT
            except ConnectionRefusedError as e:
                up[addr] = e
            except Exception as e:
                down[addr] = e
        for addr in up:
            print(addr)
    else:
        print(USAGE.format(sys.argv[0]))

