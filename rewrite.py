import subprocess
import datetime
import os

def run(cmd, env=None):
    return subprocess.check_output(cmd, env=env, shell=True).decode('utf-8').strip()

commits = run('git rev-list --reverse HEAD').split('\n')
if not commits:
    exit(0)

start_date = datetime.datetime(2026, 5, 4, 10, 0, 0)
end_date = datetime.datetime(2026, 6, 22, 18, 0, 0)

num_commits = len(commits)
if num_commits > 1:
    delta = (end_date - start_date) / (num_commits - 1)
else:
    delta = datetime.timedelta(0)

new_parent = None
env_base = os.environ.copy()

for i, commit in enumerate(commits):
    current_date = start_date + delta * i
    date_str = current_date.strftime('%Y-%m-%dT%H:%M:%S')
    
    tree = run(f'git log -1 --format=%T {commit}')
    msg = run(f'git log -1 --format=%B {commit}')
    
    env = env_base.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    if new_parent:
        cmd = f'git commit-tree {tree} -p {new_parent} -m "{msg}"'
    else:
        cmd = f'git commit-tree {tree} -m "{msg}"'
        
    new_parent = run(cmd, env=env)

if new_parent:
    branch = run('git branch --show-current')
    if not branch:
        branch = "main"
    run(f'git update-ref refs/heads/{branch} {new_parent}')
    print(f"History rewritten. Total commits: {num_commits}")
