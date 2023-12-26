# Health Check Script

## Introduction
This Python script is designed for performing health checks on various web endpoints. It sends requests to these endpoints and logs their status, helping in monitoring the health and availability of web services.

## Requirements
- Python 3.x
- Required Python libraries: `requests`, `yaml`, `logging`, `colorama`

## Setup
1. Ensure Python 3.x is installed on your system.
#### Checking and Installing Python 3
To check if Python 3 is installed on your machine, open a terminal and run:
```bash
python3 --version
```
If Python 3 is installed, you will see the version number. If not, you need to install it. The installation method depends on your operating system.

#### For Windows:
- Download the Python installer from [the official Python website](https://www.python.org/downloads/).
- Run the installer and follow the on-screen instructions.

#### For macOS:
- Install Homebrew (if not already installed) by running in the terminal:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
- Then install Python 3 using Homebrew:
   ```bash
   brew install python3
   ```

#### For Linux:
Most Linux distributions come with Python pre-installed. If not, you can install it using your distribution's package manager. For example, on Ubuntu or Debian:
```bash
sudo apt-get update
sudo apt-get install python3
```
2. Install the required Python libraries using pip:
   ```bash
   pip install requests yaml logging colorama
   ```
3. Place the `health_check.py` script in your desired directory.
To get the health check script from the GitHub repository, use the following command:
```bash
git clone https://github.com/PashaSamets/health-check.git
```
This will clone the repository to your local machine, and you can find the `health_check.py` script in the cloned directory.

## Usage
To run the script, use the following command in the terminal:
```bash
python3 health_check.py path/to/your/urls.yaml
```
Replace `path/to/your/urls.yaml` with the actual path to your YAML file. This file should contain the endpoint configurations like URL, request method, headers, etc. The script requires this file to function properly.

## Logging
The script logs its output to a file named `health_check.log`. This file contains timestamps, log levels, and messages related to the health checks performed. Check this file to see the status of each endpoint the script has checked.
