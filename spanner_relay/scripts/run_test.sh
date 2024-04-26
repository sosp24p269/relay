#!/bin/bash

trap '{
  echo "\nKilling all clients.. Please wait..";
  for host in ${clients[@]}
  do
    ssh $host "killall -9 $client";
    ssh $host "killall -9 $client";
  done

  echo "\nKilling all replics.. Please wait..";
  for host in ${servers[@]}
  do
    ssh $host "killall -9 server";
  done
}' INT


version="$1"

# Paths to source code and logfiles.
if [ "$version" = "rls" ]; then
    srcdir="/spanner_rls/tapir-master"
elif [ "$version" = "spanner" ]; then
    srcdir="/spanner/tapir-master"
elif [ "$version" = "rls2" ]; then
    srcdir="/spanner_rls2/tapir-master"
elif [ "$version" = "spanner2" ]; then
    srcdir="/spanner2/tapir-master"
fi

# 设置公共目录
dir="/scripts"
logdir="/scripts/log"

#python3 $dir/shard_generator.py $logdir/client.log $rtime $j

client="retwisClient"    # Which client (benchClient, retwisClient, etc)
store="strongstore"      # Which store (strongstore, weakstore, tapirstore)
mode="span-lock"            # Mode for storage system.

source $dir/config.env
source $dir/docker_hosts.env
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
#5ms 100ms
# Print out configuration being used.
echo "Configuration:"
echo "Shards: $nshard"
echo "Clients per host: $nclient"
echo "Threads per client: $nthread"
echo "Keys: $nkeys"
echo "Transaction Length: $tlen"
echo "Write Percentage: $wper"
echo "Error: $err"
echo "Skew: $skew"
echo "Zipf alpha: $zalpha"
echo "Skew: $skew"
echo "Client: $client"
echo "Store: $store"
echo "Mode: $mode"


# Generate keys to be used in the experiment.
#echo "Generating random keys.."
#python3 key_generator.py $nkeys > $dir/keys
#for ((i=0; i<10; i++))
#do
#python3 $dir/shard_generator.py
#done

#for inper in 0.99 0.98 0.97 0.95 0.92 0.9 0.85 0.8 0.75 0.7
#for zalpha in 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1
#for nclient in 1 2 3 5 8 10 13 15 18 20 25 30 35 40 45 50 55 60 65


for j in 1
do
for nclient in 15 25 35 45 55 65
do

echo "clean"
for host in "${hosts[@]}"; 
do
{
ssh -o StrictHostKeyChecking=no $host "ps -ef | grep tapir | grep -v grep | awk '{print \$2}' | xargs kill -9"
}&
done
wait

echo "$j nclient $nclient $version "
# Start all replicas and timestamp servers
echo "Starting TimeStampServer replicas.."
$dir/start_replica.sh tss $dir/shard/shard.tss.config \
  "$srcdir/timeserver/timeserver" $logdir

#for ((i=0; i<$nshard; i++)) need to --
for ((i=0; i<$nshard; i++))
do
{
  echo "Starting shard$i replicas.."
  $dir/start_replica.sh shard$i $dir/shard/shard$i.config \
    "$srcdir/store/$store/server -m $mode -f $dir/keys -k $nkeys -e $err -s $skew" $logdir

}&
done
wait
sleep 2


# Run the clients
count=0

for region in "${!hosts[@]}"; do
{
  echo "Running the client$region(s)"
  host=${hosts[$region]}
  ssh -o StrictHostKeyChecking=no $host "$dir/start_client.sh \"$srcdir/store/benchmark/$client \
  -c $dir/shard/shard -N $nshard -f $dir/keys \
  -d $rtime -l $tlen -i $inper -w $wper -k $nkeys -m $mode -e $err -s $skew -z $zalpha -n $nregion -M $region\" \
  $count $nclient $logdir $region"
}&
done
wait


for host in "${hosts[@]}"; do
{
  echo "wait the client$host(s)"
  timeout 90 ssh -o StrictHostKeyChecking=no $host "$dir/wait_client.sh $client"
}&

done
wait




# Kill all replicas
echo "Cleaning up"

$dir/stop_replica.sh $dir/shard/shard.tss.config > /dev/null 2>&1

for ((i=0; i<$nshard; i++))
do
{
  $dir/stop_replica.sh $dir/shard/shard$i.config > /dev/null 2>&1
}&
done

wait


# Process logs
count=0 
for host in "${hosts[@]}"; 
do
{
echo "Processing logs"
ssh -o StrictHostKeyChecking=no $host "cat $logdir/client$count.*.log | sort -g -k 3 > $logdir/client$count.log"
ssh -o StrictHostKeyChecking=no $host "rm -f $logdir/client$count.*.log"
}&
count=$((count + 1))
done

# 等待所有后台进程完成
wait
echo "All logs have been processed."

sleep 30

echo "Processing total logs"
cat $logdir/client*.log | sort -g -k 3 > $logdir/client.log

python3 $dir/process_logs.py $logdir/client.log $rtime $j nclient $nclient $version 

sleep 5


done
done

: <<'END'



for j in 1 
do
for zalpha in 0.5 0.5 0.6 0.7 0.8 0.9 1
do

echo "clean"
for host in "${hosts[@]}"; 
do
{
ssh -o StrictHostKeyChecking=no $host "ps -ef | grep tapir | grep -v grep | awk '{print \$2}' | xargs kill -9"
}&
done
wait

