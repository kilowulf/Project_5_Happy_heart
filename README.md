# Happy Heart Project


## Overview

The Happy Heart project is a software program designed to monitor the vital signs of hospital patients, specifically focusing on pulse rate, blood pressure, and blood oxygen levels. Its primary purpose is to raise alarms when it detects potentially life-threatening issues, ensuring patient safety. The program can accept data from either a file or keyboard input, providing flexibility for data sources.

## Features

The Happy Heart project provides the following key features:

- Continuous monitoring of patient vital signs.
- Ability to read data from either a file or keyboard input.
- Data collection every 10 seconds.
- Detection of the following vital signs:
    1. **Pulse Rate**: An integer value ranging from 0 to 260.
    2. **Blood Oxygen Level**: A percentage with one decimal place of precision, ranging from 0 to 99.9.
    3. **Blood Pressure**: Consisting of systolic (high number) and diastolic (low number) readings, as integers (i.e 120/80). Valid range for systolic is 0 - 230, for diastolic 0 - 150

## Alarm Levels

The Happy Heart project raises alarms at three different levels, depending on the severity of the detected issue:

1. **Highest Alarm**: Indicates a life-threatening problem, requiring immediate attention.
2. **Medium Alarm**: Suggests a dangerous condition that should be addressed promptly.
3. **Low Alarm**: Signals are a potential problem, which could be related to equipment issues.

## Usage

To run the Happy Heart program, you can provide a data file as a command-line argument or enter data manually through the keyboard. Here are some basic usage instructions:

### Operating System:
Our executable is built to run on Windows. The executable will not run on MacOs or Linux.

### Command Line:
Navigate to the directory holding the executable.
- Input with keyboard
```
happyheart.exe
```

- Input with .txt file
```
happyheart.exe <filename>.txt
```
(Important Note: The .txt file must be in the same directory as the .exe file for the command to work.)

### Data File Format

If you choose to use a data file, ensure it follows the specified format for vital signs (pulse rate, blood oxygen level, and blood pressure). For example:

```
86 92 120/80
88 91.5
88 91.3
87
85 89.4
84 89.0 122/81
```

### Keyboard Usage:

When no data file is provided in the command line, the program will prompt you to enter health data manually in the following format:

'Pulse Reading' 'Oxygen Level' 'Blood Pressure'

```
60 95 120/80
```

### Contact

For questions, feedback, or support, please contact our team.


