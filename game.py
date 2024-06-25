from tkinter import *
from csv import *
from tkinter import messagebox

w = Tk()
w.minsize(1000,800)
w.maxsize(1600,800)
w.title("Jigsaw")
l = Label(w,text="welcome to game")
l.pack()

answer1 = [ [0,0,0],[0,0,0],[0,0,0] ]

name = StringVar()
time = IntVar()
E1 = StringVar()
var = StringVar()

pp1 = PhotoImage(file='q1.png')
pp2 = PhotoImage(file='q2.png')
pp3 = PhotoImage(file='q3.png')
pp4 = PhotoImage(file='q4.png')
pp5 = PhotoImage(file='q5.png')
pp6 = PhotoImage(file='q6.png')
pp7 = PhotoImage(file='q7.png')
pp8 = PhotoImage(file='q8.png')
pp9 = PhotoImage(file='q9.png')
BW = PhotoImage(file='white.png')

select = 0
b1_use = 0
b2_use = 0
b3_use = 0
b4_use = 0
b5_use = 0
b6_use = 0
b7_use = 0
b8_use = 0
b9_use = 0

def show1_2():
  global b1_use
  if b1_use == 0:
      global select  
      select = 1
      p1["image"] = BW
      b1_use = 1

def show2_2():
  global b2_use
  if b2_use == 0:
      global select  
      select = 2
      p2["image"] = BW
      b2_use = 1

def show3_2():
  global b3_use
  if b3_use == 0:
      global select  
      select = 3
      p3["image"] = BW
      b3_use = 1

def show4_2():
  global b4_use
  if b4_use == 0:
      global select  
      select = 4
      p4["image"] = BW
      b4_use = 1

def show5_2():
  global b5_use
  if b5_use == 0:
      global select  
      select = 5
      p5["image"] = BW
      b5_use = 1

def show6_2():
  global b6_use
  if b6_use == 0:
      global select  
      select = 6
      p6["image"] = BW
      b6_use = 1

def show7_2():
  global b7_use
  if b7_use == 0:
      global select  
      select = 7
      p7["image"] = BW
      b7_use = 1

def show8_2():
  global b8_use
  if b8_use == 0:
      global select  
      select = 8
      p8["image"] = BW
      b8_use = 1

def show9_2():
  global b9_use
  if b9_use == 0:
      global select  
      select = 9
      p9["image"] = BW
      b9_use = 1
    
def show1_1(): #p10
    global select
    global answer1
    print(select)
    answer1[0][0] = select 
    if select == 1:
        p10['image'] = pp2
    if select == 2:
        p10['image'] = pp4
    if select == 3:
        p10['image'] = pp5 
    if select == 4:
        p10['image'] = pp9
    if select == 5:
        p10['image'] = pp1
    if select == 6:
        p10['image'] = pp3
    if select == 7:
        p10['image'] = pp8 
    if select == 8:
        p10['image'] = pp7
    if select == 9:
        p10['image'] = pp6
    select = 0

def show2_1():  #p11
    global select
    global answer1
    print(select)
    answer1[1][0] = select
    if select == 1:
        p11['image'] = pp2
    if select == 2:
        p11['image'] = pp4
    if select == 3:
        p11['image'] = pp5 
    if select == 4:
        p11['image'] = pp9
    if select == 5:
        p11['image'] = pp1
    if select == 6:
        p11['image'] = pp3
    if select == 7:
        p11['image'] = pp8 
    if select == 8:
        p11['image'] = pp7
    if select == 9:
        p11['image'] = pp6 
    select = 0

def show3_1():  #p12
    global select
    global answer1
    print(select)
    answer1[2][0] = select
    if select == 1:
        p12['image'] = pp2
    if select == 2:
        p12['image'] = pp4
    if select == 3:
        p12['image'] = pp5 
    if select == 4:
        p12['image'] = pp9
    if select == 5:
        p12['image'] = pp1
    if select == 6:
        p12['image'] = pp3
    if select == 7:
        p12['image'] = pp8 
    if select == 8:
        p12['image'] = pp7
    if select == 9:
        p12['image'] = pp6    
    select = 0  

