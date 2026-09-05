echo off
echo 1. cumulative listening duration - top artists
echo 2. cumulative plays - top artists
echo 3. total cumulative listening duration
echo 4. artist and album entropy

:askscript
echo please select a script to run (1-4)
set /P script_choice=enter a number:

if %script_choice% GEQ 1 (if %script_choice% LSS 5 goto scriptoptions)
goto outofboundserror


:outofboundserror
echo invalid input, please try again
goto askscript

:scriptoptions
echo chose script %script_choice%

if %script_choice% == 1 goto cum_duration
if %script_choice% == 2 goto cum_plays
if %script_choice% == 3 goto total_cum
if %script_choice% == 4 goto entropy

:cum_duration
cls
echo this script will graph your cumulative listening duration of a number of your top artists over time.
echo How many artists?
set /P x_artists=enter a number:
python cumulative_listening_duration.py "%x_artists%"
goto end

:cum_plays
cls
echo this script will graph your cumulative play count of a number of your top artists over time.
echo How many artists?
set /P x_artists=enter a number:
echo Please enter a minimum duration in seconds to include plays
set /P min_duration=enter a number:
python cumulative_plays.py "%x_artists%" "%min_duration%"
goto end

:total_cum
cls
echo this script will graph your total cumulative listening time. No choices are required.
python total_cumulative_listening_duration.py
goto end

:entropy
cls 
echo this script will graph your artist and album entropy over time. This, very loosely, is an indication of your listening diverstiy. A higher entropy grade is more diverse.
@REM echo over how many days should the data be smoothed? More days will lead to a cleaner graph, but also lose detail. If you are unsure, it is recommended to enter a value between 5 and 10.
@REM echo How many days?
@REM set /P x_days=enter a number:
@REM python entropy.py "%x_days%"
python entropy.py
goto end

:end
echo script finished succesfully, you can exit this window. Run analyse.bat again to choose a different script.
pause