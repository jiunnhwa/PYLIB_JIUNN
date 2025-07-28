"""
module for process helper functions.

"""

import subprocess


def run_batch_command(batch_file_path = "C:\\path\\to\\your\\script.bat" ):


    # Run the batch file
    # The 'shell=True' argument is necessary to execute the command through the system shell
    # 'capture_output=True' can be used to capture stdout and stderr
    # 'text=True' decodes the output as text
    try:
        result = subprocess.run([batch_file_path], shell=True, capture_output=True, text=True, check=True)
        print("Batch file executed successfully.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch file: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
