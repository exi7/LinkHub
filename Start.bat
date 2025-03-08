@echo off
cls
echo ---------------------
echo     Welcome !
echo ---------------------
echo Choose a language to launch your prgoram :
echo 1. Francais
echo 2. English
echo 3. Deutsch
echo 4. Espanol

set /p lang=Entrez votre choix (1-4): 

if "%lang%"=="1" (
    echo Lancement du programme en francais...
    cd Français
    start python Repertoire.py
    exit
)

if "%lang%"=="2" (
    echo Launching the program in English...
    cd English
    start python Register.py
    exit
)

if "%lang%"=="3" (
    echo Starten des Programms in Deutsch...
    cd Deutsch
    start python Verzeichnis.py
    exit

)

if "%lang%"=="4" (
    echo Lanzando el programa en Espanol...
    cd Español
    start python Directorio.py
    exit
)

pause
