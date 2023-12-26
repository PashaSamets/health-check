#importing modules
import requests
import time
import yaml
import logging
import argparse
from colorama import init, Fore, Back, Style

#configuring logging
logging.basicConfig(filename='health_check.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

#reading endpoints from YAML
def read_endpoints_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        endpoints = []
        for entry in data:
            name = entry.get('name', 'Unnamed endpoint')
            url = entry['url']
            method = entry.get('method', 'GET').upper()
            headers = entry.get('headers', {})
            body = entry.get('body')
            endpoints.append(Endpoint(name, url, method, headers, body))
        return endpoints

class Endpoint:
    def __init__(self, name, url, method="GET", headers=None, body=None):
        self.name = name
        self.url = url
        self.method = method
        self.headers = headers if headers is not None else {}
        self.body = body
        self.up_count = 0
        self.total_count = 0

#perform a health check on the endpoint
    def check_health(self):
        try:
            start_time = time.time()
            if self.method == "GET":
                response = requests.get(self.url, headers=self.headers)
            elif self.method == "POST":
                response = requests.post(self.url, headers=self.headers, data=self.body)
            elif self.method == "PUT":
                response = requests.put(self.url, headers=self.headers, data=self.body)
            elif self.method == "PATCH":
                response = requests.patch(self.url, headers=self.headers, data=self.body)
            elif self.method == "DELETE":
                response = requests.delete(self.url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {self.method}")

            self.total_count += 1
#calculate latency            
            latency = (time.time() - start_time) * 1000
#log the result and updates the counts for calculating availability            
            if 200 <= response.status_code < 300 and latency < 500:
                self.up_count += 1
                logging.info(f"Endpoint with name {Fore.GREEN}{self.url} {self.name}{Style.RESET_ALL} has HTTP response code {response.status_code} and response latency {latency:.2f} ms => UP")
                return True
            elif latency >= 500:
                logging.warning(f"Endpoint with name {Fore.GREEN}{self.url} {self.name}{Style.RESET_ALL} has HTTP response code {response.status_code} and response latency {latency:.2f} ms => DOWN (response latency is not less than 500 ms)")
                return False
            else:
                logging.warning(f"Endpoint with name {Fore.GREEN}{self.url} {self.name}{Style.RESET_ALL} has HTTP response code {response.status_code} and response latency {latency:.2f} ms => DOWN")
                return False
        except Exception as e:
            logging.error(f"Error checking {self.name} ({self.url}): {e}")
            return False

#calculate the availability of the endpoint
    def get_availability_percentage(self):
        if self.total_count == 0:
            return 0
        return (self.up_count / self.total_count) * 100

#continuously check the health of all endpoints in a loop
def automate_health_check(endpoints, interval_seconds):
    try:
        while True:
            for endpoint in endpoints:
                endpoint.check_health()
            for endpoint in endpoints:
                availability_msg = f"{endpoint.url} has {endpoint.get_availability_percentage():.0f}% availability percentage"
                print(availability_msg)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
        print("Program terminated by user.")

#command-line argument parsing
parser = argparse.ArgumentParser(description="Automated Health Check for URLs")
parser.add_argument('url_file', help="Path to the YAML file containing URLs")
args = parser.parse_args()

endpoints = read_endpoints_from_yaml(args.url_file)
interval = 15
automate_health_check(endpoints, interval)