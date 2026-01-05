from ftplib import FTP

class FTPClient:
    def __init__(self, host, user, password, port=2121):
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(user, password)

    def list_files(self):
        return self.ftp.nlst()

    def download(self, filename):
        with open(filename, 'wb') as f:
            self.ftp.retrbinary(f"RETR {filename}", f.write)

    def close(self):
        self.ftp.quit()
