# Health Check Script

## Introduction
This Python script is designed for performing health checks on various web endpoints. It sends requests to these endpoints and logs their status, helping in monitoring the health and availability of web services.

## Requirements
- Python 3.x
- Required Python libraries: `requests`, `yaml`, `logging`, `colorama`

## Setup
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using pip:
   ```bash
   pip install requests yaml logging colorama
   ```
3. Place the `health_check.py` script in your desired directory.


## Usage
To run the script, use the following command in the terminal:
```bash
python3 health_check.py ~/urls/urls.yaml
```
Replace `~/urls/urls.yaml` with the actual path to your YAML file. This file should contain the endpoint configurations like URL, request method, headers, etc. The script requires this file to function properly.
## Logging
The script logs its output to a file named `health_check.log`. This file contains timestamps, log levels, and messages related to the health checks performed. Check this file to see the status of each endpoint the script has checked.



## Advanced Usage
To run the script with a specific YAML file containing the endpoint configurations, use the following command:
```bash
python3 health_check.py path/to/your/urls.yaml
```
Replace `path/to/your/urls.yaml` with the actual path to your YAML file. This file should contain the endpoint configurations like URL, request method, headers, etc.
