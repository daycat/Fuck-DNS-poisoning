import requests
import ping
import json
ssconf_url = 'https://cdn.n101.workers.dev/https://github.com/Incognito-Coder/SurfSocks/blob/main/profiles.json'
ssconfig_dl = requests.get(ssconf_url)
surfsharkconf = json.loads(ssconfig_dl.text)
usable_ip = {}
count=0
for a in surfsharkconf:
    print(surfsharkconf[count]['server'])
    headers = {
        'accept': 'application/dns-json',
    }


    params = (
        ('name', surfsharkconf[count]['server']),
        ('type', 'A'),
    )
    got_usable_ip = False
    IPs = []
    retry_count = 0
    while not got_usable_ip and retry_count<5:
        try:
            current = surfsharkconf[count]['remarks']
            usable_ip[current] = ''
            response = requests.get('https://fdp.daycat.space/dns-query', headers=headers, params=params)
            print(response.text)
            data = {}
            data = json.loads(response.text)
            ip = data['Answer'][0]['data']
            if ip in IPs:
                pass
            else:
                print("new IP " + ip + " from fdp")
                if ping.hostping(ip):
                    got_usable_ip = True
                    print("Found Usable IP: "+ip)
                    usable_ip[surfsharkconf[count]['remarks']] = ip
                    retry_count=0
                else:
                    print("IP "+ ip +" not reachable by ICMP")
                    IPs.append(ip)
                    retry_count+=1
                    pass
        except:
            got_usable_ip = True
            pass
    count += 1
print(usable_ip)
