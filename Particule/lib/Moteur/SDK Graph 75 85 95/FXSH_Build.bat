@echo off
rem Do not edit! This batch file is created by CASIO fx-9860G SDK.

if exist debug\*.obj  del debug\*.obj
if exist PARTIC.G1A  del PARTIC.G1A

cd debug
if exist FXADDINror.bin  del FXADDINror.bin
"C:\Users\leofa\Applications\CASIO\fx9860 Dev Kit\OS\SH\Bin\Hmake.exe" Addin.mak
cd ..
if not exist debug\FXADDINror.bin  goto error

"C:\Users\leofa\Applications\CASIO\fx9860 Dev Kit\Tools\MakeAddinHeader363.exe" "C:\Users\leofa\OneDrive\Documents\PycharmProjects\Particule-Casio\Particule\lib\Moteur\SDK Graph 75 85 95"
if not exist PARTIC.G1A  goto error
echo Build has completed.
goto end

:error
echo Build was not successful.

:end

