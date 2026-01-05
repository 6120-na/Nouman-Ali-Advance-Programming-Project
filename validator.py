import csv
import os
import re

REQUIRED_HEADERS = [
    "batch_id","timestamp",
    "reading1","reading2","reading3","reading4","reading5",
    "reading6","reading7","reading8","reading9","reading10"
]

def valid_filename(name):
    return re.match(r"MED_DATA_\d{14}\.csv", name)


def validate_csv_content(path):
    if os.path.getsize(path) == 0:
        return False, "Empty file"

    with open(path) as f:
        reader = csv.reader(f)
        headers = next(reader, None)

        if headers != REQUIRED_HEADERS:
            return False, "Invalid headers"

        batch_ids = set()

        for row in reader:
            if len(row) != 12:
                return False, "Missing columns"

            batch = row[0]
            if batch in batch_ids:
                return False, "Duplicate batch_id"
            batch_ids.add(batch)

            readings = row[2:]
            for r in readings:
                try:
                    value = float(r)
                    if value >= 10:
                        return False, "Invalid reading"
                except:
                    return False, "Non-numeric value"

    return True, None


def validate_csv(path, tracker):
    # filename check
    filename = os.path.basename(path)
    if not valid_filename(filename):
        return False, "Invalid filename format"

    # duplicate file check (tracker)
    if tracker.is_duplicate(filename):
        return False, "Duplicate batch_id"

    # content validation
    is_valid, error = validate_csv_content(path)
    if not is_valid:
        return False, error

    tracker.mark_processed(filename)
    return True, None
