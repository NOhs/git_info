import subprocess
 
def _check_output(command_list):
    return subprocess.check_output(command_list, stderr=subprocess.STDOUT).decode("utf-8").strip()

