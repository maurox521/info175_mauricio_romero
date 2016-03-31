import string
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
x=str(input("ingrese frase a encriptar: "))
y=int(input("ingrese salto: "))
print(encrypt(x,y))
