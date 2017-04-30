"""
Module that checks if the current directory
is a git repository or is within one
"""

import subprocess
from sub_proc import _check_output

try:
    _check_output(['git', '-C', '.', 'rev-parse'])
    print("True")
except subprocess.CalledProcessError:
    print("False")
