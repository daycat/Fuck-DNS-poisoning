from ping3 import ping, verbose_ping
import requests
import json

ssconf_url = 'https://cdn.n101.workers.dev/https://github.com/Incognito-Coder/SurfSocks/blob/main/profiles.json'
ssconfig_dl = requests.get(ssconf_url)
surfsharkconf = json.loads(ssconfig_dl.text)
usable_ip = {}
best_ip = ''
best_ping = 1000
best_location =''
data = json.loads(ssconfig_dl.text)
headers = {
    'accept': 'application/dns-json',
}

for x in data:
    domain = x['server']
    retry = 0
    IPs = []
    while retry <= 9:
        params = (
            ('name', domain),
            ('type', 'A'),
        )
        try:
            response = requests.get('https://fdp.n100.workers.dev/dns-query', headers=headers, params=params)
            data = {}
            data = json.loads(response.text)
            ip = data['Answer'][0]['data']
            if ip in IPs:
                retry -= 1
                pass
            else:
                IPs.append(ip)
                ipping = ping(ip, timeout=1, unit='ms')
                if str(type(ipping)) == "<class 'float'>":
                    print('Found usable ip for ' + x["remarks"] + " " + ip)
                    usable_ip[x["remarks"]] = ip
                    retry = 9
                    if best_ping > ipping:
                        best_ip = ip
                        best_ping = ipping
                        best_location = x["remarks"]
                        print("Found new best location, " + x["remarks"] + ", ip " + ip + ", ping "+str(ipping))
                else:
                    print(ip + " for " + x["remarks"] + " is blocked by the GFW")

        except:
            print('An error was called whilst attempting to resolve a usable IP for ' + x["remarks"])
            retry += 1
        retry += 1
count = 0
print(usable_ip)
for key, value in usable_ip.items():
    print(key+": "+value)

print("Best IP:" + best_ip + "\nPing: "+ str(best_ping) + "\nLocation:" + best_location)

# debug_section
"""
print(ssconfig_dl.text)
"""
