#!/usr/bin/python

"""Count Down Small Apps"""

import time
import sys

timer_length = '00:10:00'

detik = 11 
menit = 1 
jam = 0

while menit >= 0:
    # ada if di setiap kondisi
    # ada break ketika tidak terpenuhi
    if len(str(detik)) == 2:
        sys.stdout.write("\r%d:%2d " % (int(menit), int(detik)))
        detik = detik - 1
        sys.stdout.flush()
        time.sleep(1)
        if detik == 0:
            menit = menit - 1
            detik = 59
            sys.stdout.write("\r%d:%2d " % (int(menit), int(detik)))
            detik = detik - 1
            sys.stdout.flush()
            time.sleep(1)
    elif len(str(detik)) == 1:
        sys.stdout.write("\r%d:0%d " % (int(menit), int(detik)))
        detik = detik - 1
        sys.stdout.flush()
        time.sleep(1)
        if detik == 0:
            menit = menit - 1
            detik = 59
            if menit == 0:
                sys.stdout.write("\r%d:%2d " % (int(menit), int(detik)))
                detik = detik - 1
                sys.stdout.flush()
                time.sleep(1)
