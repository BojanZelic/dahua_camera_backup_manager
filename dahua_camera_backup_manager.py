import argparse
import os

from backup_manager.BackupManager import BackupManager


def init_arg_parser():
    p = argparse.ArgumentParser()
    p.add_argument('path', help="The path where the backup stores camera files",
                   default=os.environ.get('DAHUA_PATH', None))
    return p


if __name__ == '__main__':
    parser = init_arg_parser()
    args = parser.parse_args()
    BackupManager(args.path).start()
