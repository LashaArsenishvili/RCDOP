import socket

router_ip = input("Enter the router's IP address: ")

ip_range = router_ip.split('.')[:-1]
ip_range.append('0/24')
ip_range = '.'.join(ip_range)

active_hosts = []
for i in range(1, 255):
    ip = ip_range[:-4] + str(i)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip, 80))
        active_hosts.append(ip)
        s.close()
    except:
        pass

for host in active_hosts:
    print(f"Host: {host}")
    for port in range(1, 1025):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"\tPort {port} is open")
            s.close()
        except:
            pass