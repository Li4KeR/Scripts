@echo off&setlocal enabledelayedexpansion

::perem
set max=20
set proc=firefox
set proc2=slimjet

:loop
for /f %%n in ('wmic cpu get NumberOfCores^|findstr [0-9]') do set c=%%n
for /f "skip=1 tokens=1,2" %%i in ('"2>nul wmic path Win32_PerfFormattedData_PerfProc_Process where "Name Like '!proc!%%'" get PercentProcessorTime,IDProcess"') do ^
if "%%i" neq "" set /a "p=%%~j/!c!" &if !p! gtr !max! 2>&1>nul taskkill /f /pid %%i >> log.txt

for /f %%n in ('wmic cpu get NumberOfCores^|findstr [0-9]') do set c=%%n
for /f "skip=1 tokens=1,2" %%i in ('"2>nul wmic path Win32_PerfFormattedData_PerfProc_Process where "Name Like '!proc2!%%'" get PercentProcessorTime,IDProcess"') do ^
if "%%i" neq "" set /a "p=%%~j/!c!" &if !p! gtr !max! 2>&1>nul taskkill /f /pid %%i >> log.txt

timeout /t 300
goto loop
