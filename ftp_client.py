from ftplib import FTP_TLS
import ssl
import os

class FTPClient:
    def __init__(self, host, user, password, port=21, remote_dir="."):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.remote_dir = remote_dir

        self.ftp = FTP_TLS(timeout=30)

        # Connect and secure control channel
        self.ftp.connect(host=host, port=port)
        self.ftp.auth()      # Secure control channel
        self.ftp.prot_p()    # Secure data channel
        self.ftp.login(user=user, passwd=password)
        self.ftp.set_pasv(True)  # Passive mode

        # Change to home directory if specified
        if remote_dir:
            try:
                self.ftp.cwd(remote_dir)
            except Exception as e:
                print(f"[WARNING] Could not change directory to {remote_dir}: {e}")

        print("[INFO] FTPS Connected Successfully")

    def list_files(self):
        files = []
        try:
            # Safe method for macOS SSL: NLST first
            self.ftp.retrlines("NLST", files.append)
        except ssl.SSLError:
            # Fallback to empty list if SSL shutdown occurs
            print("[WARNING] SSL issue with NLST, returning empty list")
            files = []
        return files

    def download_file(self, filename, local_dir="sample_data"):
        os.makedirs(local_dir, exist_ok=True)
        local_path = os.path.join(local_dir, filename)
        try:
            with open(local_path, "wb") as f:
                self.ftp.retrbinary(f"RETR {filename}", f.write)
            print(f"[INFO] Downloaded: {filename}")
        except Exception as e:
            print(f"[ERROR] Failed to download {filename}: {e}")

    def close(self):
        try:
            self.ftp.quit()
        except:
            self.ftp.close()
