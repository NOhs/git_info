"""
Module that checks if the current directory
is a git repository or is within one
"""

import sys
import subprocess
from sub_proc import _check_output

try:
    _check_output(['git', '-C', '.', 'rev-parse'])
    remotes = _check_output(['git', 'remote', '-v'])
    if sys.argv[1] in remotes:
        print("True")
    else:
        print("False")
except subprocess.CalledProcessError:
    print("False")
