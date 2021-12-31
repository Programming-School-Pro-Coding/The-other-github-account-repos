from tkinter import *
import qrcode
from PIL import Image
#============================
wdo = Tk()
wdo.configure(bg='darkcyan')
wdo.minsize(700, 500)
wdo.resizable(False, False)
wdo.title("QR Code Maker")
#============================





def gg ():
    qr = qrcode.make(en1.get())
    qr.save(en2.get()+'.PNG')
    img = Image.open(qr,'r')
    img.show()
























lb1=Label(text="أنشاء كود الوصول السريع ", bg='darkcyan', fg='white', font=('Hacen Tunisia',30))
lb1.place(x=165,y=75)

lb2=Label(text="ادخل الرابط هنا",bg='darkcyan',fg="white",font=('Hacen Tunisia',20))
lb2.place(x=270,y=160)

lb3=Label(text='QR Code Maker',font=('Hacen Tunisia',40),bg='darkcyan',fg='white')
lb3.place(x=177,y=0)

lb4=Label(text='Black Dead المطور',bg='darkcyan',fg='white',font=('Hacen Tunisia','20'))
lb4.place(x=500,y=450)

lb5=Label(text='ادخل اسم الملف هنا',bg='darkcyan',fg='white',font=('Hacen Tunisia',20))
lb5.place(x=248,y=250)

en1=Entry(bg="white",bd=3,font=("arial",17),width=45)
en1.place(x=55,y=210)

en2=Entry(bg='white',bd=3,font=('arial',17),width=25)
en2.place(x=180,y=300)

bt1=Button(bg='darkcyan',fg="white",text="+انشاء",bd=3,font=('Hacen Tunisia',15),command=gg, height=-1)
bt1.place(x=310,y=350)

#bt2=Button(bg='darkcyan',fg='white',text="فتح الملف",font=('Hacen Tunisia',15),bd=3,command=mynigga, )
#bt2.place(x=302,y=420)