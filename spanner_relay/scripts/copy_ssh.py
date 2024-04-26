import subprocess
import yaml
from dotenv import load_dotenv
import os

NETWORK_NAME = "rls_network"
CONTAINER_NAME_PREFIX = "roach"
HOSTS_FILE = '/home/ubuntu/share/crdb_new/crdb_scripts/hosts.yml'
NETWORK_BASE = "10.62.0"
IMAGE_NAME = "rjgong/crdb:v2"
CONTAINERS_FILE = "./containers.yml"
SSH_KEY = "\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZRnauj62ueIcOB/XC/p/++g2wtN0wrD6U0v9Q/W/qKmBS1pbzq9OFVXwsJKoL6xt+lYM6zZR2S3EdXEdoxZoBP6+H2JwJphMM6vdq+W4MsKE+Dj/ua6thtmoJZFVzMuprW4xvLLusdhdmFZgtRAxOpwgGpqsAKBx67S8fZcUuvEgtAs9n8S7TnfkWuve1jMoxeaNdgRPCaTpiknWtjmQorzEbLQXIl3bm6wjH1w7LHDL9M4Rt1KqKrnAvE9CPWxS0R//vMoUyc/P03SZz4Wltaz8e316ztWSaVOZIlbgR05zwmN8LP4vOS6iEtwM6WWkpoUJ+Xe9ZytrCxqc0Ki7R root@2dbd44fb9cb2\""

load_dotenv('hosts.env')
hosts = os.getenv('HOSTS').split(',')

containers = []

for i in range(len(hosts)):
    # each region takes a subnet
    host = hosts[i % len(hosts)]
    print(host)
    #print(PORT1, PORT2)
    #ssh_command = "sudo mount -t nfs 103.4.15.248:/home/ubuntu/share share && sudo docker start " + container_name
    ssh_command = "sudo echo " + SSH_KEY + " >> ~/.ssh/authorized_keys"
    print(ssh_command)
    subprocess.call(['ssh', host, ssh_command])

with open(CONTAINERS_FILE, 'w+') as f:
    data = {}
    data['containers'] = containers
    yaml.dump(data, f)
    


    