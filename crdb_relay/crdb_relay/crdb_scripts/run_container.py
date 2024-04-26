import subprocess
import yaml


NETWORK_NAME = "rls_network"
CONTAINER_NAME_PREFIX = "roach"
HOSTS_FILE = '/home/ubuntu/share/crdb_new/crdb_scripts/hosts.yml'
NETWORK_BASE = "10.62.0"
IMAGE_NAME = "rjgong/crdb:v2"
CONTAINERS_FILE = "./containers.yml"

hosts = [] 
with open (HOSTS_FILE, 'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    hosts = data['hosts']

containers = []

for i in range(len(hosts)):
    # each region takes a subnet
    host = hosts[i % len(hosts)]
    PORT1 = str(i+8080)
    PORT2 = str(i+26357)
    IP = NETWORK_BASE + "." + str(i+160)
    containers.append(IP)
    print(host, IP)
    #print(PORT1, PORT2)
    container_name = CONTAINER_NAME_PREFIX + str(i+1)
    #ssh_command = "sudo docker run -t -d -v /home/ubuntu/share/crdb_new:/root/crdb_new -v /home/ubuntu/share/cockroach:/root/cockroach -v /home/ubuntu/share/crdb_origin:/root/crdb_origin --network host" + " --name " + container_name + " " + IMAGE_NAME
    ssh_command = "sudo docker run -t -d -v /home/ubuntu/share/crdb_new:/root/crdb_new -v /home/ubuntu/share/cockroach:/root/cockroach -v /home/ubuntu/share/crdb_origin:/root/crdb_origin --cap-add NET_ADMIN --network " + NETWORK_NAME + " -p " + PORT1 + ":" + PORT1 + " -p " + PORT2 + ":" + PORT2 + " --name " + container_name + " --ip " + IP + " " + IMAGE_NAME + " /bin/bash -c " + "\"service ssh restart && apt-get update && apt-get install -y python3-dotenv && tail -f /dev/null\""
    print(ssh_command)
    subprocess.call(['ssh', host, ssh_command])

with open(CONTAINERS_FILE, 'w+') as f:
    data = {}
    data['containers'] = containers
    yaml.dump(data, f)

'''
 + " && " + " /root/crdb/cockroach/cockroach start " +  " --advertise-addr=" + container_name + ":26358" + " --http-addr=" + container_name + ":" + PORT1 + " --listen-addr=" + container_name + ":26357" + " --sql-addr=" + container_name + ":" + PORT2 + " --insecure" + " --join=roach1:26357,roach2:26357,roach3:26357 "
    ssh_command = " docker run -d" + " --name=" + container_name + \
                  " --hostname=" + container_name + \
                  " --net=" + NETWORK_NAME + \
                  " -p " + PORT2 + ":" + PORT2 + \ 
                  " -p " + PORT1 + ":" + PORT1 + \
                  " -v " + container_name + ":/test" + \
                  " cockroachdb/cockroach start " + \
                  " --advertise-addr=" + container_name + ":26357" + \
                  " --http-addr=" + container_name + ":" + PORT1 + \
                  " --listen-addr=" + container_name + ":26357" + \
                  " --sql-addr=" + container_name + ":" + PORT2 + \
                  " --insecure" + \
                  " --join=roach1:26357,roach2:26357,roach3:26357 "
" docker run -d \ " + 
" --name " + container_name + " \ " +
" --network " + NETWORK_NAME + " \ " +
" -p " + "26257:26257" + " \ " +
" -p " + "8080:8080" + " \ " +
" -v " + "/home/ubuntu/share/test:/tapir-master" + " \ " +
" rjgong/crdb cd crdb && chmod +x bazelisk-linux-amd64 && cp bazelisk-linux-amd64 /usr/local/bin/bazel && ln -s /usr/local/bin/bazel/bazelisk-linux-amd64 /usr/bin/bazel && ./crdb/cockroach/cockroach start \
  --advertise-addr=roach1:26357 \
  --http-addr=roach1:8080 \
  --listen-addr=roach1:26357 \
  --sql-addr=roach1:26257 \
  --insecure \
  --join=roach1:26357,roach2:26357,roach3:26357
"

" docker volume create --driver local \
  --opt type=nfs4 \
  --opt o=addr=10.22.1.5,rw \
  --opt device=:/share \
  roach " + str(i)

docker run -t -d -v /home/ubuntu/share/crdb/cockroach:/root/cockroach -v /home/ubuntu/share/cockroach:/root/crdb_origin --cap-add NET_ADMIN --network rls_network --name roach10 --ip 10.62.0.190 rjgong/crdb:v2 /root/cockroach/crdb_scripts/tc_ssh.sh 10.62.0.190


docker run -d \
--name=roach1 \
--hostname=roach1 \
-p 26257:26257 \
-p 8080:8080 \
-v /home/ubuntu/share/crdb:/root/crdb -v /home/ubuntu/share/cockroach:/root/crdb_origin \
/root/cockroach/cockroach start \
  --advertise-addr=roach1:26357 \
  --http-addr=roach1:8080 \
  --listen-addr=roach1:26357 \
  --insecure \
  --join=roach1:26357,roach2:26357,roach3:26357 \
  --background


  /root/cockroach/cockroach start \
    --advertise-addr=roach2:26357 \
    --http-addr=roach2:8081 \
    --listen-addr=roach2:26357 \
    --insecure \
    --join=roach1:26357,roach2:26357,roach3:26357


  /root/cockroach/cockroach start \
    --store=node3 \
    --advertise-addr=roach3:26357 \
    --http-addr=roach3:8082 \
    --listen-addr=roach3:26357 \
    --insecure \
    --join=roach1:26357,roach2:26357,roach3:26357


./cockroach start \
  --advertise-addr=roach1:26357 \
  --http-addr=roach1:8080 \
  --listen-addr=roach1:26357 \
  --insecure \
  --sql-addr=roach1:26257 \
  --join=roach1:26357,roach2:26357,roach3:26357 \
  --background

./crdb_scripts/start_node.sh

./cockroach --host=roach1:26357 init --insecure

./cockroach workload fixtures import tpcc \
--warehouses=250 \
'postgres://root@roach2:26257?sslmode=disable'

./cockroach workload init kv \
'postgresql://root@roach1:26257?sslmode=disable' \
--insert-count 300000

cp /root/.cache/bazel/_bazel_root/7dbb1e4f7d0bee92cebfd0a87469e4d9/execroot/com_github_cockroachdb_cockroach/bazel-out/k8-fastbuild/testlogs/pkg/kv/kvserver/tscache/tscache_test/test.log . && chmod 777 test.log

bazel test pkg/kv/kvserver/tscache:all

cp ~/node1/logs/cockroach.log . && chmod 777 cockroach.log

ps -ef | grep bazel | grep -v grep | awk '{print $2}' | xargs kill -9

./cockroach workload run kv \
--duration=1m \
'postgresql://root@roach1:26257?sslmode=disable' \
--concurrency 1000

./cockroach workload run tpcc --warehouses=2500 --ramp=1m --duration=5m 'postgresql://root@roach1:26257?sslmode=disable' 'postgresql://root@roach2:26257?sslmode=disable' 'postgresql://root@roach3:26257?sslmode=disable'

chmod +x crdb/bazelisk-linux-amd64 && cp crdb/bazelisk-linux-amd64 /usr/local/bin/bazel && ln -s /usr/local/bin/bazel/bazelisk-linux-amd64 /usr/bin/bazel && cd cockroach && bazel build pkg/cmd/cockroach && rm cockroach && cp _bazel/bin/pkg/cmd/cockroach/cockroach_/cockroach .

bazel build pkg/cmd/cockroach && rm cockroach && cp _bazel/bin/pkg/cmd/cockroach/cockroach_/cockroach .


ps -ef | grep java | grep -v grep | awk '{print $2}' | sudo xargs kill -9

rm cockroach && cp _bazel/bin/pkg/cmd/cockroach/cockroach_/cockroach .

sudo docker run -t -d -v /home/ubuntu/share/cockroach:/root/cockroach -v /home/ubuntu/share/crdb_origin:/root/crdb_origin --cap-add NET_ADMIN --network rls_network -p 8080:8080 -p 26357:26357 --name roachtest --ip 10.62.0.50 rjgong/crdb:v2 /root/cockroach/crdb_scripts/tc_ssh.sh 10.62.0.50
./cockroach workload init tpcc \
'postgresql://root@roach1:26257?sslmode=disable'

./cockroach workload run tpcc \
--warehouses=2500 \
--duration=1m \
'postgresql://root@roach1:26257?sslmode=disable' \
--concurrency 100



./cockroach workload init ycsb \
'postgresql://root@roach1:26257?sslmode=disable' \
--insert-count 3000000

./cockroach workload run ycsb \
--duration=1m \
'postgresql://root@roach1:26257?sslmode=disable' \
--concurrency 100



./cockroach workload fixtures import tpcc \
--warehouses=500 \
'postgres://root@roach1:26257?sslmode=disable'



./cockroach workload run tpcc \
--warehouses=500 \
--ramp=1m \
--duration=5m \
$(cat addrs)


/root/crdb_origin/cockroach start --store=node1 --advertise-addr=roach1:26357 --http-addr=roach1:8080 --listen-addr=roach1:26357 --sql-addr=roach1:26257 --insecure 
--join=roach1:26357,roach2:26357,roach3:26357,roach4:26357,roach5:26357,roach6:26357,roach7:26357,roach8:26357,roach9:26357,roach10:26357 --background
10.62.0.100
/root/crdb_origin/cockroach start --store=node2 --advertise-addr=roach2:26357 --http-addr=roach2:8081 --listen-addr=roach2:26357 --sql-addr=roach2:26258 --insecure --join=roach1:26357,roach2:26357,roach3:26357,roach4:26357,roach5:26357,roach6:26357,roach7:26357,roach8:26357,roach9:26357,roach10:26357 --background




cockroach start --insecure --advertise-addr=13.39.92.165 --join=13.39.92.165,57.181.129.138,35.76.59.55 --cache=.25 --max-sql-memory=.25 --background

cockroach start --insecure --advertise-addr=57.181.129.138 --join=13.39.92.165,57.181.129.138,35.76.59.55 --cache=.25 --max-sql-memory=.25 --background

cockroach start --insecure --advertise-addr=35.76.59.55 --join=13.39.92.165,57.181.129.138,35.76.59.55 --cache=.25 --max-sql-memory=.25 --background

cockroach init --insecure --host=35.76.59.55

cockroach sql --insecure --host=35.76.59.55

cockroach workload fixtures import tpcc \
--warehouses=100 \
'postgres://root@35.76.59.55:26257?sslmode=disable'

cockroach workload fixtures import tpcc \
--warehouses=500 \
'postgres://root@35.181.176.14:26257?sslmode=disable'

cockroach workload fixtures import tpcc \
--partitions=5 \
--warehouses=13000 \
'postgres://root@35.76.59.55:26257?sslmode=disable'

ulimit -n 100000 && cockroach workload run tpcc \
--partitions=5 \
--warehouses=10000 \
--duration=1m \
--ramp=1ms \
'postgres://root@35.76.59.55:26257?sslmode=disable'

ulimit -n 100000 && cockroach workload run tpcc \
--partitions=5 \
--warehouses=13000 \
--ramp=1m \
--duration=3m \
--concurrency=4096 \
postgres://root@54.64.112.23:26257?sslmode=disable postgres://root@57.181.129.138:26257?sslmode=disable postgres://root@35.76.59.55:26257?sslmode=disable postgres://root@52.88.120.20:26257?sslmode=disable postgres://root@34.210.21.166:26257?sslmode=disable postgres://root@44.224.43.239:26257?sslmode=disable postgres://root@18.168.59.124:26257?sslmode=disable postgres://root@3.8.251.11:26257?sslmode=disable postgres://root@3.9.202.62:26257?sslmode=disable postgres://root@18.162.136.24:26257?sslmode=disable postgres://root@18.162.217.132:26257?sslmode=disable postgres://root@18.167.101.35:26257?sslmode=disable postgres://root@3.208.180.135:26257?sslmode=disable postgres://root@34.206.118.173:26257?sslmode=disable postgres://root@44.214.14.165:26257?sslmode=disable


  - 18.162.136.24
  - 18.162.217.132
  - 18.167.101.35
  - 3.208.180.135
  - 34.206.118.173
  - 44.214.14.165


ulimit -n 100000 && cockroach workload run tpcc \
--partitions=3 \
--warehouses=10000 \
--ramp=1m \
--duration=1m \
postgres://root@54.64.112.23:26257?sslmode=disable postgres://root@57.181.129.138:26257?sslmode=disable postgres://root@35.76.59.55:26257?sslmode=disable postgres://root@52.88.120.20:26257?sslmode=disable postgres://root@34.210.21.166:26257?sslmode=disable postgres://root@44.224.43.239:26257?sslmode=disable postgres://root@18.168.59.124:26257?sslmode=disable postgres://root@3.8.251.11:26257?sslmode=disable postgres://root@3.9.202.62:26257?sslmode=disable



postgres://root@35.76.59.55:26257?sslmode=disable postgres://root@54.64.112.23:26257?sslmode=disable postgres://root@57.181.129.138:26257?sslmode=disable

cockroach workload run tpcc \
--warehouses=100 \
--ramp=1m \
--duration=3m \
postgres://root@54.64.112.23:26257?sslmode=disable postgres://root@57.181.129.138:26257?sslmode=disable postgres://root@35.76.59.55:26257?sslmode=disable postgres://root@35.181.176.14:26257?sslmode=disable postgres://root@15.188.72.230:26257?sslmode=disable postgres://root@13.39.92.165:26257?sslmode=disable


ulimit -n 100000 && cockroach workload run tpcc \
--warehouses=100 \
--duration=10m \
--ramp=1ms \
'postgres://root@35.76.59.55:26257?sslmode=disable'


--locality=region=us-east-1,zone=us-east-1b


ps -ef | grep cockroach | grep -v grep | awk '{print $2}' | xargs sudo kill -9

SET CLUSTER SETTING rocksdb.ingest_backpressure.l0_file_count_threshold = 100;
SET CLUSTER SETTING schemachanger.backfiller.max_buffer_size = '5 GiB';
SET CLUSTER SETTING kv.snapshot_rebalance.max_rate = '128 MiB';
SET CLUSTER SETTING rocksdb.min_wal_sync_interval = '500us';
SET CLUSTER SETTING kv.range_merge.queue.enabled = false;
SET CLUSTER SETTING cluster.organization = 'Ruijie Gong';
SET CLUSTER SETTING enterprise.license = 'crl-0-EITj3rIGGAIiC1J1aWppZSBHb25n';

/root/crdb_new/cockroach start --store=node1 --advertise-addr=13.39.92.165 --listen-addr=13.39.92.165 --insecure --join=13.39.92.165,57.181.129.138,35.76.59.55 --cache=.25 --background



















'''

