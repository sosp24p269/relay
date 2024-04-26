import paramiko
import yaml

NETWORK_NAME = "rls_network"
HOSTS_FILE = '/home/ubuntu/share/crdb_new/crdb_scripts/hosts.yml'
NETWORK_BASE = "10.62.0"
IMAGE_NAME = "rjgong/crdb:v2"

hosts = [] 
with open (HOSTS_FILE, 'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    hosts = data['hosts']

containers = []
join = ','.join(hosts)
print(join)


port = 22
username = 'ubuntu'
key_file = '/home/ubuntu/.ssh/id_rsa'
private_key = paramiko.RSAKey.from_private_key_file(key_file)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#regions = ["us-east-1", "us-west-1", "us-west-2"]
#zones = ["us-east-1a", "us-west-1a", "us-west-2"]


postgres = ""

for i in range(len(hosts)):

    port1 = i + 8080
    port2 = i + 26257
    network = i + 160

    ip = NETWORK_BASE + str(network)

    host = hosts[i]
    # 连接远程服务器
    ssh.connect(host, port, username, pkey=private_key)

    #ssh_command = "cockroach start --insecure --advertise-addr=" + host + " --join=" + join + "--cache=.25 --max-sql-memory=.25 --locality=region=" + regions[i // 3] + ",zone=" + zones[i // 3] + " --background"
    ssh_command = "./share/crdb_new/cockroach start --insecure --advertise-addr=" + host + " --join=" + join + " --cache=.25 --locality=rack=" + str(i // 3) + " --background"
    #cockroach start --insecure --advertise-addr=<node1 internal address> --join=<node1 internal address>,<node2 internal address>,<node3 internal address> --cache=.25 --locality=rack=0
    #ssh_command = "cockroach start --insecure --advertise-addr=" + host + " --join=" + join + "--cache=.25 --max-sql-memory=.25 --locality=region=" + regions[i // 3] + ",zone=" + zones[i // 3] + " --background"
    #ssh_command = "cockroach start --insecure --advertise-addr=" + host + " --join=" + join + "--cache=.25 --max-sql-memory=.25" + " --background"
    print(ssh_command)
    
    postgres += "postgres://root@"
    postgres += host
    postgres += "?sslmode=disable "
    # 创建一个SFTP客户端
    ssh.exec_command(ssh_command)

#print(postgres)