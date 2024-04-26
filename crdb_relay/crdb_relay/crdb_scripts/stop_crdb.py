import yaml
import subprocess

HOSTS_FILE = '/home/ubuntu/share/crdb_new/crdb_scripts/hosts.yml'

hosts = [] 
with open (HOSTS_FILE, 'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    hosts = data['hosts']

for h in hosts:
    ssh_command = "ps -ef | grep cockroach | grep -v grep | awk '{print $2}' | xargs sudo kill -TERM"
    print(h)
    print(ssh_command)
    subprocess.call(['ssh', '-o', 'StrictHostKeyChecking=no', h, ssh_command])

for h in hosts:
    ssh_command = "cd /home/ubuntu/data && sudo rm -rf cockroach-data"
    print(ssh_command)
    subprocess.call(['ssh', h, ssh_command])

