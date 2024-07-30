# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:47:09 2023

@author: tharun
"""
import os
import csv
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def checker():
    global idno,f,g,er,item,Name,IDNO
    er=0
    f,g=0,0
    with open("names.csv",'r') as file1:
        f1=csv.reader(file1)
        for j in f1:
            if j[0]==name1.get():
                f+=1
                Name=j[0]
                if j[1]==idno.get().strip():
                    g+=1
                    IDNO=j[1]
                    mat()
        if g==0 and f==0:
            messagebox.showerror("login error","no person found")
        elif f==1 and g==0:
            messagebox.showerror("login error","wrong id number")
    file1.close()
def checker1():
    global idno,f,g,er,item,Name,IDNO
    er=0
    f,g=0,0
    with open("names.csv",'r') as file1:
        f1=csv.reader(file1)
        for j in f1:
            if j[0]==name1.get():
                f+=1
                Name=j[0]
                if j[1]==idno.get().strip():
                    g+=1
                    IDNO=j[1]
                    place()
        if g==0 and f==0:
            messagebox.showerror("login error","no person found")
        elif f==1 and g==0:
            messagebox.showerror("login error","wrong id number")
    file1.close()
def check():
    global qwert,count,location,project,obj
    qwert=0
    for r in lis:
        for t in r:
            if maty.get()==t[1]:
                obj=t[1]
                count=t[2]
                location=t[3]
                project=t[4]
                qwert=1
                w1.destroy()
                loop()
                break
    if qwert==0:
        messagebox.showerror("invalid input","no item found")
        A=0
        w1.destroy()
        f,g=1,1
        mat()
def place():
        global w4
        global number,ent,lop2,position
        number=0
        lop=[]
        def add():
            def pri():
                    lop2=[]
                    i=0
                    while i<len(lop):
                            lop1=[]
                            for entry in range(5):
                                lop1.append(lop[i].get())
                                i+=1
                            lop2.append(lop1)
                    try:
                        for ik in lop2:
                            quink=int(ik[2])
                            if ik[0]=="" or ik[1]=="" or ik[3]=="" or ik[4]=="" or ik[0]==" " or ik[1]==" " or ik[3]==" " or ik[4]==" ":
                                raise ValueError
                        countcheck=0
                        for variable in  lis:
                            for variable1 in variable:
                                for variable2 in lop2:
                                    if variable1[1]==variable2[1]:
                                        countcheck+=1
                                        variable1[2]=int(variable1[2])+int(variable2[2])
                                        lop2.remove(variable2)
                                if len(variable1)==0:
                                    variable.remove(variable1)
                        for var in lop2:
                            LIS=[]
                            LIS.append(var)
                            lis.append(LIS)
                        for i in lis:
                            if len(i)==0:
                                lis.remove(i)
                        with open(r"ont.csv", 'w') as file:
                            writer = csv.writer(file)
                            for i in lis:
                                for j in i:
                                    writer.writerow(j)
                            file.close()
                        w5.destroy()
                    except:
                        messagebox.showerror("invalid input","enter the inputs correctly")
            try:
                u=int(noofitems.get())
                w5=Tk()
                Label(w5,text="status").grid(row=0,column=0)
                Label(w5,text="name").grid(row=0,column=1)
                Label(w5,text="count").grid(row=0,column=2)
                Label(w5,text="location").grid(row=0,column=3)
                Label(w5,text="project").grid(row=0,column=4)
                for i in range(int(noofitems.get())):
                    number=i
                    for j in range(5):
                        ent=Entry(w5)
                        ent.grid(row=i+1, column=j,padx=15,pady=0)
                        lop.append(ent)
                MY_BUTTON=Button(w5,text="Save Changes",font="Arial 10 bold",command=pri)
                MY_BUTTON.grid(row=(number+2),column=0,padx=20,pady=5)
            except:
                messagebox.showerror("invalid input","enter the input correctly")
        w4=Tk()
        w4.title("count of new and old items")
        w4.state("zoomed")
        lab1=Label(w4,text="count of items:",font="Arial 17 bold")
        lab1.place(relx=0.5,rely=0.5,anchor=CENTER)
        noofitems=Entry(w4)
        noofitems.pack()
        noofitems.place(relx=0.5,rely=0.55,anchor=CENTER)
        button=Button(w4,text="OK",font="Arial 10 bold",command=add)
        button.place(relx=0.45,rely=0.6,anchor=CENTER)
        button1=Button(w4,text="Exit",font="Arial 10 bold",command=exit2)
        button1.place(relx=0.55,rely=0.6,anchor=CENTER)
def function():
    global flag,flag1,name
    flag,flag1=0,0
    itemcount,m=0,0
    for r in lis:
        for t in r:
            if t[0]=='Consumable' or t[0]=="consumable" or t[0]=="CONSUMABLE":
                if obj==t[1]:
                    if int(x.get())<=int(t[2]):
                        lis1=[]
                        y=int(t[2])
                        t[2]=int(t[2])-int(x.get())
                        zcount=t[2]
                        flag=1
                        dt=datetime.datetime.now()
                        dt=str(dt)
                        d,t=dt.split()
                        lis1.append(Name)
                        lis1.append(IDNO)
                        lis1.append(obj)
                        lis1.append(y)
                        lis1.append(x.get())
                        lis1.append(zcount)
                        lis1.append(d)
                        lis1.append(t)
                    if int(x.get())>0:
                            with open('history.csv',"a") as file2:
                                writer=csv.writer(file2) 
                                writer.writerow(lis1)
                                flag=1
                                file2.close()
                                break
                    elif int(x.get())<0:
                            m=1
                            flag=1
                            break
                    else:
                            itemcount=1
                            flag=1
                            break
            if flag==1:
                    flag1=1
                    break
        if flag1==1:
                break
            
    if int(x.get())>0:
        with open(r'ont.csv', 'w') as file:
            writer = csv.writer(file)
            for i in lis:
                for j in i:
                    writer.writerow(j)
            file.close()
    w2.destroy()
    mat()
def loop():
    global itemcount,x,m,w2
    w2=Tk()
    w2.title("material details") 
    w2.state("zoomed")
    l3=Label(w2,text="material details")
    l3.place(relx=0.5,rely=0.45,anchor=CENTER)
    txt = Text(w2, height=3, width=30)
    l4=Label(w2,text="enter the count of items to be taken")
    l4.place(relx=0.5,rely=0.5,anchor=CENTER)
    txt.pack()
    txt.place(relx=0.5,rely=0.45,anchor=CENTER)
    txt.insert(INSERT,"item count:"+str(count)+"\n"+"material location:"+location+"\n"+"project:"+str(project))
    x=Entry(w2)
    x.pack()
    x.place(relx=0.5,rely=0.55,anchor=CENTER)
    b3=Button(w2,text="Finish",font="Arial 10 bold",command=function)
    b3.place(relx=0.5,rely=0.6,anchor=CENTER)
def mat():
        global w1,maty
        w1=Tk()
        w1.title("MATERIAL DETAILS")
        w1.state("zoomed")
        l=Label(w1,text="ITEM NAME",font="Arial 17 bold")
        l.place(relx=0.5,rely=0.3,anchor=CENTER)
        maty=ttk.Combobox(w1,values=[*combolis])
        maty.pack()
        maty.place(relx=0.5,rely=0.35,anchor=CENTER)
        b1=Button(w1,text="ENTER",font="Arial 10 bold",command=check)
        b1.place(relx=0.45,rely=0.4,anchor=CENTER)
        b2=Button(w1,text="EXIT",font="Arial 10 bold",command=exit1)
        b2.place(relx=0.55,rely=0.4,anchor=CENTER)
        w1.mainloop()
        A=1
        w1.destroy()
def entry():
    global lis,idno,w,name1,combolis
    lis=[]
    combolis=[]
    with open('ont.csv','r') as q:
        q1=csv.reader(q)
        for line in q1:
            lis1=[]
            for i in line:
                lis1.append(line)
                combolis.append(line[1])
                break
            lis.append(lis1)
        q.close()
    for i in combolis:
        if len(i)==0:
            combolis.remove(i)
    for i in lis:
        if len(i)==0:
            lis.remove(i)
    w=Tk()
    w.title("login details")
    w.state("zoomed")
    l=Label(w, text="USER NAME", font='Arial 17 bold')
    l.place(relx=0.5,rely=0.3,anchor=CENTER)
    name1=Entry(w)
    name1.pack()
    name1.place(relx=0.5,rely=0.35,anchor=CENTER)
    l1=Label(w,text="ID NUMBER",font='Arial 17 bold')
    l1.place(relx=0.5,rely=0.4,anchor=CENTER)
    idno=Entry(w)
    idno.pack()
    idno.place(relx=0.5,rely=0.45,anchor=CENTER)
    b=Button(w,text="OUTWARD",font='Arial 10 bold',command=checker)
    b.place(relx=0.45,rely=0.5,anchor=CENTER)
    lab=Button(w,text="INWARD",font="Arial 10 bold",command=checker1)
    lab.place(relx=0.55,rely=0.5,anchor=CENTER)
    w.mainloop()
def exit2():
    w.destroy()
    w.quit()
    w4.destroy()
    w4.quit()
def exit1():
    w.destroy()
    w.quit()
    w1.destroy()
    w1.quit()
if __name__=='__main__':
    entry()
