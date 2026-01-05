class FileTracker:
    def __init__(self):
        self.processed = set()

    def is_duplicate(self, filename):
        return filename in self.processed

    def mark_processed(self, filename):
        self.processed.add(filename)
