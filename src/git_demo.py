import subprocess

# windows
print('On Windows:')
subprocess.call(['python', '--version'])
subprocess.call(['git', '--version'])
# subprocess.call(['cmd', 'dir', '/A'])


print("On WSL:")
subprocess.call(['wsl', 'python3', '--version'])
subprocess.call(['wsl', 'git', '--version'])
subprocess.call(['wsl', 'pwd'], cwd='.')
subprocess.call(['wsl', 'pwd'], cwd='..')
# subprocess.call(['wsl', 'git', 'init'], cwd='..')
# subprocess.call(['wsl', 'git', 'status'], cwd='..')

repo_name = 'openfeign/feign'

project_name = repo_name.split('/')[1]
repo_link = f'https://github.com/{repo_name}.git'
clone_dir = f'../cloned/{project_name}'
print(f'Cloning {repo_link}')
output = subprocess.call(['git', 'clone', repo_link, clone_dir])
print('Done!')
# print(output)