def show4_1():  #p13
    global select
    global answer1
    print(select)
    answer1[0][1] = select
    if select == 1:
        p13['image'] = pp2
    if select == 2:
        p13['image'] = pp4
    if select == 3:
        p13['image'] = pp5 
    if select == 4:
        p13['image'] = pp9
    if select == 5:
        p13['image'] = pp1
    if select == 6:
        p13['image'] = pp3
    if select == 7:
        p13['image'] = pp8 
    if select == 8:
        p13['image'] = pp7
    if select == 9:
        p13['image'] = pp6
    select = 0
    
def show5_1():  #p14
    global select
    global answer1
    print(select)
    answer1[1][1] = select
    if select == 1:
        p14['image'] = pp2
    if select == 2:
        p14['image'] = pp4
    if select == 3:
        p14['image'] = pp5 
    if select == 4:
        p14['image'] = pp9
    if select == 5:
        p14['image'] = pp1
    if select == 6:
        p14['image'] = pp3
    if select == 7:
        p14['image'] = pp8 
    if select == 8:
        p14['image'] = pp7
    if select == 9:
        p14['image'] = pp6
    select = 0

def show6_1():  #p15
    global select
    global answer1
    print(select)
    answer1[2][1] = select
    if select == 1:
        p15['image'] = pp2
    if select == 2:
        p15['image'] = pp4
    if select == 3:
        p15['image'] = pp5 
    if select == 4:
        p15['image'] = pp9
    if select == 5:
        p15['image'] = pp1
    if select == 6:
        p15['image'] = pp3
    if select == 7:
        p15['image'] = pp8 
    if select == 8:
        p15['image'] = pp7
    if select == 9:
        p15['image'] = pp6
    select = 0

def show7_1():  #p16
    global select
    global answer1
    print(select)
    answer1[0][2] = select
    if select == 1:
        p16['image'] = pp2
    if select == 2:
        p16['image'] = pp4
    if select == 3:
        p16['image'] = pp5 
    if select == 4:
        p16['image'] = pp9
    if select == 5:
        p16['image'] = pp1
    if select == 6:
        p16['image'] = pp3
    if select == 7:
        p16['image'] = pp8 
    if select == 8:
        p16['image'] = pp7
    if select == 9:
        p16['image'] = pp6
    select = 0

def show8_1():  #p17
    global select
    global answer1
    print(select)
    answer1[1][2] = select
    if select == 1:
        p17['image'] = pp2
    if select == 2:
        p17['image'] = pp4
    if select == 3:
        p17['image'] = pp5 
    if select == 4:
        p17['image'] = pp9
    if select == 5:
        p17['image'] = pp1
    if select == 6:
        p17['image'] = pp3
    if select == 7:
        p17['image'] = pp8 
    if select == 8:
        p17['image'] = pp7
    if select == 9:
        p17['image'] = pp6
    select = 0

def show9_1():  #p18
    global select
    global answer1
    print(select)
    answer1[2][2] = select
    if select == 1:
        p18['image'] = pp2
    if select == 2:
        p18['image'] = pp4
    if select == 3:
        p18['image'] = pp5 
    if select == 4:
        p18['image'] = pp9
    if select == 5:
        p18['image'] = pp1
    if select == 6:
        p18['image'] = pp3
    if select == 7:
        p18['image'] = pp8 
    if select == 8:
        p18['image'] = pp7
    if select == 9:
        p18['image'] = pp6
    select = 0

    
def save():
    global name
    Label(w,text="Name").place(x=50,y=30)
    E2=Entry(w,textvariable=E1,width=15).place(x=50,y=50)
    Button(w,text="submit",command=submit).place(x=50,y=70)

