import os
import argparse
import subprocess
import sys


class ConvertFiles():
    def __init__(self, args):
        """

        """
        try:
            self._input_dir = args['INPUT_DIR']
            self._file_type = args['FILE_TYPE']
        except:
            sys.exit()
        self.convert_files()

    def convert_files(self):
        if self._file_type[0] != '.':
            self._file_type = '.' + self._file_type

        files_to_edit = [[dp, f] for dp, _, filenames in os.walk(self._input_dir) for f in filenames if
                         f.endswith(self._file_type)]
        for directory, f in files_to_edit:
            input_file = os.path.join(directory, f)
            output_file = os.path.join(directory, os.path.splitext(f)[0] + '.flac')
            subprocess.call(['ffmpeg', '-i', input_file, output_file])
            os.remove(input_file)


#====================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        action="store_true")
    parser.add_argument('INPUT_DIR', help='directory containing the sub directories or files to process')
    parser.add_argument('FILE_TYPE', help='type of audio file to convert')
    args = vars(parser.parse_args())
    ConvertFiles(args)
else:
    pass

# exit file





