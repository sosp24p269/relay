import subprocess
import yaml
import sys
import os
from dotenv import load_dotenv


host = '35.181.176.14'

print("run spanner on " + host)
ssh_command = "sudo docker exec spanner_rls_0 /scripts/run_test.sh " + sys.argv[1]
#ssh_command = "sudo docker exec spanner_rls_0 python3 /scripts/process_logs.py /scripts/log/client.log 60 1 nclient 55 "# + sys.argv[1]
print(ssh_command)
subprocess.call(['ssh', '-o', 'StrictHostKeyChecking=no', host, ssh_command])

