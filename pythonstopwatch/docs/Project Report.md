# Python Stopwatch (MET CS521 Information Structures with Python)

##Introduction
This is a python GUI project for a stopwatch using TKinter UI. It is a complete project with class definitions, unit tests and packaging.
The project has a [stopwatch.py](../stopwatch.py) class which contains all the logic related to it. It also includes the LapTime class to store lap timings.

The starting point of the project is the [__main__.py](../__main__.py) file which loads the project and sets up the main GUI.
The project also contains unit tests for various methods/classes of the project which can be found inside [test_stop_watch.py](../../tests/test_stop_watch.py) and [test_string_time_utils.py](../../tests/test_string_time_utils.py) 

The project uses [history_logger.py](../logger/history_logger.py) to log the stop watch data after user hits reset. It is stored in [stop_watch_history.txt](../logger/stop_watch_history.txt)
##How to run the project
Instructions on how to run the project can be found in the [README.md](../../README.md) file in the project root folder.

##Requirements
The complete project runs using the standard library modules. The requirements for the project are mentioned in [requirements.txt](../../requirements.txt)
They are part of the standard library and are not really used to run the project. They are used to package and distribute the project.

##Features
-   The project takes inspiration from the Alarms & Clock application of Windows 10.
-   This project was built to solve the issue of keeping track/history of previous stopwatch runs and analyse/use the data as per the needs of the user.
-   When start is hit, it starts the stopwatch and shows with milliseconds precision, only after hitting start one can hit reset or lap time.
-   The project is built on pythonic ideals and it is built to be maintainable, scalable and testable. It is based on OOP design and uses inheritance as well.

-   The classes use assert to make sure the behavior is expected and it throws an error to bring it to notice of the developer that what they are doing might be wrong.
-   All the project assets are bundled and packaged with the project when shared inside assets folder
-   Files only import and required names from the modules.
-   All project constants including [colors.py](../constants/colors.py) and [strings.py](../constants/strings.py) are kept in a separate package and used as a single source of access for scalability and maintainability.
-   The project has a score of 9.69/10.0 pylint.