def submit():
    global E1
    with open("data.csv","a",encoding='UTF-8') as fa:
      we=writer(fa,lineterminator='\n')
      print(E1.get())
      we.writerow([E1.get()])

  
def load():
    with open("data.csv","r",encoding='UTF-8') as aa:
        az=reader(aa)
        l=list(az)
        print(l)
        Label(w,text="load",bg='white',fg='black',font='SimSun 14 bold',width=5,height=2).place(x=50,y=110)

        vag = ""
        for k in range(len(l)):
            vag = vag + str(l[k][0]) + '\n'

        var.set(vag)
        Label(w,textvariable=var).place(x=65,y=170)       
            
def check():
    global answer1
    if answer1[0][0]==5 and answer1[1][0]==2 and answer1[2][0]==8 and answer1[0][1]==1 and answer1[1][1]==3 and answer1[2][1]==7 and answer1[0][2]==6 and answer1[1][2]==9 and answer1[2][2]==4:
        messagebox.showwarning("ถูกต้อง!","ไปต่อจ้า")
        Button(w,text="Next",command=w.destroy).place(x=650,y=325)
    else :
        messagebox.showwarning("คำตอบ,ผิด","ตอบใหม่เร็ว")

def htp():
    messagebox.showinfo("how to play","นำรูปจากด้านล่างมาใส่ในช่องให้ถูกต้องง")
    messagebox.showinfo("how to play","การ save กดปุ่ม save แล้วกรอกชื่อลงในช่อง")

#รูปที่ใช้เลือก
p1 = Button(w,width=100,height=100, command=show1_2,image=pp2 )
p1.place(x=100,y=500)
p2 = Button(w,width=100,height=100, command=show2_2,image=pp4 )
p2.place(x=275,y=500)
p3 = Button(w,width=100,height=100, command=show3_2,image=pp5 )
p3.place(x=450,y=500)
p4 = Button(w,width=100,height=100, command=show4_2,image=pp9 )
p4.place(x=625,y=500)
p5 = Button(w,width=100,height=100, command=show5_2,image=pp1 )
p5.place(x=800,y=500)
p6 = Button(w,width=100,height=100, command=show6_2,image=pp3 )
p6.place(x=190,y=625)
p7 = Button(w,width=100,height=100, command=show7_2,image=pp8)
p7.place(x=365,y=625)
p8 = Button(w,width=100,height=100, command=show8_2,image=pp7 )
p8.place(x=540,y=625)
p9 = Button(w,width=100,height=100, command=show9_2,image=pp6 )
p9.place(x=715,y=625)

#รูปในตาราง
p10 = Button(w,width=100,height=100, command=show1_1,image=BW ) #1
p10.place(x=325,y=100)
p11 = Button(w,width=100,height=100, command=show2_1,image=BW ) #4
p11.place(x=325,y=200)
p12 = Button(w,width=100,height=100, command=show3_1,image=BW ) #7
p12.place(x=325,y=300)
p13 = Button(w,width=100,height=100, command=show4_1,image=BW ) #2
p13.place(x=425,y=100)
p14 = Button(w,width=100,height=100, command=show5_1,image=BW ) #5
p14.place(x=425,y=200)
p15 = Button(w,width=100,height=100, command=show6_1,image=BW ) #8
p15.place(x=425,y=300)
p16 = Button(w,width=100,height=100, command=show7_1,image=BW ) #3
p16.place(x=525,y=100)
p17 = Button(w,width=100,height=100, command=show8_1,image=BW ) #6
p17.place(x=525,y=200)
p18 = Button(w,width=100,height=100, command=show9_1,image=BW ) #9
p18.place(x=525,y=300)



#ปุ่มคำสั่ง
b1 = Button(w,text="save",command=save ,width=10,height=3)
b1.place(x=850,y=50)
b3 = Button(w,text="check",command=check )
b3.place(x=650,y=225)
b4 = Button(w,text="load",command=load , width=10,height=3)
b4.place(x=850,y=150)
b5 = Button(w,text="how to play",command=htp , width=10,height=3)
b5.place(x=850,y=250)

