import subprocess
import sys
import yaml
import os
from dotenv import load_dotenv

# Command to execute on each host
commands = """
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
ssh-keygen -q -N "" -f ~/.ssh/id_rsa
sudo apt install nfs-common -y
sudo apt install nfs-server -y
sudo systemctl start nfs-server
sudo systemctl start rpcbind
sudo systemctl enable nfs-server
sudo systemctl enable rpcbind
sudo docker swarm join --token SWMTKN-1-38vswtc8q7w04f00h6q8x0s8vo9k36ecsgxn9b9sem8wdyfxx9-6wbhlrx2iwjedmjym39qe3f9c 103.4.15.248:2377
mkdir share
sudo exportfs -r 
sudo mount 103.4.15.248:/home/ubuntu/share share
"""

def execute_commands_on_host(host):
    try:
        # Use SSH to connect to the host and execute the commands
        ssh_command = f"ssh {host} '{commands}'"
        print(ssh_command)
        subprocess.run(ssh_command, shell=True, check=True)
        print(f"Commands executed successfully on {host}")
    except subprocess.CalledProcessError:
        print(f"Failed to execute commands on {host}")

def main():
    # Read hosts from hosts.env file
    load_dotenv('hosts.env')
    hosts = os.getenv('HOSTS').split(',')

    # Execute commands on each host
    for host in hosts:
        print(host)
        execute_commands_on_host(host)

if __name__ == "__main__":
    main()