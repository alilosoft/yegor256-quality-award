import os
import subprocess

base_dir = 'D:/Programing/Projects/Freelancing/yegor-qaward2020'
repos_dir = base_dir+'/repos'
repos = os.listdir(repos_dir)
output = open('cloc_results.txt', 'w')
for repo in repos:
    repo_path = f'{repos_dir}/{repo}'
    print('repo: '+repo)
    subprocess.call([f'{base_dir}/cloc-1.88.exe', repo], cwd=repos_dir)
    # print(output)
