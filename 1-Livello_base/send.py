import smtplib

oggetto="Subject: Urgente da leggere subito\n\n"
contenuto= "connettiti al server"
messaggio = oggetto + contenuto

email = smtplib.SMTP("smtp.gmail.com",587)
email.ehlo()#saluto al server
email.starttls()#mettiamo al sicuro la nostra comunicazione con il server
#RICORDA: SE RINOMINI IL FILE EMAIL DA ERRORE IN QUANTO impedisce a smtplib di importare il modulo e-mail integrato.
email.login("orionperseus999@gmail.com","orologio96")
#dara' errore perche' devi accettare su gmail che l email che usi possa essere usata per questi scopi
email.sendmail("claudio.rimensi.lavoro@gmail.com",messaggio)#invio email ai destinatari
email.quit()