w.mainloop()

#page 2

b = Tk()
b.minsize(1000,800)
b.maxsize(1600,800)
b.title("Jigsaw")

qq1 = PhotoImage(file='p1.png')
qq2 = PhotoImage(file='p2.png')
qq3 = PhotoImage(file='p3.png')
qq4 = PhotoImage(file='p4.png')
qq5 = PhotoImage(file='p5.png')
qq6 = PhotoImage(file='p6.png')
qq7 = PhotoImage(file='p7.png')
qq8 = PhotoImage(file='p8.png')
qq9 = PhotoImage(file='p9.png')
BW = PhotoImage(file='white.png')

select = 0
p1_use = 0
p2_use = 0
p3_use = 0
p4_use = 0
p5_use = 0
p6_use = 0
p7_use = 0
p8_use = 0
p9_use = 0

E3 = StringVar()
var2 = StringVar()

answer2 = [ [0,0,0],[0,0,0],[0,0,0] ]

def show1_3():
  global p1_use
  if p1_use == 0:
      global select  
      select = 1
      e1["image"] = BW
      p1_use = 1

def show2_3():
  global p2_use
  if p2_use == 0:
      global select  
      select = 2
      e2["image"] = BW
      p2_use = 1

def show3_3():
  global p3_use
  if p3_use == 0:
      global select  
      select = 3
      e3["image"] = BW
      p3_use = 1

def show4_3():
  global p4_use
  if p4_use == 0:
      global select  
      select = 4
      e4["image"] = BW
      p4_use = 1

def show5_3():
  global p5_use
  if p5_use == 0:
      global select  
      select = 5
      e5["image"] = BW
      p5_use = 1

def show6_3():
  global p6_use
  if p6_use == 0:
      global select  
      select = 6
      e6["image"] = BW
      p6_use = 1

def show7_3():
  global p7_use
  if p7_use == 0:
      global select  
      select = 7
      e7["image"] = BW
      p7_use = 1

def show8_3():
  global p8_use
  if p8_use == 0:
      global select  
      select = 8
      e8["image"] = BW
      p8_use = 1

def show9_3():
  global p9_use
  if p9_use == 0:
      global select  
      select = 9
      e9["image"] = BW
      p9_use = 1

def show1_4(): #e10
    global select
    global answer1
    print(select)
    answer2[0][0] = select
    if select == 1:
        e10['image'] = qq2
    if select == 2:
        e10['image'] = qq4
    if select == 3:
        e10['image'] = qq5 
    if select == 4:
        e10['image'] = qq9
    if select == 5:
        e10['image'] = qq1
    if select == 6:
        e10['image'] = qq3
    if select == 7:
        e10['image'] = qq8 
    if select == 8:
        e10['image'] = qq7
    if select == 9:
        e10['image'] = qq6
    select = 0

def show2_4():  #e11
    global select
    global answer1
    print(select)
    answer2[1][0] = select
    if select == 1:
        e11['image'] = qq2
    if select == 2:
        e11['image'] = qq4
    if select == 3:
        e11['image'] = qq5 
    if select == 4:
        e11['image'] = qq9
    if select == 5:
        e11['image'] = qq1
    if select == 6:
        e11['image'] = qq3
    if select == 7:
        e11['image'] = qq8 
    if select == 8:
        e11['image'] = qq7
    if select == 9:
        e11['image'] = qq6 
    select = 0

def show3_4():  #e12
    global select
    global answer1
    print(select)
    answer2[2][0] = select
    if select == 1:
        e12['image'] = qq2
    if select == 2:
        e12['image'] = qq4
    if select == 3:
        e12['image'] = qq5 
    if select == 4:
        e12['image'] = qq9
    if select == 5:
        e12['image'] = qq1
    if select == 6:
        e12['image'] = qq3
    if select == 7:
        e12['image'] = qq8 
    if select == 8:
        e12['image'] = qq7
    if select == 9:
        e12['image'] = qq6    
    select = 0  

