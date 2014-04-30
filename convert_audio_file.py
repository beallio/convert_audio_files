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
            self._remove_source_file = args['--remove-source-file']
        except:
            sys.exit()
        self.convert_files()

    def convert_files(self):
        if self._file_type[0] != '.':
            self._file_type = '.' + self._file_type

        files_to_edit = [[dp, f] for dp, _, filenames in os.walk(self._input_dir) for f in filenames if
                         f.lower().endswith(self._file_type)]
        total_file_count = len(files_to_edit)
        if total_file_count > 0:
            file_count = 0
            for directory, f in files_to_edit:
                input_file = os.path.join(directory, f)
                output_file = os.path.join(directory, os.path.splitext(f)[0] + '.flac')
                file_count += 1
                progress_pct = (file_count / float(total_file_count)) * 100
                print 'Processing {0}/{1}...{2:.1f}% complete'.format(file_count, total_file_count, progress_pct)
                subprocess.call(['ffmpeg', '-i', input_file, output_file])
                if self._remove_source_file:
                    os.remove(input_file)
            print 'Process complete. {0} files processed.'.format(total_file_count)
        else:
            print 'No files found.'

#====================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        action="store_true")
    parser.add_argument('-R', '--remove-source-file', help='remove source file after conversion', action="store_true")
    parser.add_argument('INPUT_DIR', help='directory containing the sub directories or files to process')
    parser.add_argument('FILE_TYPE', help='type of audio file to convert')
    args = vars(parser.parse_args())
    ConvertFiles(args)
else:
    pass

# exit file





