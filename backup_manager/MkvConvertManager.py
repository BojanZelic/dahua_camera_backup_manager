import logging
import os
import subprocess

from pymkv import MKVFile, expanduser, sp

class MkvConvertManager:
    def convert(self, input, output):
        logging.info('Converting File: {0}'.format(input))
        mkv = MKVFile()
        mkv.add_track(input)
        try:
            self.mux(mkv, output)
        except subprocess.CalledProcessError as err:
            logging.error(err.output)
            return False

        logging.info('Converted File: {0}'.format(output))
        logging.info('Deleting File: {0}'.format(input))
        os.remove(input)
        os.remove(input.replace('.dav', '.idx'))
        return True

    def mux(self, mkv, output_path):
        output_path = expanduser(output_path)
        command = mkv.command(output_path)
        logging.info('Running with command:\n"' + command + '"')
        return sp.check_output(mkv.command(output_path, subprocess=True))