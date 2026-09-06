echo off
echo 1. cumulative listening duration - top artists
echo 2. cumulative plays - top artists
echo 3. total cumulative listening duration
echo 4. artist and album entropy
echo 5. weekly listening duration - top artists
echo 6. hourly and weekly listening distribution
echo 7. cumulative listening duration - top tracks

:askscript
echo please select a script to run (1-7)
set /P script_choice=enter a number:

if %script_choice% GEQ 1 (if %script_choice% LSS 8 goto scriptoptions)
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
if %script_choice% == 5 goto weekly_dur
if %script_choice% == 6 goto h_w_dis
if %script_choice% == 7 goto cum_duration_tracks

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
python entropy.py
goto end

:weekly_dur
cls
echo This script will graph the weekly listening duration of your top artists.
echo How many artists?
set /P x_artists=enter a number:
echo Do you want the weekly listening duration of your top artists to be graphed as a percentage of your weekly total listening duration? Enter 1 for yes, 2 for no 
set /P fractional=enter a number:
python fractional_top_artists.py "%x_artists%" "%fractional%"
goto end

:h_w_dis
cls
echo This script will graph your hourly and weekly listening distribution.
echo WARNING! The hourly distribution portion of this graph doesn't always seem to working entirely correctly, I am looking into this.
python hourly_weekly_distribution.py
goto end

:cum_duration_tracks
cls
echo this script will graph your cumulative listening duration of a number of your top tracks over time.
echo How many tracks?
set /P x_artists=enter a number:
python cumulative_duration_tracks.py "%x_artists%"
goto end


:end
echo script finished succesfully, you can exit this window. Run analyse.bat again to choose a different script.
pause