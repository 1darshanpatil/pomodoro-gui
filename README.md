# Pomodoro Timer GUI Application

This is a simple GUI application that implements the Pomodoro Technique, a time management method that involves breaking work into intervals (by default: 25 minutes), separated by short breaks.

# Features
* Start and reset functionalities
* Customizable work, break, and final break durations
* Audio notifications for work, break, and final break intervals
* Graphical countdown timer
* Progress indication by tick marks


# Prerequisites
* Linux Operating System
* Python 3.x
* `sox` for playing audio notifications
  `sox` will be installed as when `./pydeb.sh` will be executed.


# Installation
* Download or clone the files
    
      git clone https://github.com/1darshanpatil/pomodoro-gui

* Navigate to the directory
      
      cd pomodoro-gui

* Execute permission (Being a developer, I would not suggest anyone provide execute permission to any `.sh` file downloaded from known or unknown sources without examining the bash script commands.)


      chmod +x pydeb.sh

* Execution

      ./pydeb.sh pomodoro-gui.py

Your application is ready!


# To uninstall the application 

* Giving access

      chmod +x rmpkg.sh

* Execute

      ./rmpkg.sh

# [File Structure](![image](https://github.com/1darshanpatil/pomodoro-gui/assets/72539638/db638e63-ca1b-4b88-9181-b88552bd7b96)
