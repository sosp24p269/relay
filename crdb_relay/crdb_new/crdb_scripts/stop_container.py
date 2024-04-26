import yaml
import subprocess

HOSTS_FILE = '/home/ubuntu/share/crdb_new/crdb_scripts/hosts.yml'

hosts = [] 
with open (HOSTS_FILE, 'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    hosts = data['hosts']

for h in hosts:
    print("stopping container on " + h)
    ssh_command = "sudo docker stop $(sudo docker ps -q)"
    print(ssh_command)
    subprocess.call(['ssh', h, ssh_command])

for h in hosts:
    print("stopping container on " + h)
    ssh_command = "sudo docker rm $(sudo docker ps -aq)"
    print(ssh_command)
    subprocess.call(['ssh', h, ssh_command])
