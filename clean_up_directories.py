#!/usr/bin/env python
"""
Used to clean up non-audio files in music directory.  Remove files and empty directories
"""

import os
import argparse
import sys
import datetime

class CleanUpDirectories():
    def __init__(self, args):
        """

        """
        try:
            self._input_dir = args['INPUT_DIR']
            if args['FILE_TYPE'].lower() == 'audio':
                self._file_type = ['.mp3', '.m4a', '.flac', '.ape', '.ogg']
            else:
                print 'Incorrect file type selected.  Exiting'
                sys.exit()
        except TypeError:
            sys.exit()
        self.clean_up_files()

    def clean_up_files(self):
        time_start = datetime.datetime.utcnow()
        files_to_clean = [[dp, f] for dp, _, filenames in os.walk(self._input_dir) for f in filenames if
                         os.path.splitext(f)[1].lower() not in self._file_type]
        #total_file_count = len(files_to_clean)
        file_count = 0
        dir_count = 0
        log_file_path = os.path.join(self._input_dir, 'cleanupfiles.log')
        with open(log_file_path, 'w') as log_file:
            for directory, f in files_to_clean:
                current_file = os.path.join(directory, f)
                os.remove(current_file)
                out = '[Deleted file]: {0}\n'.format(current_file)
                log_file.write(out)
                file_count += 1
                if not os.listdir(directory):
                    os.rmdir(directory)
                    out = '[Deleted directory]: {0}\n'.format(directory)
                    dir_count += 1
                    log_file.write(out)
        time_delta = datetime.datetime.utcnow().replace(microsecond=0) - time_start.replace(microsecond=0)
        print 'Files removed: {0}'.format(file_count)
        print 'Directories removed: {0}'.format(dir_count)
        print 'Process time: {0}'.format(time_delta)

#====================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        action="store_true", default=False)
    parser.add_argument('INPUT_DIR', help='directory containing the sub directories or files to process')
    parser.add_argument('FILE_TYPE', help='type of audio file to convert')
    args = vars(parser.parse_args())
    CleanUpDirectories(args)
else:
    pass

# exit file





