# instructions

1. These scripts work using spotify's Extended streaming history. You can head over to [Spotify's privacy page](https://www.spotify.com/us/account/privacy/) to download your personal streaming data. Spotify also offers data on your account and technical log, but for most people these aren't very useful/interesting - they are therefore also not required for these scripts. After a usual waiting period of 1-14 days, you will receive a mail, allowing you to download "my_spotify_data.zip". **Make sure it actually belongs to the Extended streaming history!** , as all three data catagories will default to the same filename. Keep this file somewhere you'll remember, you are going to need it later. **It is recommended you don't share these files** - especially those belonging to account logs - with other people, as some files contain sensitive information.

2. If you haven't already, download the latest python version from [the official site](https://www.python.org/downloads/).

3. Download all scripts using the Code > Download ZIP button at the top of this page.

4. Extract both zip files, and copy the contents of the "Spotify Extended Streaming History" inside of the newly created "my_spotify_data" folder (or whatever name you gave it) into the "data" folder inside of the other extracted folder (The one you downloaded from this page). **Make sure you copy the contents of "Spotify Extended Streaming History", not the folder itself!**

5. To initialise, double click to initialise.bat. This may require administrator priviliges. This will open command prompt and download a few python libraries that the scripts need in order to run properly. The full list of used dependencies can be found in "requirements.txt". This will also create a "spotify_history.json" file, which merges all usefull info from the files spotify provided into one list of listening events. All scripts will use this file as their data source, so make sure you don't accidentally move or delete it. This process may take a few minutes at most. It will clearly display when it is finished, at which point you can press any key, or simply close the window.

6. You can now run analyse.bat to start the fun. This will open another command prompt window. It will prompt you to choose a script to run:
    1. cumulative listening duration - top artists
    2. cumulative plays - top artists

enter a number (1 or 2) and press enter to confirm you selection. Based on what script you chose, the program may prompt you to choose a few more options. For instance, if you chose 1, the program will ask you how many of your top artists you wish to analyse. It is recommended to choose a sensible number, such as 10. If you go much beyond 20, the resulting image will likely get very cluttered, but you can choose anything. Choosing 2, will have you make a similar choice, but also make you choose a minimum listening duration (in seconds) to include listens in the analysis. You may for instance not wish to include tracks you skipped after 5 seconds. It is recommended to choose a duration between 30-60 seconds, but again, you can get creative.

After all choices are made, the program will ask you to confirm wether you want to run the script. Enter "Yes" to continue, anything else will discontinue the program. After this, the program will get to work. This may take a few seconds. When finished, the program will again close itself. In the "results" folder, you will find an image with the same name as the script you chose. Subsequent iterations of the same script will overwrite this image, so move it someplace else if you want to save it.

I may add some more scripts or update existing ones once every so often.

Have fun!
