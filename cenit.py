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
    print(x)

frase=str(input("ingrese frase: "))
cenit(frase)
