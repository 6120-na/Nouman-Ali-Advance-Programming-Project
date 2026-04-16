from ftp_client import FTPClient
FTP_HOST = "127.0.0.1"        
FTP_USER = "testuser"
FTP_PASS = "test123"
FTP_PORT = 21
REMOTE_DIR = "/"           

LOCAL_DIR = "sample_data"

def process_ftp_files():
    ftp = FTPClient(FTP_HOST, FTP_USER, FTP_PASS, FTP_PORT, REMOTE_DIR)

    files = ftp.list_files()
    if not files:
        print("[INFO] No files found on FTP server.")
    else:
        print(f"[INFO] Found {len(files)} file(s): {files}")

    for f in files:
        ftp.download_file(f, LOCAL_DIR)

    ftp.close()
    print("[DONE] FTP processing completed.\n")

def validate_local_files():
    import os
    if not os.path.exists(LOCAL_DIR):
        print("[ERROR] Local folder does not exist.")
        return
    files = os.listdir(LOCAL_DIR)
    if not files:
        print("[WARNING] No files in local folder.")
    else:
        print(f"[INFO] Local folder contains: {files}")

def main():
    while True:
        print("="*30)
        print("     MEDDATA PIPELINE")
        print("="*30)
        print("1. Generate Sample CSV Files")
        print("2. Validate Local Folder (sample_data/)")
        print("3. Download & Validate from FTP")
        print("4. Exit")
        print("="*30)
        choice = input("Choose option (1-4): ").strip()

        if choice == "1":
            print("[INFO] Sample CSV generation not implemented yet.")
        elif choice == "2":
            validate_local_files()
        elif choice == "3":
            process_ftp_files()
            validate_local_files()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("[ERROR] Invalid choice. Enter 1-4.\n")

if __name__ == "__main__":
    main()
