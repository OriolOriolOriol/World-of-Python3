#!/usr/bin/python
import usb.core
import usb.util
import sys,os
import psutil
from hurry.filesize import size

def send():
    pass
def numero_cpu():
    numero=psutil.cpu_count()
    print("Numero di core: " + " " + str(numero))

def utilizzo_network():
    dati=psutil.net_io_counters(pernic=True)
    print("Dati LAN: " + " " + str(dati['Connessione alla rete locale (LAN)* 3']) + " " + str(dati['Connessione alla rete locale (LAN)* 4']))
    print("\n")
    print("Dati del Bluetooth: " + " " + str(dati['Connessione di rete Bluetooth']))
    print("\n")
    print("Dati del Loopback: " + " " + str(dati['Loopback Pseudo-Interface 1']))
    print("\n")
    print("Dati del Wi-fi: " + " " + str(dati['Wi-Fi']))

    #connessioni=psutil.net_connections()
    NIC=psutil.net_if_stats()
    #acronimo di scheda d interfaccia di rete
    #print(NIC)

def utilizzo_cpu():
    print ("---------------------------------------------")
    print ("---------------------------------------------")
    frequenza=psutil.cpu_freq()
    current=frequenza[0]
    minimo=frequenza[1]
    massimo=frequenza[2]
    print("Frequenza corrente della CPU: " + " " + str(current))
    print("Frequenza massima della CPU:"   + " " + str(massimo))
    print("Frequenza minima della CPU:"   + " " + str(minimo))

def sensori():
    if hasattr(psutil, "sensors_temperatures"):
        temperatura = psutil.sensors_temperatures()
        print(temperatura)
    else:
        temperatura={}
    if hasattr(psutil, "sensors_fans"):
        fans = psutil.sensors_fans()
        print(fans)
    else:
        fans = {}
    if hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
        print(battery)
    else:
        battery = None

    if not any((temperatura, fans)):
        print("I can't read any temperature or fans  info")
        return


def processi():
   for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        
       except psutil.NoSuchProcess:
           pass
        
       else:
        print(pinfo)

#Da finire la parte della RAM
def memory_usage():
    memory=psutil.virtual_memory()
    totale=size(memory[0])
    disponibile=size(memory[1])
    percent=memory[2]
    usata=size(memory[3])
    libera=size(memory[4])
    print("Memoria RAM totale: " + " " + str(totale))
    print("Memoria RAM disponibile"  + " " + str(disponibile))
    print("Percentuale d'utilizzo: " + " " + str(percent) + "%")
    print("Memoria RAM in uso: " + " " + str(usata))
    print("Memoria RAM libera: " + " " + str(libera))

    #if(disponibile < usata):
    #    print("Attenzione!!! hai superato la meta' della capienza della RAM")
    #else:
    #   print("Stai usando poca RAM")

def dischi():
    count=0
    dischi=psutil.disk_partitions()
    for ciclo in dischi:
        count=count+1
        print("Numero disco " + " " + str(count) + ":")
        print(ciclo)
        device=ciclo[0]
        try:
            utilizzo=psutil.disk_usage(device)
            totale=size(utilizzo[0])
            usata=size(utilizzo[1])
            libera=size(utilizzo[2])
            percent=utilizzo[3]
            print("Memoria" + " " +  device + " " + "totale:"  + " " + str(totale))
            print("Memoria" + " " +  device + " " + " in uso: " + " " + str(usata))
            print("Memoria" + " " +  device + " " + " libera: " + " " + str(libera))
            print("Percentuale d'utilizzo : " + " " + str(percent) + "%")
            numero_di_operazioni=psutil.disk_io_counters()
            read1=numero_di_operazioni[0]
            write1=numero_di_operazioni[1]
            read_byte1=size(numero_di_operazioni[2])
            write_byte1=size(numero_di_operazioni[3])
            tempo_lettura=numero_di_operazioni[4]
            tempo_scrittura=numero_di_operazioni[5]
            TL=float(tempo_lettura)/ 1000
            TS=float(tempo_scrittura)/ 1000
            tempo_scrittura=numero_di_operazioni[5]
            print("Numero di letture sul disco:" + " " + str(read1) + " " + "Numero di byte letti: " + " " + str(read_byte1))
            print("Numero di scritture sul disco:" + " " + str(write1) + " " + "Numero di byte scritti: " + " " + str(write_byte1))
            print("Tempo totale della lettura: " + " " + str(TL) + " " + "secondi" )
            print("Tempo totale della scrittura: " + " " + str(TS) + " " + "secondi")
            print ("---------------------------------------------")
            print ("---------------------------------------------")
        except WindowsError:
            print ("---------------------------------------------")
            print ("---------------------------------------------")
            pass

def check_usb_device_for_backup():
    count=0
    trovato=False
    dev = usb.core.find(find_all=True)
    for cfg in dev:
        count=count+1
        if(str(cfg.idVendor)=="9527" and str(cfg.idProduct)=="4198"):
            trovato=True
            print("Device trovato :D")
            sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
            sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
        else:
            pass
    print("In totale ci sono: " + " " + str(count) + " " + "devices")
    if trovato==False:
        print("Il dispositivo non e' collegato al pc, per favore collegarlo..\n") 

def run():
    print("0-UTENTE/I DEL COMPUTER")
    utenti=psutil.users()
    print(utenti)
    #nome=utenti[0]
   # tempo_trascorso_dalla_creazione=utenti
    #print(nome)
    #print("\n")
    #print("Numero giorni trascorsi dalla creazione dell'account:" + " " + str(tempo_trascorso_dalla_creazione))
    print ("---------------------------------------------")
    print ("---------------------------------------------")
    print("1-ANALISI DELLA CPU\n")
    #numero_cpu()
    #utilizzo_cpu()
    print ("---------------------------------------------")
    print("2-ANALISI DELLA RAM\n")
    #memory_usage()
    print ("---------------------------------------------")
    print ("---------------------------------------------")
    print("3-ANALISI DEL DISCO FISSO\n")
    #dischi()
    print("4-ANALISI DELLA RETE")
    utilizzo_network()
    print ("---------------------------------------------")
    print ("---------------------------------------------")
    print("5-TEMPERATURE DELL'HARDWARE\n")
    #sensori()
    print ("---------------------------------------------")
    print ("---------------------------------------------")
    print("6-PROCESSI IN SECUZIONE SUL COMPUTER LOCALE\n")
    #processi()


run()