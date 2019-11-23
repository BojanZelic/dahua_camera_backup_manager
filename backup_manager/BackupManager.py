import os


class BackupManager:
    path = None

    def __init__(self, path):
        self.path = path

    def start(self):
        files = self.get_unconverted_files()
        print(files)

    def get_unconverted_files(self):
        all_files = []

        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.dav'):
                    all_files.append(file)

        return all_files

