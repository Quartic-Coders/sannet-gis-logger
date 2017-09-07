# ---------------------------------------------------------------------------
# CosdLogger.py
# Created on: 2017-09-07
# Author:     Andrew Tangeman
# Purpose:   Class to standardize logging procedure for City of San Diego batch
#            Processing.
#
# ---------------------------------------------------------------------------
# Processing: 1. Get parameters and validate.
#             	2. Add L_MGRA and R_MGRA because SanGIS deleted them.
#             	3. Calculate L_MGRA and R_MGRA from repective L_PSBLOCK and #----------------------------------------------------------------------------

import logging, os, inspect, glob


class CosdLogger:

    def __init__(self, directory = None, name = None):
        self.file_name = name
        self.directory = directory
        self.extra_format = {'mod_name':'root', 'line_no' : 0, 'line_code' : ''} 

        if self.file_name is None: # if user doesn't supply name, find out what file they call from
            frm = inspect.stack()[1] # get stack trace info
            mod = inspect.getmodule(frm[0]) # grab submodule from stack trace
            self.file_name = mod.__file__.split(".py")[0] # set file_name to submodule

        if self.directory is None:
            self.directory = os.path.dirname(os.path.realpath(__file__))

        self.logger = logging.getLogger(self.file_name)

        self.logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler(self.directory + '\\' + self.file_name +'.log')
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(asctime)-10s | %(name)-8s | %(levelname)-5s | Method: %(mod_name)-10s | Line No: %(line_no)-5s | Message: %(message)s' )
        handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(handler)
        self.logger = logging.LoggerAdapter(self.logger, self.extra_format)

    def log(self, message):
        frm = inspect.stack()[1] # get stack trace info
        mod = inspect.getmodule(frm[0]) # grab submodule from stack trace
        line = inspect.getsourcelines(frm[0])
        comment = inspect.getcomments(frm[0])
        self.extra_format['mod_name'] = inspect.getouterframes(frm[0])[0][3]
        self.extra_format['line_no'] = inspect.getouterframes(frm[0])[0][2]
        #self.extra_format['line_code'] = inspect.getouterframes(frm[0])[0][4]
        self.logger.info(message)

if __name__=="__main__":
    cosdlogger = CosdLogger()
    cosdlogger.log("test message")