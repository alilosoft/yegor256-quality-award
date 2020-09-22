import subprocess
import os


def clone(repo_name):
    project_name = repo_name.split('/')[1]
    repo_link = f'https://github.com/{repo_name}.git'
    clone_dir = f'../github/{project_name}'
    if os.path.isdir(clone_dir):
        print(f'{repo_name} cloned!')
        return
    print(f'Cloning {repo_link}')
    subprocess.call(['git', 'clone', repo_link, clone_dir])
    print('Done!')


repos = ['traccar/traccar',
         'imrafaelmerino/json-values',
         'openfeign/feign',
         'mcjtymods/rftoolscontrol',
         'yuriykulikov/alarmclock',
         'victorx64/devrating',
         'fleksl/avatar-maker',
         'retejs/rete',
         'onqtam/doctest',
         'dotenv-linter/dotenv-linter']

for repo in repos:
    clone(repo)
