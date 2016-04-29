def comparar(a,b):
    if a>b:
        print("el numero mayor es : ",a)
        print("el numero menor es : ",b)
    elif a==b:
        print("los numeros son iguales")
    else:
        print("el numero mayor es : ",b)
        print("el numero menor es : ",a)

x=int(input("ingrese primer numero: "))
y=int(input("ingrese segundo numero: "))
comparar(x,y)
