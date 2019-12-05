# LiveGreenScreen
This program is designed as a portable and accessible live green screen program.

## Installation:

- **Windows:**
  * Install python3 from the [official site](https://www.python.org/downloads/release/python-380/)
    * One of the Windows executable installers at the bottom of the page should work.
    * Ensure that the installer says that it is also installing pip
    * Additionally, ensure to check the box that says "Add python to PATH"
  * Open Command Prompt and type in the following commands:
    * `python -m pip install --upgrade pip --user`
    * `pip3 install opencv-python --user`

- **MacOS:**
  * Follow instructions found [here:](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)

- **Linux:**
  * In a Terminal window, type in `sudo apt-get install python3.6`
  * Enter your user password
  * Next, type `sudo apt-get install python-opencv`
  * run `sudo apt-get update`


## Usage:
- **Windows:**
  - Open File Explorer
  - In File Explorer, navigate to the top level directory of this project
  - Double click `LiveGreenScreen.bat`<br>
  _Note: It may be useful to make a shortcut for the above file for future use._ 

- **MacOS:**
  - Open a Terminal and navigate to the "src" folder in this project
  - Enter `python3 Main.py` into the terminal to run the program.

- **Linux:**
  - Navigate to the top level directory of this project in Terminal
  - Enter the command `./LiveGreenScreen.sh`

## License:
MIT
