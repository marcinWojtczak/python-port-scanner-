import socket
import sys 

target = ""
if len(sys.argv) > 1:
	target =  sys.argv[1]
else:
	target = "127.0.0.1"


print(f"Target:{target}")
ports = {
  21:"FTP",
  22:"SSH", 
  8080:"HTTP-Proxy", 
  80:"HTTP", 
  53:"DNS", 
  443:"HTTPS", 
  3389:"RDP", 
  3306:"MySQL",  
  5432: "PostgreSQL"
}

print(f"Scanning: {target}")
print("-" * 30)


for port, service in ports.items():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)

	result = sock.connect_ex((target, port))

	if result == 0:
		print(f"Port {port} ({service}) - Open")

	sock.close()

print("-" * 30)
print("Scanning finished")
