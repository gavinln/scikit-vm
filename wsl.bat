@echo off
set ROOT_DIR=%~dp0
echo starting Windows subsystem for Linux in %ROOT_DIR%
ubuntu.exe run "cd $(wslpath -u '%ROOT_DIR%'); bash"
