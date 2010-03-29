#!/usr/bin/python

# Upload firmware of GPS chip to file.

import ubx
import struct
import calendar
import os
import gobject
import logging
import sys
import socket
import time

d = {}

f = open("upload.dat", "w+")
loop = gobject.MainLoop()

def callback(ty, *args):
    global f
    global t
    print("callback %s %s" % (ty, repr(args)))
    if ty == "UPD-UPLOAD" and args[0][0]["Flags"] == 1:
        for i in xrange(16):
            f.write(chr(args[0][0]["B%s" % i]))
        f.flush()
        time.sleep(0.1)
        t.send("UPD-UPLOAD", 12 +16, {"StartAddr" : args[0][0]["StartAddr"] + 16, "DataSize" : 16, "Flags" : 0, "B0" : 0, "B1" : 0, "B2" : 0, "B3" : 0, "B4" : 0, "B5" : 0, "B6" : 0, "B7" : 0, "B8" : 0, "B9" : 0, "B10" : 0, "B11" : 0, "B12" : 0, "B13" : 0, "B14" : 0, "B15" : 0})
        
if __name__ == "__main__":
    t = ubx.Parser(callback)
    start = int(sys.argv[1])
    t.send("UPD-UPLOAD", 12 + 16, {"StartAddr" : start, "DataSize" : 16, "Flags" : 0, "B0" : 0, "B1" : 0, "B2" : 0, "B3" : 0, "B4" : 0, "B5" : 0, "B6" : 0, "B7" : 0, "B8" : 0, "B9" : 0, "B10" : 0, "B11" : 0, "B12" : 0, "B13" : 0, "B14" : 0, "B15" : 0})
    loop.run()
