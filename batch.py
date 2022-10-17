"""
This is the batch version for FDP to get a range of IPs that are usable from a domain
"""
import requests
import ping
import json
domain = input("Domain:")
search_times = int(input("Depth:"))
headers = {
    'accept': 'application/dns-json',
}

params = (
    ('name', domain),
    ('type', 'A'),
)
got_usable_ip = False
IPs = []
Usable_IPs = []
for x in range (search_times):
    try:
        response = requests.get('https://fdp.daycat.space/dns-query', headers=headers, params=params)
    except:
        print("Failed to connect to FDP api. Exiting...")
        exit(0)
    data = {}
    data = json.loads(response.text)
    ip = data['Answer'][0]['data']
    if ip not in IPs:
        print("new IP " + ip + " from fdp")
        if ping.hostping(ip):
            got_usable_ip = True
            IPs.append(ip)
            print("Found Usable IP: " + ip)
            if ip not in Usable_IPs:
                Usable_IPs.append(ip)
        else:
            print("IP " + ip + " not reachable by ICMP")
            IPs.append(ip)
            pass
    else:
        pass
c=0
for y in Usable_IPs:
    print(Usable_IPs[c])
    c+=1
