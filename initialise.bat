echo off
echo initialising...
echo looking for dependencies
if exist requirements.txt (
    echo requirements.txt found... installing dependencies
) else (
    echo failed
    exit
)

pip install -r requirements.txt

echo dependencies installed
echo loading history...

python library_builder.py


echo finished initialising succesfully!
echo you can now run analyse.bat to start analysing your listening history

pause