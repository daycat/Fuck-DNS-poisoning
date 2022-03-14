# FDP

Fuck-DNS-Poisoning is a simple python script that takes in a domain and outputs a useable (pingable) ip.

## Usage:

```shell
git clone https://github.com/daycat/fuck_DNS_poisoning.git
cd fuck_DNS_poisoning
python3 main.py
```
## Background:
In some areas of the world, to control and censor the internet, there are often measures such as restricticting access to websites put in place by the local government. This is especially true in countries such as China - with that being the main reason of why I created this tool.

There are numerous different ways that the government can censor the internet. Aside from blocking IP addresses, another way that is often used in censoring IP addresses is DNS poisoning.

DNS poisoning is a technique in which the censor exploits the domain resolution cycle as a mean to censor specific web pages, especially if served through a CDN handling normal, non-blocked traffic (i.e Cloudflare. Note that this purpose is largely superseded by SNI blocking.)

This is an example of DNS poisoning in action. Here, I have the domain name for the New York surfshark server:

```shell
us-nyc.prod.surfshark.com
```
Now, let's try ping this server from China:

```shell
alanzhou@Alans-MacBook ~ % ping us-nyc.prod.surfshark.com
PING us-nyc.prod.surfshark.com (199.16.158.9): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
Request timeout for icmp_seq 2
Request timeout for icmp_seq 3
Request timeout for icmp_seq 4
Request timeout for icmp_seq 5
Request timeout for icmp_seq 6
Request timeout for icmp_seq 7
^C
--- us-nyc.prod.surfshark.com ping statistics ---
9 packets transmitted, 0 packets received, 100.0% packet loss
alanzhou@Alans-MacBook ~ % 
```

hmmm... Maybe this IP address is blocked?... Wait a second, isn't this a IP from Twitter?

```shell
 ip: "199.16.158.9"
 city: "Singapore"
 region: "Singapore"
 country: "SG"
 loc: "1.2897,103.8501"
 org: "AS13414 Twitter Inc."
 postal: "018989"
 timezone: "Asia/Singapore"
 asn: Object
```
ip data from ipinfo.io. I am not affiliated with them in any ways.

That *surely* can't be right? It's supposed to be in the United States!

Ladies and gentlemen, may I present to you, DNS poisoning. 

## So, What the fuck does this script do?

Well, this is simple. Because the censor attacks the address resolvation through a mixture of DNS poisoning and DNS injection, therefore, let's mitigate that with something else.

This script is very simple - in fact WAY shorter than this stupidly long documentation. 

1. It resolves the address. However, it does this by using DNS over HTTPS: This means that the censor cannot intercept and modify the answer from the DNS server. In fact, they won't even know that we are resolving a domain name - they can only see that we have connected in HTTPS to the API (which, is fully compatible with the official cloudflare API)
2. It checks each of the address resolved to see if your computer can reach it from your network. This is especially useful in China, for example, when you need to find a working IP address for surfshark VPN (for example). This gives you a ready-to-use IP address that you can use straight away.

## Proof that this shit works

So, now we know that this is very simple, and nothing really can go wrong, let's check the New York surfshark domain again, but using this script?

```shell
Domain:us-nyc.prod.surfshark.com
new IP 84.17.35.111 from fdp
PING 84.17.35.111 (84.17.35.111): 56 data bytes
64 bytes from 84.17.35.111: icmp_seq=0 ttl=51 time=228.902 ms

--- 84.17.35.111 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 228.902/228.902/228.902/0.000 ms
Found Usable IP: 84.17.35.111

Process finished with exit code 0
```
Neat! Lets ping this IP:

```shell
alanzhou@Alans-MacBook ~ % ping 84.17.35.111
PING 84.17.35.111 (84.17.35.111): 56 data bytes
64 bytes from 84.17.35.111: icmp_seq=0 ttl=51 time=228.079 ms
64 bytes from 84.17.35.111: icmp_seq=1 ttl=51 time=227.642 ms
64 bytes from 84.17.35.111: icmp_seq=2 ttl=51 time=229.576 ms
64 bytes from 84.17.35.111: icmp_seq=3 ttl=51 time=228.089 ms
64 bytes from 84.17.35.111: icmp_seq=4 ttl=51 time=228.428 ms
64 bytes from 84.17.35.111: icmp_seq=5 ttl=51 time=228.131 ms
64 bytes from 84.17.35.111: icmp_seq=6 ttl=51 time=227.764 ms
64 bytes from 84.17.35.111: icmp_seq=7 ttl=51 time=228.764 ms
^C
--- 84.17.35.111 ping statistics ---
8 packets transmitted, 8 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 227.642/228.309/229.576/0.581 ms
alanzhou@Alans-MacBook ~ % 
```
Sweet! It's working!

Lets see what ipinfo tells us:
```sh
 ip: "84.17.35.111"
 hostname: "unn-84-17-35-111.cdn77.com"
 city: "New York City"
 region: "New York"
 country: "US"
 loc: "40.7086,-74.0087"
 org: "AS60068 Datacamp Limited"
 postal: "10045"
 timezone: "America/New_York"
 asn: Object
```
Voila! Its working! Time to catch the next netflix show!
