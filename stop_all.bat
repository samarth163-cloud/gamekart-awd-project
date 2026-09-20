@echo off
title Stopping Full-Stack Application Services...
color 0C

echo ===================================================
echo     STOPPING ALL SERVERS AND FRONTEND PORTS
echo ===================================================
echo.

echo Freeing Port 5000 (Admin Backend)...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5000" ^| findstr "LISTENING"') do taskkill /f /pid %%a 2>nul

echo Freeing Port 4000 (Client Backend)...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":4000" ^| findstr "LISTENING"') do taskkill /f /pid %%a 2>nul

echo Freeing Port 5173 (Admin Frontend)...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5173" ^| findstr "LISTENING"') do taskkill /f /pid %%a 2>nul

echo Freeing Port 5174 (Client Frontend)...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5174" ^| findstr "LISTENING"') do taskkill /f /pid %%a 2>nul

echo.
echo ===================================================
echo   ALL PORTS HAVE BEEN CLEARED & SERVERS STOPPED!
echo ===================================================
echo.
pause