def show4_4():  #e13
    global select
    global answer1
    print(select)
    answer2[0][1] = select
    if select == 1:
        e13['image'] = qq2
    if select == 2:
        e13['image'] = qq4
    if select == 3:
        e13['image'] = qq5 
    if select == 4:
        e13['image'] = qq9
    if select == 5:
        e13['image'] = qq1
    if select == 6:
        e13['image'] = qq3
    if select == 7:
        e13['image'] = qq8 
    if select == 8:
        e13['image'] = qq7
    if select == 9:
        e13['image'] = qq6
    select = 0
    
def show5_4():  #e14
    global select
    global answer1
    print(select)
    answer2[1][1] = select
    if select == 1:
        e14['image'] = qq2
    if select == 2:
        e14['image'] = qq4
    if select == 3:
        e14['image'] = qq5 
    if select == 4:
        e14['image'] = qq9
    if select == 5:
        e14['image'] = qq1
    if select == 6:
        e14['image'] = qq3
    if select == 7:
        e14['image'] = qq8 
    if select == 8:
        e14['image'] = qq7
    if select == 9:
        e14['image'] = qq6
    select = 0

def show6_4():  #e15
    global select
    global answer1
    print(select)
    answer2[2][1] = select
    if select == 1:
        e15['image'] = qq2
    if select == 2:
        e15['image'] = qq4
    if select == 3:
        e15['image'] = qq5 
    if select == 4:
        e15['image'] = qq9
    if select == 5:
        e15['image'] = qq1
    if select == 6:
        e15['image'] = qq3
    if select == 7:
        e15['image'] = qq8 
    if select == 8:
        e15['image'] = qq7
    if select == 9:
        e15['image'] = qq6
    select = 0

def show7_4():  #e16
    global select
    global answer1
    print(select)
    answer2[0][2] = select
    if select == 1:
        e16['image'] = qq2
    if select == 2:
        e16['image'] = qq4
    if select == 3:
        e16['image'] = qq5 
    if select == 4:
        e16['image'] = qq9
    if select == 5:
        e16['image'] = qq1
    if select == 6:
        e16['image'] = qq3
    if select == 7:
        e16['image'] = qq8 
    if select == 8:
        e16['image'] = qq7
    if select == 9:
        e16['image'] = qq6
    select = 0

def show8_4():  #e17
    global select
    global answer1
    print(select)
    answer2[1][2] = select
    if select == 1:
        e17['image'] = qq2
    if select == 2:
        e17['image'] = qq4
    if select == 3:
        e17['image'] = qq5 
    if select == 4:
        e17['image'] = qq9
    if select == 5:
        e17['image'] = qq1
    if select == 6:
        e17['image'] = qq3
    if select == 7:
        e17['image'] = qq8 
    if select == 8:
        e17['image'] = qq7
    if select == 9:
        e17['image'] = qq6
    select = 0

def show9_4():  #e18
    global select
    global answer1
    print(select)
    answer2[2][2] = select
    if select == 1:
        e18['image'] = qq2
    if select == 2:
        e18['image'] = qq4
    if select == 3:
        e18['image'] = qq5 
    if select == 4:
        e18['image'] = qq9
    if select == 5:
        e18['image'] = qq1
    if select == 6:
        e18['image'] = qq3
    if select == 7:
        e18['image'] = qq8 
    if select == 8:
        e18['image'] = qq7
    if select == 9:
        e18['image'] = qq6
    select = 0

def save_1():
    global name
    Label(b,text="Name").place(x=50,y=30)
    E4=Entry(b,textvariable=E3,width=15).place(x=50,y=50)
    Button(b,text="submit",command=submit_1).place(x=50,y=70)

