from tkinter import*
import random
root=Tk()
root.title("Testing Random Function")
root.geometry("500x500")
ip=Entry(root)
g1=Label(root)
g2=Label(root)
array_3d=[[["a","f","e","p","j","k","m","d","h"],["king","queen"],["!","@","#","$","%","^","&","*"]]]
print(array_3d[0][2][3])
def newpass():
    g1["text"]="guestpassword : "+ip.get()
    r1=random.randint(0,5)
    r2=random.randint(0,1)
    r3=random.randint(0,7)
    l1=array_3d[0][0][r1]
    l2=array_3d[0][1][r2]
    l3=array_3d[0][2][r3]
    g2["text"]="generated password : "+l1+""+l2+""+l3
ip.place(relx=0.5,rely=0.3,anchor=CENTER)
g1.place(relx=0.5,rely=0.4,anchor=CENTER)
g2.place(relx=0.5,rely=0.6,anchor=CENTER)
btn=Button(root,text="New password ",command=newpass)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
    