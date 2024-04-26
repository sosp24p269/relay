import subprocess

# 定义开始和结束的仓库数，以及步长
start_concurrency = 2000
end_concurrency = 3000
step = 200

# 定义命令的不变部分
base_command = "./share/crdb_rls/cockroach workload run ycsb --duration=3m"
db_urls = "postgresql://root@35.76.59.55:26257?sslmode=disable"

for concurrency in range(start_concurrency, end_concurrency + 1, step):
    # 构建完整的命令
    full_command = f"{base_command} --concurrency={concurrency} {db_urls}"
    print(f"Running command for {concurrency} warehouses...")
    print(full_command)
    
    # 执行命令并将输出重定向到文件
    with open(f"/home/ubuntu/share/crdb_new/crdb_scripts/result_ycsb.txt", "a+") as output_file:
        process = subprocess.run(full_command, shell=True, stdout=output_file, stderr=subprocess.STDOUT)

    print(f"Command for {concurrency} warehouses completed. Output saved to output_warehouses_{concurrency}.txt")