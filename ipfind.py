import socket
target_site=(input("Please Enter Sites Link Here:"))
ip_address=socket.gethostbyname(target_site)
print(f"{target_site} İp_is:{ip_address}")
      