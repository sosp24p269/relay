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

load_dotenv('hosts.env')
hosts = os.getenv('HOSTS').split(',')

containers = []

for i in range(len(hosts)):
    # each region takes a subnet
    host = hosts[i % len(hosts)]
    print(host)
    #print(PORT1, PORT2)
    ssh_command = ["sudo mount 103.4.15.248:/home/ubuntu/share share"]
    
    '''
    ssh_command = [
        "for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done",
        "sudo apt-get update",
        "sudo apt-get install ca-certificates curl gnupg -y",
        "sudo install -m 0755 -d /etc/apt/keyrings",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
        "sudo chmod a+r /etc/apt/keyrings/docker.gpg",
        "echo \
        \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable\" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
        "sudo apt-get update",
        "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y",
        "sudo apt install nfs-common -y",
        "sudo apt install nfs-server -y",
        "sudo systemctl start nfs-server",
        "sudo systemctl start rpcbind",
        "sudo systemctl enable nfs-server",
        "sudo systemctl enable rpcbind",
        "sudo docker swarm join --token SWMTKN-1-3ihpt3grpbd5h579sxfpsmhtguy50gpromictun0hg9fdptv8s-ce1q5sn81b7e5nxe3z7jyrktf 103.4.15.248:2377",
        "mkdir share",
        "sudo exportfs -r",
        "sudo mount 103.4.15.248:/home/ubuntu/share share"
    ]
    '''
    for command in ssh_command:
        print(command)
        subprocess.call(['ssh', '-o', 'StrictHostKeyChecking=no', host, command])

with open(CONTAINERS_FILE, 'w+') as f:
    data = {}
    data['containers'] = containers
    yaml.dump(data, f)
    


    