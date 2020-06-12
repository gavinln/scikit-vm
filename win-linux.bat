@echo off
set ROOT_DIR=%~dp0
REM Needed to execute direnv
wsl -e /bin/bash -l -c "/bin/bash"
