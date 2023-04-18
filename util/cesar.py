#!/usr/bin/python

import sys


USAGE = """\
{} [e|d] <key> <file>

  <key>  - cesar key
  <file> - file containing the content to be encrypted/decrypted
"""

if __name__ == "__main__":
    """
    """

    if len(sys.argv) == 4:

        action = sys.argv[1]
        key = int(sys.argv[2])
        ifile = open(sys.argv[3], "rb")

        data = ifile.read()

        for c in data:
            if action == 'e':
                c = c + key
            else:
                c = c - key
            sys.stdout.buffer.write(c.to_bytes(1, 'big'))

    else:
        print(USAGE.format(sys.argv[0]))
