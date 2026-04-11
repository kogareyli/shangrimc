@echo off
title ShangriMC - Installation des librairies Forge
color 0A
echo.
echo  ============================================
echo   ShangriMC - Installation librairies Forge
echo  ============================================
echo.

:: Verifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe !
    echo Installe Python depuis https://python.org
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.
echo Lancement de la verification et installation...
echo.

cd /d "%~dp0"
python fix_libs.py

echo.
echo ============================================
echo  Termine ! Lance maintenant le launcher.
echo ============================================
echo.
pause