echo "$j zalpha $zalpha $version "
# Start all replicas and timestamp servers
echo "Starting TimeStampServer replicas.."
$dir/start_replica.sh tss $dir/shard/shard.tss.config \
  "$srcdir/timeserver/timeserver" $logdir

#for ((i=0; i<$nshard; i++)) need to --
for ((i=0; i<$nshard; i++))
do
{
  echo "Starting shard$i replicas.."
  $dir/start_replica.sh shard$i $dir/shard/shard$i.config \
    "$srcdir/store/$store/server -m $mode -f $dir/keys -k $nkeys -e $err -s $skew" $logdir

}&
done
wait
sleep 2


# Run the clients
count=0

for region in "${!hosts[@]}"; do
{
  echo "Running the client$region(s)"
  host=${hosts[$region]}
  ssh -o StrictHostKeyChecking=no $host "$dir/start_client.sh \"$srcdir/store/benchmark/$client \
  -c $dir/shard/shard -N $nshard -f $dir/keys \
  -d $rtime -l $tlen -i $inper -w $wper -k $nkeys -m $mode -e $err -s $skew -z $zalpha -n $nregion -M $region\" \
  $count $nclient $logdir $region"
}&
done
wait


for host in "${hosts[@]}"; do
{
  echo "wait the client$host(s)"
  timeout 90 ssh -o StrictHostKeyChecking=no $host "$dir/wait_client.sh $client"
}&

done
wait




# Kill all replicas
echo "Cleaning up"

$dir/stop_replica.sh $dir/shard/shard.tss.config > /dev/null 2>&1

for ((i=0; i<$nshard; i++))
do
{
  $dir/stop_replica.sh $dir/shard/shard$i.config > /dev/null 2>&1
}&
done

wait


# Process logs
count=0 
for host in "${hosts[@]}"; 
do
{
echo "Processing logs"
ssh -o StrictHostKeyChecking=no $host "cat $logdir/client$count.*.log | sort -g -k 3 > $logdir/client$count.log"
ssh -o StrictHostKeyChecking=no $host "rm -f $logdir/client$count.*.log"
}&
count=$((count + 1))
done

# 等待所有后台进程完成
wait
echo "All logs have been processed."

sleep 30

echo "Processing total logs"
cat $logdir/client*.log | sort -g -k 3 > $logdir/client.log

python3 $dir/process_logs.py $logdir/client.log $rtime $j zalpha $zalpha $version 

sleep 5


done
done
zalpha=0.75 




for j in 1 
do
for inper in 100 100 95 90 85 80 75
do

echo "clean"
for host in "${hosts[@]}"; 
do
{
ssh -o StrictHostKeyChecking=no $host "ps -ef | grep tapir | grep -v grep | awk '{print \$2}' | xargs kill -9"
}&
done
wait

echo "$j inper $inper $version"
# Start all replicas and timestamp servers
echo "Starting TimeStampServer replicas.."
$dir/start_replica.sh tss $dir/shard/shard.tss.config \
  "$srcdir/timeserver/timeserver" $logdir

#for ((i=0; i<$nshard; i++)) need to --
for ((i=0; i<$nshard; i++))
do
{
  echo "Starting shard$i replicas.."
  $dir/start_replica.sh shard$i $dir/shard/shard$i.config \
    "$srcdir/store/$store/server -m $mode -f $dir/keys -k $nkeys -e $err -s $skew" $logdir

}&
done
wait
sleep 2


# Run the clients
count=0

for region in "${!hosts[@]}"; do
{
  echo "Running the client$region(s)"
  host=${hosts[$region]}
  ssh -o StrictHostKeyChecking=no $host "$dir/start_client.sh \"$srcdir/store/benchmark/$client \
  -c $dir/shard/shard -N $nshard -f $dir/keys \
  -d $rtime -l $tlen -i $inper -w $wper -k $nkeys -m $mode -e $err -s $skew -z $zalpha -n $nregion -M $region\" \
  $count $nclient $logdir $region"
}&
done
wait


for host in "${hosts[@]}"; do
{
  echo "wait the client$host(s)"
  timeout 90 ssh -o StrictHostKeyChecking=no $host "$dir/wait_client.sh $client"
}&

done
wait




# Kill all replicas
echo "Cleaning up"

$dir/stop_replica.sh $dir/shard/shard.tss.config > /dev/null 2>&1

for ((i=0; i<$nshard; i++))
do
{
  $dir/stop_replica.sh $dir/shard/shard$i.config > /dev/null 2>&1
}&
done

wait


# Process logs
count=0 
for host in "${hosts[@]}"; 
do
{
echo "Processing logs"
ssh -o StrictHostKeyChecking=no $host "cat $logdir/client$count.*.log | sort -g -k 3 > $logdir/client$count.log"
ssh -o StrictHostKeyChecking=no $host "rm -f $logdir/client$count.*.log"
}&
count=$((count + 1))
done

# 等待所有后台进程完成
wait
echo "All logs have been processed."

sleep 30

echo "Processing total logs"
cat $logdir/client*.log | sort -g -k 3 > $logdir/client.log

python3 $dir/process_logs.py $logdir/client.log $rtime $j inper $inper $version

sleep 5


done
done
inper=90

END