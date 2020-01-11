@echo off
set ROOT_DIR=%~dp0
echo starting Windows subsystem for Linux in %ROOT_DIR%
REM ubuntu.exe run "cd $(wslpath -u '%ROOT_DIR%'); bash"
wsl -e /bin/bash -c "cd $(wslpath '%ROOT_DIR%');/bin/bash -l"