def submit_1():
    global E1
    with open("data2.csv","a",encoding='UTF-8') as fa:
      wa=writer(fa,lineterminator='\n')
      print(E3.get())
      wa.writerow([E3.get()])

  
def load_1():
    with open("data2.csv","r",encoding='UTF-8') as aa:
        az=reader(aa)
        ll=list(az)
        print(ll)
        Label(b,text="load",bg='white',fg='black',font='SimSun 14 bold',width=5,height=2).place(x=50,y=110)

        vag2 = ""
        for n in range(len(ll)):
            vag2 = vag2 + str(ll[n][0]) + '\n'

        var2.set(vag2)
        Label(b,textvariable=var2).place(x=65,y=170) 
        
def check_1():
    global answer2
    if answer2[0][0]==5 and answer2[1][0]==2 and answer2[2][0]==8 and answer2[0][1]==1 and answer2[1][1]==3 and answer2[2][1]==7 and answer2[0][2]==6 and answer2[1][2]==9 and answer2[2][2]==4:
        messagebox.showwarning("ถูกต้อง!","เสียดายจังไม่มีให้ทำแล้ว")
    else :
        messagebox.showwarning("คำตอบ,ผิด","ตอบใหม่เร็ว")

def kill_2():
    b.destroy()

#รูปที่ใช้เลือก
e1 = Button(b,width=100,height=100, command=show1_3,image=qq2 )
e1.place(x=100,y=500)
e2 = Button(b,width=100,height=100, command=show2_3,image=qq4 )
e2.place(x=275,y=500)
e3 = Button(b,width=100,height=100, command=show3_3,image=qq5 )
e3.place(x=450,y=500)
e4 = Button(b,width=100,height=100, command=show4_3,image=qq9 )
e4.place(x=625,y=500)
e5 = Button(b,width=100,height=100, command=show5_3,image=qq1 )
e5.place(x=800,y=500)
e6 = Button(b,width=100,height=100, command=show6_3,image=qq3 )
e6.place(x=190,y=625)
e7 = Button(b,width=100,height=100, command=show7_3,image=qq8 )
e7.place(x=365,y=625)
e8 = Button(b,width=100,height=100, command=show8_3,image=qq7 )
e8.place(x=540,y=625)
e9 = Button(b,width=100,height=100, command=show9_3,image=qq6 )
e9.place(x=715,y=625)

#รูปในตาราง
e10 = Button(b,width=100,height=100, command=show1_4,image=BW )
e10.place(x=325,y=100)
e11 = Button(b,width=100,height=100, command=show2_4,image=BW )
e11.place(x=325,y=200)
e12 = Button(b,width=100,height=100, command=show3_4,image=BW )
e12.place(x=325,y=300)
e13 = Button(b,width=100,height=100, command=show4_4,image=BW )
e13.place(x=425,y=100)
e14 = Button(b,width=100,height=100, command=show5_4,image=BW )
e14.place(x=425,y=200)
e15 = Button(b,width=100,height=100, command=show6_4,image=BW )
e15.place(x=425,y=300)
e16 = Button(b,width=100,height=100, command=show7_4,image=BW )
e16.place(x=525,y=100)
e17 = Button(b,width=100,height=100, command=show8_4,image=BW )
e17.place(x=525,y=200)
e18 = Button(b,width=100,height=100, command=show9_4,image=BW )
e18.place(x=525,y=300)

#ปุ่มคำสั่ง
b1_1 = Button(b,text="save",command=save_1 , width=10,height=3)
b1_1.place(x=850,y=50)
b2_1 = Button(b,text="exit",command=kill_2 ,width=10,height=3)
b2_1.place(x=890,y=725)
b3_1 = Button(b,text="check",command=check_1 )
b3_1.place(x=650,y=225)
b4_1 = Button(b,text="load",command=load_1 , width=10,height=3)
b4_1.place(x=850,y=150)

b.mainloop()
