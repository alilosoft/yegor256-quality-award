import os
import subprocess
# https://stackoverflow.com/a/5189144/5724706
git_log_first_commit = 'git log --pretty=format:%as --reverse | head -1'

# https://stackoverflow.com/a/1007545/5724706
rev_list_first_commit = 'git rev-list --format=%as --max-parents=0 HEAD'

base_dir = '../../repos'
repos = os.listdir(base_dir)
output = open('first_commits.txt', 'w')
for repo in repos:
    repo_path = f'{base_dir}/{repo}'
    print(repo)
    output = subprocess.call(rev_list_first_commit, cwd=repo_path)
    # subprocess.call('git log --pretty=format:%as --reverse | head -1', cwd=repo_path)
    # print(output)
