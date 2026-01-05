from ftp_client import FTPClient
from validator import validate_csv
from logger import Logger
from tracker import FileTracker
import os, shutil

FTP_HOST = "localhost"
FTP_USER = "user"
FTP_PASS = "12345"
FTP_PORT = 2121


def show_menu():
    print("\n" + "=" * 30)
    print("     MEDDATA PIPELINE")
    print("=" * 30)
    print("1. Generate Sample CSV Files")
    print("2. Validate Local Folder (sample_data/)")
    print("3. Download & Validate from FTP")
    print("4. Exit")
    print("=" * 30)


def generate_samples():
    print("\n[INFO] Generating sample CSV files...")
    os.system("python generate_csv.py")
    print("[SUCCESS] Sample files generated.\n")


def validate_local_folder():
    print("\n[INFO] Validating files in sample_data/ folder...")

    tracker = FileTracker()
    logger = Logger()

    src = "sample_data"
    os.makedirs("valid", exist_ok=True)
    os.makedirs("invalid", exist_ok=True)

    if not os.path.exists(src):
        print("[ERROR] sample_data/ folder not found!")
        return

    for file in os.listdir(src):
        if file.endswith(".csv"):
            filepath = os.path.join(src, file)
            is_valid, error = validate_csv(filepath, tracker)

            if is_valid:
                shutil.move(filepath, f"valid/{file}")
                print(f"{file} -> VALID")
            else:
                shutil.move(filepath, f"invalid/{file}")
                logger.log(file, error)
                print(f"{file} -> INVALID")

    print("[DONE] Local folder validation completed.\n")


def process_ftp_files():
    print("\n[INFO] Connecting to FTP server...")

    ftp = FTPClient(FTP_HOST, FTP_USER, FTP_PASS, FTP_PORT)
    tracker = FileTracker()
    logger = Logger()

    os.makedirs("valid", exist_ok=True)
    os.makedirs("invalid", exist_ok=True)

    files = ftp.list_files()

    for file in files:
        if file.startswith("MED_DATA_") and file.endswith(".csv"):
            ftp.download(file)
            print(f"Processing {file}")

            is_valid, error = validate_csv(file, tracker)
            if is_valid:
                shutil.move(file, f"valid/{file}")
                print(f"{file} -> VALID")
            else:
                shutil.move(file, f"invalid/{file}")
                logger.log(file, error)
                print(f"{file} -> INVALID")

    ftp.close()
    print("[DONE] FTP processing completed.\n")


def main():
    while True:
        show_menu()
        choice = input("Choose option (1-4): ").strip()

        if choice == "1":
            generate_samples()
        elif choice == "2":
            validate_local_folder()
        elif choice == "3":
            process_ftp_files()
        elif choice == "4":
            print("\nExiting MEDDATA Pipeline. Goodbye!")
            break
        else:
            print("[ERROR] Invalid option. Please choose between 1–4.\n")


if __name__ == "__main__":
    main()
