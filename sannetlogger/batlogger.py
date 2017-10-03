# ---------------------------------------------------------------------------
# Name:      batlogger.py
# Author:    Andrew Tangeman
# Created:   2017-09-23
# Purpose:   Adapter module to passe messages piped in from DOS / CMD prompt
#            to sannetlogger.
#
# ---------------------------------------------------------------------------   

import traceback, os, sys   
from sannetlogger import SannetLogger


if __name__== "__main__":
    print(sys._current_frames()[0])
    sanlogger = SannetLogger(directory=os.getcwd(), name="name", print_to_console=True) # initialize logger
    line = sys.stdin.readline()
    while line:
        sanlogger.log(line.strip("\n"))
        line = sys.stdin.readline()