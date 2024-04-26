import subprocess

# 定义开始和结束的仓库数，以及步长
start_warehouses = 2000
end_warehouses = 12000
step = 2000

# 定义命令的不变部分
base_command = "ulimit -n 100000 && ./share/crdb_rls/cockroach workload run tpcc --partitions=5 --ramp=1m --duration=3m --concurrency=4096"
db_urls = "postgres://root@54.64.112.23:26257?sslmode=disable postgres://root@57.181.129.138:26257?sslmode=disable postgres://root@35.76.59.55:26257?sslmode=disable postgres://root@52.88.120.20:26257?sslmode=disable postgres://root@34.210.21.166:26257?sslmode=disable postgres://root@44.224.43.239:26257?sslmode=disable postgres://root@18.168.59.124:26257?sslmode=disable postgres://root@3.8.251.11:26257?sslmode=disable postgres://root@3.9.202.62:26257?sslmode=disable postgres://root@18.162.136.24:26257?sslmode=disable postgres://root@18.162.217.132:26257?sslmode=disable postgres://root@18.167.101.35:26257?sslmode=disable postgres://root@3.208.180.135:26257?sslmode=disable postgres://root@34.206.118.173:26257?sslmode=disable postgres://root@44.214.14.165:26257?sslmode=disable"

for warehouses in range(start_warehouses, end_warehouses + 1, step):
    # 构建完整的命令
    full_command = f"{base_command} --warehouses={warehouses} {db_urls}"
    print(f"Running command for {warehouses} warehouses...")
    print(full_command)
    
    # 执行命令并将输出重定向到文件
    with open(f"/home/ubuntu/share/crdb_new/crdb_scripts/result.txt", "a+") as output_file:
        process = subprocess.run(full_command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

    print(f"Command for {warehouses} warehouses completed. Output saved to output_warehouses_{warehouses}.txt")