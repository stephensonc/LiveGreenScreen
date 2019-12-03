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

- **Linux:**
  * In a Terminal window, type in `sudo apt-get install python3.6`
  * Next, type `sudo apt-get install python-opencv`
  * To check that everything installed properly, enter `python3` and then enter the following commands:
  ```Python
  import cv2
  print(cv2.__version__)
  ```


## Usage:
- **Windows:**
  - Open File Explorer
  - In File Explorer, navigate to the top level directory of this project
  - Double click `run.bat`
- **Linux:**
  - Navigate to the top level directory of this project in Terminal
  - Enter the command `./run.sh`

## License:
