import requests
from datetime import datetime

class Logger:
    def __init__(self):
        self.log_file = "error.log"

    def get_uuid(self):
        try:
            response = requests.get("https://www.uuidtools.com/api/generate/v1")
            return response.json()[0]
        except:
            return "LOCAL-UUID"

    def log(self, filename, error):
        uid = self.get_uuid()
        timestamp = datetime.now()
        with open(self.log_file, "a") as f:
            f.write(f"{timestamp} | {uid} | {filename} -> {error}\n")