from ping3 import ping
from concurrent.futures import ThreadPoolExecutor
import threading
import requests
import json

ssconf_url = 'https://cdn.n101.workers.dev/https://github.com/Incognito-Coder/SurfSocks/blob/main/profiles.json'
ssconfig_dl = requests.get(ssconf_url)
surfsharkconf = json.loads(ssconfig_dl.text)
usable_ip = {}
best_ip = ''
best_ping = 1000
best_location = ''
data = json.loads(ssconfig_dl.text)
headers = {
    'accept': 'application/dns-json',
}
thread_status = []
count = 0
for w in data:
    thread_status.append(0)
    count += 1

print(thread_status)
IPs = []


def check_IP(count):
    # print(count)
    tls = threading.local()
    tls.params = (
        ('name', data[count]["server"]),
        ('type', 'A'),
    )
    try:
        tls.response = requests.get('https://fdp.daycat.space/dns-query', headers=headers, params=tls.params)
        tls.response = json.loads(tls.response.text)
        tls.currentip = tls.response['Answer'][0]['data']
        if tls.currentip in IPs:
            thread_status[count]-=1
        else:
            IPs.append(tls.currentip)
            tls.ipping = ping(tls.currentip, timeout=1, unit='ms')
            if str(type(tls.ipping)) == "<class 'float'>":
                print('Found usable ip for ' + data[count]["remarks"] + " " + tls.currentip)
                usable_ip[data[count]["remarks"]] = tls.currentip
                thread_status[count] = 5
            else:
                print(tls.currentip + " for " + data[count]["remarks"] + " is blocked by the GFW")
    except Exception as e:
        print("An Error occured attempting to process "+data[count]["remarks"])
        print(str(e))
        thread_status[count] = 5


# Main thread
with ThreadPoolExecutor(max_workers=20) as ex:
    while sum(thread_status) / len(thread_status) < 5:
        min_value = min(thread_status)
        min_index = thread_status.index(min_value)
        thread_status[min_index] += 1
        ex.submit(check_IP, min_index)

print(thread_status)
for key, value in usable_ip.items():
    print(key+": " +value)
