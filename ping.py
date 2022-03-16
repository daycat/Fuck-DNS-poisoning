import platform
import subprocess

def hostping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', '-W 1', host]
    return subprocess.call(command) == 0