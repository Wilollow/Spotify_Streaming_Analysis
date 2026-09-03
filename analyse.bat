echo off
echo 1. cumulative listening duration - top artists
echo 2. cumulative plays - top artists

:askscript
echo please select a script to run (1-2)
set /P script_choice=enter a number:

if %script_choice% GEQ 1 (if %script_choice% LSS 3 goto scriptoptions)
goto outofboundserror


:outofboundserror
echo invalid input, please try again
goto askscript

:scriptoptions
echo chose script %script_choice%

if %script_choice% == 1 goto cum_duration
if %script_choice% == 2 goto cum_plays

:cum_duration
echo How many artists?
set /P x_artists=enter a number:
@REM if %x_artists% GEQ 1 (
@REM     echo succes
@REM )
python cumulative_listening_duration.py "%x_artists%"
goto end

:cum_plays
echo How many artists?
set /P x_artists=enter a number:

echo "Please enter a minimum duration in seconds"
set /P min_duration=enter a number:
python cumulative_plays.py "%x_artists%" "%min_duration%"
goto end


:end
echo script finished succesfully, you can exit this window
pause