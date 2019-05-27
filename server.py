import tkinter
from tkinter import *
import socket
import threading
import time
import random


#POVEIZVANJE

s=socket.socket()
host=socket.gethostname()
port=9999
s.bind((host,port))
s.listen(5)

listavremena=[0]

#FUNKCIJE

def isporucena():



    while True:

        vremez=listavremena[1]
        time.sleep(vremez)
        isporuceneNarudzbine.insert(END,"Isporucena pica za: "+klijent+"\n")
        primljenePorudzbine.delete('1.0', '3.0')
        listavremena.pop(1)
        break

def niti():
    konekcija, adresa = s.accept()

    while True:
        print("Konektovano")
        global klijent
        klijent=konekcija.recv(1024).decode()
        if klijent=='1':
            konekcija.close()
            break
        else:

            vreme = random.randint(10, 51)
            listavremena.append(vreme)
            vreme = str(vreme)
            konekcija.send((vreme).encode())
            primljenePorudzbine.insert(END,"Porudzbina za: "+klijent+"\n"+"Preostalo vreme: "+vreme+" minuta"+"\n")

            threading.Thread(target=isporucena).start()
            for i in listavremena:
                print(i)


#TKINTER DEO
root=tkinter.Tk()
levo=Frame(root)
levo.grid(row=0,column=0)
l1=Label(levo,text="Pristigle narudzbine")
l1.pack()
primljenePorudzbine=Text(levo,width=30,height=20)
primljenePorudzbine.pack()

desno=Frame(root)
desno.grid(row=0,column=1)
l2=Label(desno,text="Isporucene narudzbine")
l2.pack(side=TOP)
isporuceneNarudzbine=Text(desno,width=30,height=20)
isporuceneNarudzbine.pack(side=RIGHT)
threading.Thread(target=niti).start()

root.mainloop()
