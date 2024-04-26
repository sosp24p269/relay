
#echo $test
source /scripts/config.env
source /scripts/docker_hosts.env
OLD_IFS="$IFS"

# 设置 IFS 为逗号，用于分割字符串
IFS=','

# 读取 DB_HOSTS 并将其分割为数组
read -ra hosts <<< "$DOCKER_HOSTS"

# 恢复原始的 IFS
IFS="$OLD_IFS"

# 遍历 IP 地址数组并打印每个地址
for host in "${hosts[@]}"; do
    echo "Database host: $host"
done
for host in "${hosts[@]}";
do
    echo "Stop the progress in client $i(s)"

    cmd="ps -ef | grep tapir | grep -v grep | awk '{print \$2}' | xargs kill -9"
    echo $cmd
    ssh $host "ps -ef | grep tapir | grep -v grep | awk '{print \$2}' | xargs kill -9"
    ssh $host "ps -ef | grep origin | grep -v grep | awk '{print \$2}' | xargs kill -9"
    ssh $host "ps -ef | grep run | grep -v grep | awk '{print \$2}' | xargs kill -9"
done