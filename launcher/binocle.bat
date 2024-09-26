@ECHO OFF

IF EXIST "%~dp0..\venv" (
    CALL "%~dp0..\venv\Scripts\activate.bat"
)

py "%~dp0..\source\binocle.py" %*