import csv, random

def generate_good(filename):
    with open(filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "batch_id","timestamp",
            *[f"reading{i}" for i in range(1,11)]
        ])
        for i in range(10):
            w.writerow([
                random.randint(1,200),
                "14:01:04",
                *[round(random.uniform(0,9.9),3) for _ in range(10)]
            ])

generate_good("MED_DATA_20240101120101.csv")
