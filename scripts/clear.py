import subprocess
import getpass

# Your commands
commands = [
    "kubectl delete deployment pgpool",
    "kubectl delete service prometheus-server-nodeport",
    "kubectl delete spok spok-cluster",
    #"kubectl delete sts pgset-master",
    #"kubectl delete sts pgset-replica",
    "kubectl delete service pgsql-headless",
    "kubectl delete pvc pgdata-pgset-master-0 pgdata-pgset-replica-0 pgdata-pgset-replica-1 pgdata-pgset-replica-2",
    "kubectl delete pv pv-pg-0 pv-pg-1 pv-pg-2 pv-pg-3",
    "echo {} | sudo -S rm -rf /data/pv-pg*".format(getpass.getpass(prompt='Enter your local sudo password: ')),
]

# Remote ssh commands
ssh_commands = [
    "ssh kw-node1 'echo {} | sudo -S rm -rf /data/pv-pg*'".format(getpass.getpass(prompt='Enter your remote sudo password: '))
]

# Run your commands
for cmd in commands:
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error executing command: {cmd}\nError: {stderr.decode()}")
    else:
        print(f"Executed command: {cmd}\nOutput: {stdout.decode()}")

# Run your ssh commands
for cmd in ssh_commands:
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error executing command: {cmd}\nError: {stderr.decode()}")
    else:
        print(f"Executed command: {cmd}\nOutput: {stdout.decode()}")
