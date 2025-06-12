@echo off
SETLOCAL

echo ========================================
echo Checking for Python installation...
echo ========================================
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python not found.
    echo 🔽 Downloading and installing Python 3.12...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe -OutFile python-installer.exe"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    del python-installer.exe
    echo ✅ Python installed.
) ELSE (
    echo ✅ Python is already installed.
)

echo ========================================
echo 🔧 Upgrading pip and installing packages...
echo ========================================
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install pandas requests openpyxl streamlit

echo ========================================
echo ✅ Environment setup complete!
echo You can now run your Python scripts.
echo ========================================
pause
ENDLOCAL
