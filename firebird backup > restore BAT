rem patch DB
set FULL_PATH=C:\Data\
set WORK=base.FDB
set NEW=base_new.FDB
set OLD=base_old.FDB
set BACKUP=base.fdk

rem path backup
set COPY_PATH=X:\backup\bupIK\

set USER_IB=NAME_DB
set PASSWORD_IB=PASS_DB


gbak -b -user %USER_IB% -pass %PASSWORD_IB% -v -g %FULL_PATH%%WORK% %FULL_PATH%%BACKUP%
if errorlevel 1 goto exit1

gbak -r -user %USER_IB% -pass %PASSWORD_IB%  -v  %FULL_PATH%%BACKUP%  %FULL_PATH%%NEW%
if errorlevel 1 goto exit2

del %FULL_PATH%%OLD%
ren %FULL_PATH%%WORK% %OLD%
if errorlevel 1 goto exit3

ren %FULL_PATH%%NEW% %WORK%
if errorlevel 1 goto exit4


echo All GOOD!
pause

:exit1
echo  
echo Error creating archive.
pause

:exit2
echo  
echo Error restore.
pause

                          
:exit3
echo  
echo Error rename %WORK% > %OLD%!
pause


:exit4
echo  
echo Error rename %NEW% > %WORK%!
pause
