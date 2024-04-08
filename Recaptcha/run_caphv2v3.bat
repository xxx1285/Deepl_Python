@echo off
echo ######################################################
echo ###   GSA Service Recaptchav2v3 Solver (CAPV2V3)   ###
echo ###   (Listening on port http://127.0.0.1:8181)    ###
echo ######################################################
echo(
echo Running ...
echo ######################################################################################################################

python --version 3.11.7>NUL

if %errorlevel% equ 0 (
  python -m uvicorn caphv2v3:app --port 8181 --log-config caphv2v3.ini
) else (
  py -m uvicorn caphv2v3:app --port 8181 --log-config caphv2v3.ini
)
pause