import os
import subprocess
import directories as dirs

# https://stackoverflow.com/a/5189144/5724706
# TODO: this command works from terminal but not from python, why?
git_log_first_commit = 'git log --pretty=format:%as --reverse | head -1'

# https://stackoverflow.com/a/1007545/5724706
rev_list_first_commit = 'git rev-list --format=%as --max-parents=0 HEAD'


repos = os.listdir(dirs.repos_dir)
output = open('first_commits.txt', 'w')
for repo in repos:
    repo_path = f'{dirs.repos_dir}/{repo}'
    print(repo)
    output = subprocess.call(rev_list_first_commit, cwd=repo_path)
    print(output)
    # subprocess.call('git log --pretty=format:%as --reverse | head -1', cwd=repo_path)
    # print(output)
