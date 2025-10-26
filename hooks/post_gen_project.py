from pathlib import Path
import subprocess

# rename config file
temppath = Path('config.toml.temp')
defpath = Path('config.toml')

if temppath.exists():
    temppath.rename(defpath)

# initiate uv project
subprocess.run(['uv', 'init', '--bare', '--vcs', 'git'])

# create a virtualenv
subprocess.run(['uv', 'venv'])

# commit created project to git
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Initiated project {{cookiecutter.project_name}}'])