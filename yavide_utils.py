import subprocess
from subprocess import call
import shlex

class YavideUtils():
    @staticmethod
    def file_type_to_programming_language(file_type):
        if (file_type == '.c' or file_type == '.cpp' or file_type == '.cc' or
            file_type == '.h' or file_type == '.hpp'):
            return 'Cxx'
        elif (file_type == '.java'):
            return 'Java'
        else:
            return ''

    @staticmethod
    def programming_language_to_extension(programming_language):
        if (programming_language == 'Cxx'):
            return ['.c', '.cpp', '.cc', '.h', '.hpp']
        elif (programming_language == 'Java'):
            return ['.java']
        else:
            return ''

    @staticmethod
    def send_vim_remote_command(vim_instance, command):
        cmd = 'vim --servername ' + vim_instance + ' --remote-send "<ESC>' + command + '<CR>"'
        call(shlex.split(cmd))

