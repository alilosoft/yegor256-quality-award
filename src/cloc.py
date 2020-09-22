import os
import subprocess
import directories as dirs

repos = os.listdir(dirs.repos_dir)
output = open('cloc_results.txt', 'w')
for repo in repos:
    repo_path = f'{dirs.repos_dir}/{repo}'
    print('repo: '+repo)
    subprocess.call([f'{dirs.base_dir}/cloc-1.88.exe', repo], cwd=dirs.repos_dir)
    # print(output)
