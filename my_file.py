'''

https://safjan.com/mastering-temporary-files-and-directories-with-python-tempfile-module/
https://stackoverflow.com/questions/847850/cross-platform-way-of-getting-temp-directory-in-python
https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories

'''
import os
from pathlib import Path
import platform
import tempfile
import shutil
import glob

def get_tempdir():
    tempdir = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
    return tempdir

def path_mkdir(pathname="/my/directory"):
    '''
    create a directory at a given path, and also create any missing parent directories along that path
    '''
    from pathlib import Path
    Path(pathname).mkdir(parents=True, exist_ok=True)


def path_makedir(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)


def path_join(*args):
    """
    eg: os.path.join(['home', 'user', 'documents', 'report.txt'])
    """
    return os.path.join(*args) # unpack using the * operator


def file_delete(filename):
    """delete file if exist """
    if os.path.exists(filename):
        os.remove(filename)


def file_readlines(filename):
    """read file to lines """
    with open(filename, "r") as file_ptr:
        return [line.rstrip() for line in file_ptr.readlines()]


def file_readalltext(filename):
    """file read as text"""
    with open(filename, "r") as file:
        return file.read()


def file_appendtext(filename, text):
    """file append text,  creates dir if not exist"""
    path_makedir(filename)
    with open(filename, "a") as file_ptr:
        file_ptr.write(text)

        
def file_writetext(filename, text):
    """file write text"""
    # makedirs(dirname(filename), exist_ok=True)
    with open(filename, "w") as file_ptr:
        file_ptr.write(text)


def file_writelines(filename, datalist):
    """file write list separated with newline"""
    file_writetext(filename,"\n".join(datalist))


def print_to_file(data, filename="_run.txt", filepath=""):
    """print to file, becomes append if file exists"""
    filepath = filepath if filepath else get_tempdir()
    filename = path_join(filepath, filename)
    with open(filename, "a") as file_ptr:
        print(data, file=file_ptr)


def save_as_json(df, outfile='output.json'):
    # Convert DataFrame to JSON and save to a file
    # The 'orient' parameter controls the JSON structure.
    # 'records' is often a suitable choice for JSON files, as it represents each row as a separate JSON object.
    df.to_json(outfile, orient='records', indent=4)


def copy_all_files(source_folder, target_folder):
    """
    copy_all_files("source_folder", "target_folder")
    """
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        if os.path.isfile(source_file):
            shutil.copy(source_file, target_folder)


def copy_files_with_extension(source_folder, target_folder, extension):
    """
    copy_files_with_extension("source_folder", "target_folder", ".txt")
    """
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        if os.path.isfile(source_file) and filename.endswith(extension):
            shutil.copy(source_file, target_folder)


def copy_files_with_pattern(source_folder, target_folder, pattern):
    """
    copy_files_with_pattern('source_folder', 'target_folder', 'report_*')
    """
    for file_path in glob.glob(os.path.join(source_folder, pattern)):
        if os.path.isfile(file_path):
            shutil.copy(file_path, target_folder)


def UnitTest():
    ''' selective unit tests '''
    print(get_tempdir())
    print_to_file("test print to temp dir")
    file_writelines("nums.txt", ['88103219', '88013219', '80866219'])
