#!/usr/bin/python

import sys

NOP = "90"

USAGE = """\
{} <size> <code>

  <size> - size of the complete string (preceded by NOP)
  <code> - shellcode to be injected on the target program\
"""

if __name__ == "__main__":
    """
    """

    if len(sys.argv) == 3:

        size = int(sys.argv[1])
        code = sys.argv[2]

        # verify the code input format if uses '\x' remove it
        if len(code) == code.count("\\x") * 4:
            code = code.replace("\\x", "")

        # compute the NOP head
        head = NOP * int(size - (len(code) / 2))

        sys.stdout.buffer.write(bytes.fromhex(head + code))

    else:
        print(USAGE.format(sys.argv[0]))
