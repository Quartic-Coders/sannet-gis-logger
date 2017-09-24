@echo off

REM Program: SannetLogger.bat
REM Author:  Andrew Tangeman    
REM Date:    20170719
REM

SET LOGPGM=..\sannetlogger\batlogger.py
SET ERRORCODE=0
SET JOBNAME=SannetLogger
SET TEMP=C:\Temp

REM Runs jobs without reports
.\pgms\TestLogger.exe | %LOGPGM%
SET ERRORCODE=%ERRORLEVEL%
IF %ERRORCODE% == 0 GOTO SECOND_JOB
ECHO FIRST_JOB Failed | %LOGPGM%
GOTO Email_Err

:Job_Complete
ECHO %JOBNAME% | %LOGPGM%
DATE /T | %LOGPGM%
TIME /T | %LOGPGM%
GOTO Job_Exit

:Email_Err
ECHO ERROR
GOTO Job_Exit

:Job_Exit
ECHO FireJobs.bat Ended | %LOGPGM%
DATE /T
TIME /T
exit %ERRORCODE%
