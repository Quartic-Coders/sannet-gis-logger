# SannetLogger

Class to standardize logging procedure for City of San Diego batch Processing.

## Getting Started

sannetlogger.py is a self-contained and portable tool but it can also be installed globally on your local machine for development using setup.py -install from cmd.

### Prerequisites

Python 2.7.1 or above.

### Installing

#### Option 1: Install in project folder

Use this step if you're developing locally and do not want to install the script ["globally"](https://stackoverflow.com/questions/1471994/what-is-setup-py) on your local machine. 

Step 1. Copy the sannetlogger.py file from the sannetlogger directory to the scripts folder of your project
	
Step 2. Import sannetlogger using the following syntax:

```python
from sannetlogger import SannetLogger
```

#### Option 2: Install on system globally.

Use this option to install the module directly on your machine or a server. GISAPPSERVER and VMGISDEV04 are examples of where this module is already installed. 

Step 1. Open command prompt and navigate to the sannetlogger directory

```
cd <Drive>\..\sannetlog
```

Step 2. Run the setup.py file with the proper command

```
Setup.py install
```

Project will now be available on the local system for all python projects.

### How to Use

To use this script, simply include the following at the top of your imports:

```python
from sannetlogger import SannetLogger
```

To log, assign the ``` SannetLogger() ``` object to a variable, and use the .log() method to write to the log file.

```python
sanlogger = SannetLogger()
sanlogger.log("test message")
 ```

SannetLogger also extends the following additional logging options:

 ```python

sanlogger = SannetLogger()
sanlogger.log("Log default message. Default priority is INFO")
sanlogger.debug("Log message as DEBUG")
sanlogger.warning("Log message as WARNING")
sanlogger.error("Log message as ERROR")
sanlogger.critical("Log message as CRITICAL")
sanlogger.exception("Log message as EXCEPTION")

 ```
- Note: the "DefaultLevel" parameter will set a minimum threashold for what will be written to the log.

SannetLogger has the following optional parameters for initialization:

```python

def __init__(self, directory = "", name = "", level=INFO, file_type=".log", print_to_console=False, verbose=True):
    ...
    
```

When initializing the logger you can define the following optional parameters to specify the output filename:

```python
sanlogger = SannetLogger('<Directory Name>', '<File_Name>') # optional parameters
```

By default, the logger will output all files to the same directory of the calling script and the name will automatically match the script name. 

For Example: To output logs to a directory called "Log" outside of the \Scripts directory  use the following:

```python
sanlogger = SannetLogger("..\\Logs") # .. operator will cd back 1 and into Log directory
 
sanlogger.log("test message") # log will output to Logs directory
```

## Version

Alpha version 1.0.4

## Authors

* **Andrew Tangeman** - *Initial work* - [atangeman](https://github.com/atangeman)
