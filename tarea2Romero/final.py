from tkinter import *
import string
    
def cenit(x):
    for i in x:
        if(i=="c"):
            x=x.replace("c","p")
        elif(i=="e"):
            x=x.replace("e", "o")
        elif(i=="n"):
            x=x.replace("n", "l")
        elif(i=="i"):
            x=x.replace("i", "a")
        elif(i=="t"):
            x=x.replace("t", "r")
    
def encrypt(word,jump):
    abcd=string.ascii_lowercase
    encrypt_word=""
    for char in word:
        if char!=" ":
            index=(abcd.index(char.lower())+jump)%len(abcd)
            encrypt_word += abcd[index]
        else:
                   encrypt_word += char
    return encrypt_word
 

ventana = Tk()
v=IntVar()
ventana.title("encriptacion de frase")
ventana.config(bg="blue")
ventana.geometry("500x400")
ventana.resizable(0,0)
etiqueta1=Label(ventana,text="ingrese frase a encriptar: ").place(x=10,y=20)
z=StringVar()
w=StringVar()
entrada1=Entry(ventana,textvariable=z).place(x=200,y=20,width=200, height=80)
boton = Button(ventana,text="encriptar",command=cenit(z.get()),width=15, height=1).place(x=10,y=200)
etiqueta2=Label(ventana,text="la frase resultante es: ").place(x=10,y=300)
entrada2=Entry(ventana,text=w.set(z)).place(x=200,y=280,width=200, height=80)
etiqueta3=Label(ventana,text="seleccione forma a encriptar: ").place(x=10,y=120)
salto=Spinbox(ventana,values=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27")).place(x=250,y=200)
etiqueta4=Label(ventana,text="salto: ").place(x=170,y=200)
r1=Radiobutton(ventana,text="cesar",variable=v,value=1).place(x=200,y=120)
r2=Radiobutton(ventana,text="cenit-polar",variable=v,value=2).place(x=250,y=120)
ventana.mainloop()

