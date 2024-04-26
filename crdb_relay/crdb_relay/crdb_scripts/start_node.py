import subprocess
import yaml

NETWORK_NAME = "rls_network"
HOSTS_FILE = '/root/crdb_new/crdb_scripts/hosts.yml'
NETWORK_BASE = "10.62.0."
IMAGE_NAME = "rjgong/crdb:v2"

hosts = [] 
with open (HOSTS_FILE, 'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    hosts = data['hosts']

join = ""

for i in range(1, len(hosts) + 1):
    if i < len(hosts):
        join += f"roach{i}:26357,"
    else:
        join += f"roach{i}:26357"

print(join)

for i in range(len(hosts)):
    # each region takes a subnet
    port1 = i + 8080
    port2 = i + 26257
    network = i + 160

    ip = NETWORK_BASE + str(network)

    container_name = "roach" + str(i + 1) 

    ssh_command = " /root/crdb_new/cockroach start --insecure --advertise-addr=" + container_name + ":26357 --http-addr=" + container_name + ":" + str(port1) + " --listen-addr=" + container_name + ":26357 --sql-addr=" + container_name + ":" + str(port2) + " --insecure --join=" + join + " --cache=.25 --background"
    print(ssh_command)
    print(ip)
    #subprocess.call(['ssh', ip, ssh_command])


#ssh_command = " /root/crdb_new/cockroach start --store=node" + str(i + 1) + " --advertise-addr=" + container_name + ":26357 --http-addr=" + container_name + ":" + str(port1) + " --listen-addr=" + container_name + ":26357 --sql-addr=" + container_name + ":" + str(port2) + " --insecure --join=" + join + " --cache=.25 --background"