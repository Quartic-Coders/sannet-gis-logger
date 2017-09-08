# Project Title

Class to standardize logging procedure for City of San Diego batch Processing.

## Getting Started

sannetlogger.py is a self-contained and portable, script but it can also be installed globally on your local machine for development using setup.py -install from cmd.

### Prerequisites

Python 2.7.1 or above.

### Installing

#### Option 1: Install in project folder

-- Step 1. Copy the sannetlogger.py file from the sannetlogger directory to the scripts folder of your project
-- Step 2. Import sannetlogger using the following syntax:

```python
from sannetlogger import sannetlogger
```

#### Option 2: Install on system globally.

-- Step 1. Open command prompt and navigate to the sannetlogger directory

```
cd <Drive>\..\sannetlog
```

-- Step 2. Run the setup.py file with the proper command

```
Setup.py install
```

Project will now be available on the local system for all python projects.

### How to USe

To use this script, simply include the following at the top of your imports:

```python
from sannetlogger import SannetLogger
```

To log, assign the ``` SannetLogger() ``` object to a variable, and use the .log() method to write to the log file.

```python
sanlogger = SannetLogger() # initialize sannetlogger
sanlogger.log("test message") # log using .log() method
 ```
 
When initializing the logger you can define the following optional parameters to output the log:

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
