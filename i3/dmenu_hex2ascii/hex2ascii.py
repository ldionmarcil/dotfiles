import sys
from binascii import hexlify, unhexlify

if len(sys.argv) < 3:
    sys.exit(-1)

OPER = sys.argv[1]
DATA = sys.argv[2]

if OPER.lower() == "hexify":
    hexified = str(hexlify(DATA.encode('ascii')))
    print(' '.join(hexified[i:i+2] for i in range(0, len(hexified), 2)))

elif OPER.lower() == "unhexify":
    print(unhexlify(DATA))

else:
    sys.exit(-1)
