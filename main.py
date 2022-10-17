import requests
import ping
import json
domain = input("Domain:")
headers = {
    'accept': 'application/dns-json',
}

params = (
    ('name', domain),
    ('type', 'A'),
)
got_usable_ip = False
IPs = []
while not got_usable_ip:
    try:
        response = requests.get('https://fdp.daycat.space/dns-query', headers=headers, params=params)
    except:
        print("Failed to connect to FDP api. Exiting...")
        exit(0)
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
        else:
            print("IP "+ ip +" not reachable by ICMP")
            IPs.append(ip)
            pass
