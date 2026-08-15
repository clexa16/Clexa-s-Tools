import socket
target=input("Pleae enter target site:")
port=int(input("Please Enter Port Number:"))
soket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conclusion=soket.connect_ex((target, port))
if conclusion == 0:
    print(f"[+] Success! {target} on port is open!")
else:
    print(f"[+] Sorry! {target} on port is closed or blocked")
soket.close()