@echo off
title Launching Full-Stack Application...
color 0A

echo ===================================================
echo     STARTING SERVERS AND FRONTEND APPLICATIONS
echo ===================================================
echo.

cd /d "%~dp0"

echo [1/4] Starting Admin Backend API (Port 5000)...
start "Admin Backend Server (Port 5000)" cmd /k "cd /d "%~dp0admin" && node src/server.cjs"

echo [2/4] Starting Client Backend API (Port 4000)...
start "Client Backend Server (Port 4000)" cmd /k "cd /d "%~dp0client" && node src/server.cjs"

echo [3/4] Starting Admin Frontend (Port 5173)...
start "Admin Frontend (Vite Port 5173)" cmd /k "cd /d "%~dp0admin" && npm run dev"

echo [4/4] Starting Client Frontend (Port 5174)...
start "Client Frontend (Vite Port 5174)" cmd /k "cd /d "%~dp0client" && npm run dev"

echo.
echo Waiting 5 seconds for services to initialize...
timeout /t 5 /nobreak >nul

echo.
echo [5/5] Opening applications in your default web browser...
start http://localhost:5174/
start http://localhost:5173/

echo.
echo ===================================================
echo   ALL SERVICES ARE RUNNING!
echo   - Customer Store: http://localhost:5174/
echo   - Admin Portal:   http://localhost:5173/
echo.
echo   To stop all running servers, run 'stop_all.bat'
echo ===================================================
echo.
pause
