from tkinter import*
import tkinter
import random
top=tkinter.Tk()
code=''
def gen_cap():
  n=''
  for i in range(0,6):
      cap=random.randint(1,3)
      if(cap==1):
          value=random.randint(97,122)
          n+=chr(value)
      elif(cap==2):
          value=random.randint(65,90)
          n+=chr(value)
      else:
          value=random.randint(48,57)
          n+=chr(value)
  return n
def check():
      ck=ent_cap.get()
      ent_cap.delete(0,END)
      global code
      if(ck==code):
            print('Access')
      else :
            g=gen_cap()
            code=g
            display()
            c.create_text(160,40,text=g,font='Calibri 28 bold')
            c.grid(row=3,column=10)
            see=tkinter.Label(top,text='Opps! Wrong captcha : ',font='Times 10')
            see.grid(row=6,column=10)
def display():
      c.create_rectangle(80,10,240,70,fill='white')
      c.create_line(80,20,230,50)
      c.create_line(85,55,180,25)
      c.create_line(150,10,170,70)
      c.create_line(100,65,240,40)
def reset1():
      ent_cap.delete(0,END)
      global code
      g=gen_cap()
      code=g
      display()
      c.create_text(160,40,text=g,font='Calibri 28 bold')
      c.grid(row=3,column=10)
code=gen_cap()
Reg=tkinter.Label(top,text='Registration Number : ',font='Times 13')
Reg.grid(row=1,column=10)
Reg_ent=Entry(top)
Reg_ent.grid(row=1,column=11)
#top.geometry('300x300')
top.title("PASSWORD REMINDER")
c=Canvas(top,height=80,width=240)
display()
c.create_text(160,40,text=code,font='Calibri 28 bold')
c.grid(row=3,column=10)
see=tkinter.Label(top,text='Type the code you see above : ',font='Times 10')
see.grid(row=4,column=10)
ent_cap=Entry(top)
ent_cap.grid(row=5,column=10)
submit=tkinter.Button(top,text='Submit',relief=GROOVE,height=2,width=10,bg='lightgreen',command=check)
submit.grid(row=10,column=10)
reset=tkinter.Button(top , text='Reload',relief=GROOVE,height=1,width=6,bg='lightgreen',command=reset1)
reset.grid(row=3,column=11)
top.mainloop()
