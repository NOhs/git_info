"""
Module to get information about the git repository one is currently in.
"""
import sys
import subprocess

def _check_output(command_list):
    return subprocess.check_output(command_list, stderr=subprocess.STDOUT).decode("utf-8").strip()

def get_git_info():
    """
    Returns a dictionary with useful info of the current (i.e. of the current working directory)
    git repository.

    Currently the following keys are defined:
    - sha1
    - is_dirty
    - branch
    - tag
    - last_commit_time
    - last_commit_subject
    """
    git_info = {}
    git_info['sha1'] = _check_output(['git', 'describe', '--always', '--dirty', '--abbrev=40', '--match="NoTagHasThisNaMe"'])
    git_info['is_dirty'] = git_info['sha1'].endswith('-dirty')
    git_info['branch'] = _check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    git_info['tag'] = _check_output(['git', 'describe', '--always', '--dirty', '--tags'])
    git_info['last_commit_time'] = _check_output(['git', 'log', '-1', '--format=%ad', '--date=local'])
    git_info['last_commit_subject'] = _check_output(['git', 'log', '-1', '--format=%s'])

    return git_info

def _replace_placeholder(
        file,
        bool_format=str):

    git_info = get_git_info()
    script = file.read()
    for key, value in git_info.items():
        if type(value) is bool:
            script = script.replace("@{0}@".format(key), bool_format(value))
        elif isinstance(value, str):
            script = script.replace("@{0}@".format(key), value)
        else:
            pass

    return script


if __name__ == "__main__":
    with open(sys.argv[1]) as header:
        with open(sys.argv[3], 'w') as output:
            if sys.argv[2] == "cpp":
                output.write(_replace_placeholder(
                    header, bool_format=lambda x: str(x).lower()))
            if sys.argv[2] == "python":
                output.write(_replace_placeholder(header))
