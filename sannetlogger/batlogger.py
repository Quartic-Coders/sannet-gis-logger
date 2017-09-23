# ---------------------------------------------------------------------------
# Name:      batlogger.py
# Author:    Andrew Tangeman
# Created:   2017-09-23
# Purpose:   Adapter module to passe messages piped in from DOS / CMD prompt
#            to sannetlogger.
#
# ---------------------------------------------------------------------------   

import os, sys   
from SannetLogger import sannetlogger
   
if __name__== "__main__":
    sanlogger = SannetLogger(print_to_console=True) # initialize logger
    line = sys.stdin.readline()
    while line:
        sanlogger.log(line.strip("\n"))
        line = sys.stdin.readline()