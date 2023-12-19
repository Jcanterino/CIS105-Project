import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 8008
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for any incoming connections ...")
conn, addr = s.accept()
print(addr, "Has connected to the server.")

def receivefile():
    filename = "FileTransferReceive"
    file = open(filename, 'wb')
    file_data = conn.recv(1024)
    file.write(file_data)
    file.close()
    print("File has been received succesfully")

while True:
    receivefile()
    time.sleep(1800)


