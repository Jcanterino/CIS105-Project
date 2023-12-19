import socket
import time

s = socket.socket()
host = "BallsMachine"
port = 8008
s.connect((host, port))
print("Connected ... ")

def sendfile():
    filename = "FileTransfer.txt"
    file = open(filename, 'rb')
    file_data = file.read(1024)
    s.send(file_data)
    print("Data has been transferred succesfully")

while True:
    sendfile()
    time.sleep(1800)