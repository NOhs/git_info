import git_info

with open('python_git.out', 'w') as txt_file:
    txt_file.write("SHA1:  "+ str(git_info.SHA1) + "\n")
    txt_file.write("Is dirty:  "+ str(git_info.IS_DIRTY) + "\n")
    txt_file.write("Branch name:  "+ str(git_info.BRANCH) + "\n")
    txt_file.write("Tag:  "+ str(git_info.TAG) + "\n")
    txt_file.write("Commit time:  "+ str(git_info.LAST_COMMIT_TIME) + "\n")
    txt_file.write("Last commit subject:  "+ str(git_info.LAST_COMMIT_SUBJECT) + "\n")
