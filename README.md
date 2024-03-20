# Photo Organizer v0.1
Author: Nikola Paunovic

## Disclaimer & Backup Reminder
It is always a good idea to create a backup of any data that will be worked on before using this program. This program is under development and there is no guarantee that all data will be safe if the instructions were not properly followed.

Please read the "Instructions" **AND** "Folder structure & folder_config.json" sections before proceeding.

## Installation & Requirements
This project requires Python3 (tested with Python 3.12), as well as its 'pillow' module to be installed. Currently, this module needs to be installed manually.
To install pillow using pip, run 'pip install pillow' from your terminal.

```shell
pip install pillow
```

If the list of requirements ever changes, I will update it here as well as in the 'requirements.txt' file.

## How To Run / Instructions

1. Run **setup_cli.py** and follow on-screen instructions to create an output folder configuration file **OR** manually create a file according to the specifications below.
2. Once set up, run photo_organizer_gui.py and select an input folder.
3. Keep the terminal window open at all times! Closing the terminal window will terminate the program. The window is also useful to check whether an operation was successful.
4. As the images load, simply select the folder where each image should be sent.

The first step is very important for a working program. **setup_cli.py** can be run any number of times to change the folders available.
As of right now, there is no GUI available for folder setup, but that feature will be added in a future update.

## Folder structure & folder_config.json

### Categories
A category simply represents the type of image that will be sorted. For example, a category may be travel, landscapes, etc.

All folders should be sorted into categories. The user is able to choose the name of the category, and when prompted, writing an unrecognized category name will create the category.

The user may choose to not use categories for folders. To do so, simply leave the category prompt blank. Since configuration information is stored in a JSON file, any images without a category will actually be marked as a blank category ("").

### Folder name
All folders should be named to make it easier for the user to navigate the GUI. The folder name is what will be shown on the button for the folder once the photo organizer GUI is run.

### Folder path
All folders must include an **absolute** filepath for the program to work properly. Providing a relative filepath may produce unpredictable results, and should only be done at the user's own risk.

This program does **NOT** check the validity of each path, nor whether a path was provided. Make sure that every filepath is valid before attempting to move images. 

### folder_config.json
The folder_config.json file is created with the following format. This format has been chosen with future expandability in mind.
1. Every category created will be the name of a key, and will be fully upper-case.
2. The value of each key (category) is an object with keys that represent the name of each folder.
3. The value of each key (folder) is another object with a "path" key that contains the value of the path.  

This is an example of the file on a Windows machine:

```json
{
  "TRAVEL": {
    "Greece": { "path": "C:\\Photos\\Travel\\Greece" },
    "France": { "path": "C:\\Photos\\Travel\\France" }
  },
  "LANDSCAPES": {
    "Mountains": { "path": "C:\\Photos\\Landscapes\\Mountains" },
    "Lakes": { "path": "C:\\Photos\\Landscapes\\Lakes" }
  }
}
```

You may choose to manually create the folder_config.json file or do it automatically through the provided setup script.
Keep in mind that the choice of path is option and may be any desired folder.