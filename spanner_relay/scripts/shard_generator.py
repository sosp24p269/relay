import os
import subprocess
from dotenv import load_dotenv

load_dotenv('docker_hosts.env')
hosts = os.getenv('DOCKER_HOSTS').split(',')

total_shards = 2000

print(hosts)
for i in range(total_shards):
    current_host = hosts[i % len(hosts)]  # 获取当前shard的host
    filename = f"shard/shard{i}.config"
    with open(filename, "w+") as f:
        f.write("f 1\n")
        for j in range(3):
            # 使用当前host的IP地址
            f.write(f"replica {current_host}:{15000 + 3 * i + j}\n")


filename = f"shard/shard.tss.config"
with open(filename, "w+") as f:
    f.write("f 1\n")
    for j in range(3):
        # 使用当前host的IP地址
        f.write(f"replica {hosts[0]}:{5100 + 3 * i + j}\n")