import uuid
from datetime import datetime

class Logger:
    def __init__(self, logfile="error.log"):
        self.logfile = logfile

    def log(self, filename, error):
        entry = (
            f"{datetime.now()} | "
            f"{uuid.uuid4()} | "
            f"{filename} -> {error}\n"
        )
        with open(self.logfile, "a") as f:
            f.write(entry)
