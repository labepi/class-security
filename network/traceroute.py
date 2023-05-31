#!/usr/bin/python

import sys
import socket

BUFFER_SIZE = 1024
DEFAULT_PORT = 80

USAGE = """\
Verify the route to a given Host.

{} <host>
  <host> - Remote host used to generate route address list.\
"""

def create_receiver(timeout=1):
    """
    """
    receiver = socket.socket(family=socket.AF_INET,
                             type=socket.SOCK_RAW,
                             proto=socket.IPPROTO_ICMP)
    receiver.settimeout(timeout)

    return receiver

def create_sender(ttl):
    """
    """
    sender = socket.socket(family=socket.AF_INET,
                           type=socket.SOCK_DGRAM,
                           proto=socket.IPPROTO_UDP)
    sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    return sender

if __name__ == "__main__":
    """
    """
    if len(sys.argv) == 2:
        addr = socket.gethostbyname(sys.argv[1])
 
        ans_addr = None
        error = ""
        ttl = 1
        hop_limit = 30
        while ans_addr != addr and ttl <= hop_limit:
 
            receiver = create_receiver() 
            sender = create_sender(ttl)
            ans = None
            try:
                sender.sendto(b'', (addr, DEFAULT_PORT))
                data, ans = receiver.recvfrom(BUFFER_SIZE)
            except socket.error as e:
                error = '{}'.format(e)
            finally:
                receiver.close()                
                sender.close()
 
            if ans:
                ans_addr, _ = ans
                print('{} {}'.format(ttl, ans_addr))
            else:
                print('{} {}'.format(ttl, error))
 
            ttl += 1
    else:
        print(USAGE.format(sys.argv[0]))
