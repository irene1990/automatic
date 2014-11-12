@echo off
for /L %%i in (0,1,10) do (
echo %%i >> a.txt
echo %%i >> b.txt
ping -n 1 127.0.0.1 > nul
)
