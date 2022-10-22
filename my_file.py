


def file_readlines(filename):
    """read file to lines """
    with open(filename, "r") as file_ptr:
        return [line.rstrip() for line in file_ptr.readlines()]


def file_readalltext(filename):
    """file read as text"""
    with open(filename, "r") as file:
        return file.read()

      
def file_writetext(filename, text):
    """file write text"""
    
    makedirs(dirname(filename), exist_ok=True)
    with open(filename, "w") as file_ptr:
        file_ptr.write(text)

      
def print_to_file(data, filename="_run.txt", filepath=""):
    """print to file"""
    filepath = filepath if filepath else getdir_testlist_blwin32win32()
    filename = path_join(filepath, filename)
    with open(filename, "a") as file_ptr:
        print(data, file=file_ptr)
      
