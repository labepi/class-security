#!/usr/bin/python

import sys
import socket
import threading

BUFFER_SIZE = 1024

USAGE = """\
Verify the state of a TCP port of a Host.

{} <host> <port>
  <host> - the URL or IP address of the Host.
  <port> - the TCP port of the Host.\
"""

def create_receiver(timeout=1):
    """
    """
    receiver = socket.socket(family=socket.AF_INET,
                             type=socket.SOCK_RAW,
                             proto=socket.IPPROTO_ICMP)
    receiver.settimeout(timeout)

    return receiver

def read_receiver(receiver, ttl):
    """
    """
    try:
        data, addr = receiver.recvfrom(BUFFER_SIZE)
        print(ttl, addr)
    except Exception as e:
        print(ttl, e)


if __name__ == "__main__":
    """
    """
    if len(sys.argv) == 4:
        host = sys.argv[1]
        port = int(sys.argv[2])
        ttl = int(sys.argv[3])

        r = create_receiver()
        threading.Thread(target=read_receiver, args=[r, ttl]).start()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
        s.settimeout(1)
        try:
            s.connect((host, port))
            print(host, port, "open")
        except ConnectionRefusedError:
            print(host, port, "closed")
        except (TimeoutError, socket.timeout):
            print(host, port, "filtered")
        except Exception as e:
            print(e.args)
    else:
        print(USAGE.format(sys.argv[0]))
