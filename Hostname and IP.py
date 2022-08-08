import socket
print(socket.gethostname())
print (socket.gethostbyname("www.google.com"))
print("\n\n")
hostname=socket.gethostname()

try:
    ipv4 = socket.gethostbyname_ex(hostname)
    print('ipv4 address is ==> '+ str( ipv4 [2][2]))
except:
    print ('err')