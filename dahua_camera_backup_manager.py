import argparse
import logging
import os
import sys

from backup_manager.BackupManager import BackupManager


def init_arg_parser():
    p = argparse.ArgumentParser()
    p.add_argument('path', help="The path where the backup stores camera files",
                   default=os.environ.get('DAHUA_PATH', None))
    return p

def init_logger():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

if __name__ == '__main__':
    init_logger()
    parser = init_arg_parser()
    args = parser.parse_args()
    BackupManager(args.path).start()
