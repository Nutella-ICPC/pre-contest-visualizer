# pre contest visualizer
[![fa](https://img.shields.io/badge/click_to_README-Persian-red.svg)](README-FA.md)
<br>


This repository contains a Python program that simulates a realistic ICPC contest.

## Installation
The program requires several external libraries.  To install them, run the following command in your terminal:
```bash
sudo pip3 install -r requirements.txt
```
This command will download and install all the necessary libraries listed in the `requirements.txt` file.

### Installation with Virtual Environment
1. Create a virtual environment:
```bash
virtualenv venv
```
This creates a virtual environment named `venv` in your current directory. It isolates project dependencies from your system-wide Python installation, ensuring compatibility and avoiding conflicts.

2. Activate the virtual environment:
```bash
. venv/bin/activate
```
This activates the virtual environment, making `venv` the active environment. Packages installed within it will be isolated from your system-wide Python.

### Deactivate the Virtual Environment (Optional):
When you're finished working on the project, you can deactivate the virtual environment to return to your system-wide Python installation:
```bash
deactivate
```


## Contributing
We welcome contributions to this project! If you have any ideas or improvements, please feel free to create a pull request.

adding new madules in `requirements.txt`:
```bash
pip3 freeze > requirements.txt
```

## License
This project is licensed under the [MIT Licence](/LICENSE).  Please see the LICENSE file for more details.