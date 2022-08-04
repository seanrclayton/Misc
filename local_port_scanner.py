import requests
import socket


for ip in list(range(1,255+1)):
    ips_with_open_http = []
    target = f"192.168.0.{ip}"
    port = 80

    print
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # returns an error indicator
    result = s.connect_ex((target, port))
    if result == 0:
        ips_with_open_http.append(target)
        print(f"Port {port} is open on {target} ")
        print
    s.close()

for address in ips_with_open_http:
    print(f"http://{address}")
