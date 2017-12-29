# ---------------------------------------------------------------------------
# Name:      SannetLogger.py
# Author:    Andrew Tangeman
# Created:   2017-09-07
# Purpose:   Wapper class to standardize logging procedure for City of San Diego batch
#            Processing. Extends from python logging library. 
#
# ---------------------------------------------------------------------------

import logging, os, inspect, glob, sys, textwrap
from logging import DEBUG, CRITICAL, INFO, ERROR, WARNING, NOTSET

class SannetLogger(logging.getLoggerClass()):
    # global variable to define default logfile format
    LOG_FORMAT_A = '%(asctime)-10s | %(name)-8s | '\
                   '%(levelname)-8s | Method: %(mod_name)-8s | '\
                   'Line: %(line_no)-5s | Message: %(message)s'

    LOG_FORMAT_B = '%(asctime)-10s | %(name)-8s | '\
                   '%(levelname)-8s | Message: %(message)s'
                   
    # global variable to define default datetime format
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, directory = "", name = "", level=INFO, file_type=".log", print_to_console=False, verbose=True):
        """Private method to initialize logger and set formatting to conform to CoSD standards."""
        # Initial construct.
        self.format = self.LOG_FORMAT_A if (verbose) else self.LOG_FORMAT_B
        self.level = level
        self.name = name
        self.parent = None
        self.propagate = 1
        self.handlers = []
        self.disabled = 0
        self.verbose = verbose
        self.max_len = 200

        # intialize public and private member variables
        self.__addformat = {'mod_name':'root', 'line_no' : '0', 'line_code' : ''} # verbose log formatting
        self.file_name = os.path.basename(self.__getCallingName()) if (name == "") else name # assign file name to name of caller if bank
        self.directory = os.path.dirname(self.__getCallingName()) if (directory == "") else directory # assign dir to dir of caller if blank

        # intialize logger
        self.file_name = self.file_name if ("." in self.file_name == False) else self.file_name.split('.')[0]
        self.logger = logging.getLogger(self.file_name)
        self.logger.setLevel(level) # sets level of urgency
        self.file_path = self.directory + '\\' + self.file_name + file_type # format complete file path

        # adds file handler
        self.__addFileHandler()

        # add handler to print to stdout
        if (print_to_console):
            self.__addStreamHandler()

        # set enhanced formatting requirements
        self.logger = logging.LoggerAdapter(self.logger, self.__addformat)

    def __addFileHandler(self):
        """private function to add file handler to the logger"""
        self.file_handler = logging.FileHandler(self.file_path) # create a file handler
        self.__formatter = logging.Formatter(self.format, self.DATETIME_FORMAT) # init formatter
        self.file_handler.setFormatter(self.__formatter) # set formatter for log file
        self.logger.addHandler(self.file_handler) # add final handle object

    def __addStreamHandler(self):
        """Private function to add stream handler for passing messages to stdout."""
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(self.format, self.DATETIME_FORMAT) # init formatter
        ch.setFormatter(formatter)
        self.root.addHandler(ch)

    def __getCallingName(self):
        """Private function to return the calling name of parent process in stack queue."""
        stack_frame = inspect.stack()[2] # get stack trace info
        module = inspect.getmodule(stack_frame[0]) # grab submodule from stack trace
        return module.__file__.split(".py")[0] # return file_name of caller submodule

    def __setStackInfo(self):
        """Private function to update output based on calling info from execution stack."""
        stack_frame = inspect.stack()[2] # get stack trace info
        module = inspect.getouterframes(stack_frame[0])[0][3] # grabs most recent module from stack outer frame
        line_no = inspect.getouterframes(stack_frame[0])[0][2] # gets line number trace fron stack outer frame
        self.__addformat['mod_name'] = module if (module != '<module>') else "Main" # set name of calling method
        self.__addformat['line_no'] = line_no # set line number

    def __log(self, message, level=INFO):
        """Private function to execute writing a message to log file."""
        parts = textwrap.wrap(message, self.max_len)
        for item in parts: self.logger.log(level, item)

    def log(self, message, level=INFO):
        """Public function to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.log(message, INFO) # write message to log

    def info(self, message):
        """Public function to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.__log(message, INFO) # write message to log
        
    def warning(self, message):
        """Public function to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.__log(message, WARNING) # write message to log

    def debug(self, message):
        """Public function to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.__log(message, DEBUG) # write message to log

    def error(self, message):
        """Public function to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.__log(message, ERROR) # write message to log

    def critical(self, message):
        """Public function to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.__log(message, CRITICAL) # write message to log

    def exception(self, message):
        """Public function to execute writing a message to log file."""
        try:
            self.__setStackInfo() # update stack information from caller
            self.logger.exception(message) # write message to log
        except AttributeError:
            self.logger.exception(str(message)) # some exception objects (ArcPy type) are not expandable and throw Attribute Error; must cast to string
        except StandardError as ex:    # good idea to be prepared to handle various fails
            self.__log(ex, ERROR) # write message to log
            
## ------ TEST MAIN -----------------------------------------------------------------------

if __name__== "__main__":
    sanlogger = SannetLogger(print_to_console=True, verbose=True) # initialize logger
    sanlogger.log("test")
    sanlogger.warning("test warning")
    sanlogger.debug("test debug")
    sanlogger.error("test error")
    sanlogger.error("test critical")