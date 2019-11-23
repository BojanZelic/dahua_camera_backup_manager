import os
import logging

from backup_manager.MkvConvertManager import MkvConvertManager


class BackupManager:
    path = None

    def __init__(self, path):
        self.path = path

    def start(self):
        mkv_convert = MkvConvertManager()
        files = self.get_unconverted_files()

        for file in files:
            mkv_convert.convert(file, file.replace('.dav', '.mkv'))

    def get_unconverted_files(self):
        all_files = []

        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.dav'):
                    all_files.append(os.path.join(root, file))

        return all_files



