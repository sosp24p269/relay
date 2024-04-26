import subprocess
import sys
import yaml
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

NETWORK_NAME = "rls_network"
CONTAINER_NAME_PREFIX = "spanner_rls_"

NETWORK_BASE = "10.62.0"
IMAGE_NAME = "rjgong/spanner_rls:v2"

load_dotenv('hosts.env')
hosts = os.getenv('HOSTS').split(',')

containers = []
#sys.argv[2]


def deploy_container(i):
    host = hosts[i % len(hosts)]
    IP = NETWORK_BASE + "." + str(i*1+160)
    containers.append(IP)
    container_name = CONTAINER_NAME_PREFIX + str(i)


    print(host, IP)
    #ssh_command = "sudo docker run -t -d -p 2222:22 -v /home/ubuntu/share/spanner_rls/scripts:/scripts -v /home/ubuntu/share/spanner_rls/spanner_rls:/spanner_rls -v /home/ubuntu/share/spanner_rls/spanner:/spanner --cap-add NET_ADMIN " + " --name " + container_name + " " + IMAGE_NAME + " /bin/bash -c " + "\"service ssh restart && tail -f /dev/null && apt-get install -y python3-dotenv\""
    ssh_command = "echo APTX4869_dockerhub | sudo docker login --username rjgong --password-stdin"
    print(ssh_command)
    #subprocess.call(['ssh', '-o', 'StrictHostKeyChecking=no', host, ssh_command])
    ssh_command = "sudo mount 103.4.15.248:/home/ubuntu/share share && sudo docker stop $(sudo docker ps -q) ; sudo docker rm $(sudo docker ps -aq) ; sudo docker run -t -d -v /home/ubuntu/share/spanner_rls/scripts:/scripts -v /home/ubuntu/share/spanner_rls/spanner_rls:/spanner_rls -v /home/ubuntu/share/spanner_rls/spanner:/spanner -v /home/ubuntu/share/spanner_rls/spanner_rls2:/spanner_rls2 -v /home/ubuntu/share/spanner_rls/spanner2:/spanner2 --cap-add NET_ADMIN --network " + NETWORK_NAME +  " --name " + container_name + " --ip " + IP + " " + IMAGE_NAME + " /bin/bash -c " + "\"service ssh restart && apt-get install -y python3-dotenv && tail -f /dev/null\""
    print(ssh_command)
    result = subprocess.run(['ssh', '-o', 'StrictHostKeyChecking=no', host, ssh_command], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"\033[91mError executing command on {host}: {result.stderr}\033[0m")
    else:
        print(f"\033[92mSuccessfully deployed container on {host}\033[0m")

# 使用ThreadPoolExecutor启动并行任务
num_containers = int(sys.argv[1])
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(deploy_container, range(num_containers))


'''
ssh_command = "sudo docker run -t -d -p 2222:22 -v /home/ubuntu/share/spanner_rls/scripts:/scripts -v /home/ubuntu/share/spanner_rls/spanner_rls:/spanner_rls -v /home/ubuntu/share/spanner_rls/spanner:/spanner --cap-add NET_ADMIN --network " + NETWORK_NAME +  " --name " + container_name + " --ip " + IP + " " + IMAGE_NAME + " /bin/bash -c " + "\"service ssh restart && tail -f /dev/null && apt-get install -y python3-dotenv\""

docker run -d -v /home/ruijie/share/tapir/tapir-master:/tapir-master -v /home/ruijie/share/origin:/origin --cap-add NET_ADMIN --network rls_network --name ingress --ip 10.62.0.150 haozesong/spanner_rls /tapir-master/scripts/tc_ssh.sh 10.62.0.150 
docker run -t -d -v /home/ruijie/share/crdb:/root/crdb -v /home/ruijie/share/cockroach:/root/crdb_origin --cap-add NET_ADMIN --network rls_network --name crdb2 --ip 10.62.0.150 rjgong/crdb:v2



'''