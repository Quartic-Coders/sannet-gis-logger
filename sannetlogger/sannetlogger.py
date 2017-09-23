# ---------------------------------------------------------------------------
# Name:      SannetLogger.py
# Author:    Andrew Tangeman
# Created:   2017-09-07
# Purpose:   Class to standardize logging procedure for City of San Diego batch
#            Processing.
#
# ---------------------------------------------------------------------------

import logging, os, inspect, glob
from logging import DEBUG, CRITICAL, INFO, ERROR, WARNING

class SannetLogger(logging.getLoggerClass()):
    # global variable to define default logfile format
    LOG_FORMAT = '%(asctime)-10s | %(name)-8s |'\
                 '%(levelname)-5s | Method: %(mod_name)-10s | '\
                 'Line No: %(line_no)-5s | Message: %(message)s'

    def __init__(self, directory = "", name = "", level=INFO):
        """Private method to initialize logger and set formatting to conform to CoSD standards."""
        # Initial construct.
        self.format = self.LOG_FORMAT
        self.level = level
        self.name = name

        # intialize public and private member variables
        self.__addformat = {'mod_name':'root', 'line_no' : '0', 'line_code' : ''} # verbose log formatting
        self.file_name = os.path.basename(self.__getCallingName()) if (name == "") else name # assign file name to name of caller if bank
        self.directory = os.path.dirname(self.__getCallingName()) if (directory == "") else directory # assign dir to dir of caller if blank

        # intialize logger
        self.logger = self.getLogger(self.file_name)
        self.logger.setLevel(logging.INFO) # sets level of urgency
        file_path = self.directory + '\\' + self.file_name + '.log' # format complete file path

        # add the handlers to the logger
        file_handler = logging.FileHandler(file_path) # create a file handler
        file_handler.setLevel(logging.INFO) # set a log format
        
        formatter = logging.Formatter(self.format) # init formatter
        file_handler.setFormatter(formatter) # set formatter for log file
        self.logger.addHandler(file_handler) # add final handle object

        # set enhanced formatting requirements
        self.logger = logging.LoggerAdapter(self.logger, self.__addformat)

    def __getCallingName(self):
        """Private method to return the calling name of parent process in stack queue."""
        stack_frame = inspect.stack()[2] # get stack trace info
        module = inspect.getmodule(stack_frame[0]) # grab submodule from stack trace
        return module.__file__.split(".py")[0] # return file_name of caller submodule

    def __setStackInfo(self):
        """Private method to update output based on calling info from execution stack."""
        stack_frame = inspect.stack()[2] # get stack trace info
        module = inspect.getouterframes(stack_frame[0])[0][3] # grabs most recent module from stack outer frame
        line_no = inspect.getouterframes(stack_frame[0])[0][2] # gets line number trace fron stack outer frame
        self.__addformat['mod_name'] = module if (module != '<module>') else "Main" # set name of calling method
        self.__addformat['line_no'] = line_no # set line number

    def getLogger(self, name):
        return logging.getLogger(name)

    def log(self, message, level=INFO):
        """Public method to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.logger.log(level, message) # write message to log

    def info(self, message):
        """Public method to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.logger.info(message) # write message to log
        
    def warning(self, message):
        """Public method to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.logger.warning(message) # write message to log

    def error(self, message):
        """Public method to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.logger.error(message) # write message to log

    def critical(self, message):
        """Public method to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.logger.critical(message) # write message to log

    def exception(self, message):
        """Public method to execute writing a message to log file."""
        self.__setStackInfo() # update stack information from caller
        self.logger.exception(message) # write message to log

## ------ TEST MAIN -----------------------------------------------------------------------

if __name__== "__main__":
    sanlogger = SannetLogger() # initialize logger
    print('logging output to ' + sanlogger.directory + '\\' + sanlogger.file_name)
    sanlogger.log("test message") # test log output
    sanlogger.log("test warning", WARNING)
    sanlogger.critical("test critical")