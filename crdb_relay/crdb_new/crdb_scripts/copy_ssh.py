import paramiko

hosts = [] 
with open (HOSTS_FILE, 'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    hosts = data['hosts']

username = "ubuntu"

# 用于存储每个实例的公钥
public_keys = {}

# 私钥路径
private_key_path = r"C:\Users\17923\.ssh\id_rsa"

# 创建SSH客户端配置
ssh_config = paramiko.SSHClient()
ssh_config.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到每个实例并获取公钥
for host in hosts:
    print(f"Connecting to {host}...")

    try:
        # 使用私钥进行认证
        key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_config.connect(host, username=username, pkey=key)
        
        # 获取公钥
        stdin, stdout, stderr = ssh_config.exec_command('cat ~/.ssh/id_rsa.pub')
        public_key = stdout.read().decode().strip()
        public_keys[host] = public_key
        print(f"Public key for {host} retrieved successfully.")
        
    finally:
        ssh_config.close()

# 将每个实例的公钥添加到其他实例的authorized_keys中
for host in hosts:
    
    ssh_config.connect(host, username=username, pkey=key)
    
    for ip, public_key in public_keys.items():
        if ip != host:
            # 检查authorized_keys是否已包含该公钥
            stdin, stdout, stderr = ssh_config.exec_command(f'grep "{public_key}" ~/.ssh/authorized_keys')
            if not stdout.read().decode().strip():
                # 添加公钥到authorized_keys
                command = f'echo "{public_key}" >> ~/.ssh/authorized_keys'
                stdin, stdout, stderr = ssh_config.exec_command(command)
                print(f"Public key from {ip} added to {host}.")
            else:
                print(f"Public key from {ip} already exists in {host}.")
    
    ssh_config.close()

print("All public keys have been exchanged successfully.")