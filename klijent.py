import tkinter
from tkinter import *
from tkinter import messagebox
import socket

#POVEIZVANJE

s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))


#FUNKCIJE

def izlaz():
    messagebox.showinfo("Izlaz","Izasli ste iz programa")
    s.send(("1").encode())
    exit(1)

def naruci():
    p1=""
    p2=""
    p3=""
    if (var.get()==1):
        nacinPlacanja="Kes"
    else:
        nacinPlacanja="Kartica"

    if(var1.get()==1):
        vrstaPice="25cm"
    elif(var1.get()==2):
        vrstaPice="32cm"
    else:
        vrstaPice="50cm"

    if (t1.get("1.0","1.1")!=""):
        napomena="Napomena: "+t1.get("1.0",END)
    else:
        napomena=""

    if(CheckVar1.get()):
        p1="Kecap"
    if (CheckVar2.get()):
        p2 = "Majonez"
    if (CheckVar3.get()):
        p3 = "Origano"



    if((entry1.get() and entry2.get() and entry3.get() and entry4.get()!="") and (var.get()!=0) and(var1.get()!=0) ):
        ime = entry1.get()
        s.send((ime).encode())
        vreme = s.recv(1024).decode()
        messagebox.showinfo("Vasa narudzbina", "Ime: "+entry1.get()+"\n"+"Prezime: "+entry2.get()+"\n"+"Adresa: "+entry3.get()+"\n"+"Broj: "+entry4.get()+"\n"\
                            +"Placanje: "+nacinPlacanja+"\n"+"Vrsta pice: "+Lb1.get(ACTIVE)+"\n"+"Velicina Pice: "+vrstaPice+"\n"+"Prilozi: "+p1+" "+p2+" "+p3+"\n" +napomena\
                            +"Vreme do isporuke: "+vreme+"min")


    else:
        messagebox.showinfo("Upozorenje", "Niste sve uneli u polja sa zvezdicom!")

#FUNKCIJE KRAJ


#TKINTER
#LEVO

root=tkinter.Tk()
levo=Frame(root)
levo.grid(row=0,column=1)
tekst=StringVar()
tekst2=StringVar()
tekst3=StringVar()
broj=IntVar()
var = IntVar()

label1=Label(levo,text="Vasi podaci: ",font=("Verdana",12,"bold"))
label1.pack()
label2=Label(levo,text="Ime:* ",font=("Verdana",8))
label2.pack()
entry1=Entry(levo,textvariable=tekst)
entry1.pack()
label3=Label(levo,text="Prezime:* ",font=("Verdana",8))
label3.pack()
entry2=Entry(levo,textvariable=tekst2)
entry2.pack()
label4=Label(levo,text="Adresa:* ",font=("Verdana",8))
label4.pack()
entry3=Entry(levo,textvariable=tekst3)
entry3.pack()
label5=Label(levo,text="Broj:* ",font=("Verdana",8))
label5.pack()
entry4=Entry(levo,textvariable=broj,text="")
entry4.pack()
label7=Label(levo,text="Nacin placanja:* ",font=("Verdana",8))
label7.pack()
r1 = Radiobutton(levo,text="Kes     ", variable=var, value=1)
r1.pack()
r2 = Radiobutton(levo,text="Kartica", variable=var, value=2)
r2.pack()
label6=Label(levo,text="Izaberite vrstu pice:* ",font=("Verdana",8))
label6.pack()
Lb1 = Listbox(levo, selectmode=SINGLE )
Lb1.insert(0, "Margarita")
Lb1.insert(1, "Funghi")
Lb1.insert(2, "Quatro Stagione")
Lb1.insert(3, "Vegeteriana")
Lb1.activate(0)
Lb1.select_set(1,1)
Lb1.pack()

#LEVO KRAJ


#DESNO  POCETAK
desno=Frame(root)
desno.grid(row=0,column=2)
var1=IntVar()
label8=Label(desno,text="Izaberite velicinu pice:* ",font=("Verdana",12))
label8.pack(side=TOP)
r3 = Radiobutton(desno,text="25", variable=var1, value=1)
r3.pack(side=TOP)
r4 = Radiobutton(desno,text="32", variable=var1, value=2)
r4.pack(side=TOP)
r5 = Radiobutton(desno,text="50", variable=var1, value=3)
r5.pack(side=TOP)

label9=Label(desno,text="Izaberite priloge: ",font=("Verdana",12))
label9.pack()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3= IntVar()
c1 = Checkbutton(desno, text = "Kecap", variable = CheckVar1, onvalue = 1, offvalue = 0,)
c1.pack()
c2 = Checkbutton(desno, text = "Majonez", variable = CheckVar2, onvalue = 1, offvalue = 0,)
c2.pack()
c3 = Checkbutton(desno, text = "Origano", variable = CheckVar3, onvalue = 1, offvalue = 0,)
c3.pack()
label10=Label(desno,text="Napomena: ",font=("Verdana",12))
label10.pack()
t1=Text(desno,width=20,height="12")
t1.pack()
#DESNO KRAJ


#DOLE
dole=Frame(root)
dole.grid(row=1,column=2)
b1=Button(dole,text="Naruci!",width=10,command=naruci)
b1.pack(side=TOP)
dolelevo=Frame(root)
dolelevo.grid(row=1,column=1)
b2=Button(dolelevo,text="Izadji",command=izlaz)
b2.pack(side=BOTTOM)
root.mainloop()
