@echo off

taskkill /F /IM svchost.exe /FI "SERVICES eq stisvc"

net start stisvc
