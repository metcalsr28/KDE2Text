# KDE2Text
A hacky solution for utilizing Capture2Text effectively on Linux. This project utilizes Linux native tools to implement the functionality that wine is currently unable to replicate. Capture2Text is a powerful tool and it's great being able to run it alongside Linux's already powerful native tools such as gazou. 

This project does not require you to run KDE to utilize, but it currently relies on Spectacle as dependency, and the installation for Spectacle will bring with it a lot of KDE's background dependencies. Granted, you've probably picked up most of them up without realizing at some point anyway.

## Installation

### Native Dependencies
```
Wine
Python
Spectacle
```

### Required Python Packages
```
python -m pip install opencv-contrib-python
python -m pip install pyperclip
```

### Capture2Text
```
mkdir res
cd res
curl -L https://sourceforge.net/projects/capture2text/files/Capture2Text/Capture2Text_v4.6.3/Capture2Text_v4.6.3_64bit.zip/download --output Capture2Text.zip
unzip Capture2Text.zip
rm Capture2Text.zip
```

## The next section should work, but just tried it on a fresh install and it didn't work. Keeping out of interest.

### Creating .Desktop

#### From main directory:
```
mv KDE2Text.desktop ~/.local/share/applications/KDE2Text.desktop
cd ~/.local/share/applications
sudo nano KDE2Text.desktop
```
Inside KDE2Text.desktop, change PATH variable to your KDE2Text directory


## End  archived Section

### Creating .Desktop
```
Right click on application menu icon on taskbar
Click "Edit Applications..."
Click "New Item" on menu bar
In Name: KDE2Text
In program line: python
In Command-Line Arguments: __main__.py
Unclick "Enable launch feedback"
Save
Optionally, drag and drop KDE2Text Item into one of the categories on the left.
Open ~/.local/share/applications/KDE2Text.desktop in text editor
Set PATH variable to KDE2Text base directory
```

## Running as a keyboard shortcut
```
Open System Settings -> Shortcuts
Press "Add Application" and select the KDE2Text application
Finally, Select KDE2Text in the applications menu and apply any shortcut key. (The default Capture2Text shortcut is Alt+Q) 
The program will automatically determine the vertical option should be used, so only one shortcut is required.
```

