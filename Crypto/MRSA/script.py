from Crypto.Util.number import *


with open('flag.txt','rb') as f:
    flag = f.read().strip()

e=65537
p=getPrime(256)
q=getPrime(128)
n=p*q
m=bytes_to_long(flag)
ct=pow(m,e,n)

print (n)
print (e)
print (ct)

def enc(msg):
    print (p%m)

try:
    br="#"
    print (br*70)
    print ("Now here's the More part!!!")
    print ("Enter some message, and I will encrypt it for you")
    print ("But you gotta follow the condition that your message gotta be less than q (and like legitamite)")
    print (br*70)
    s=int(input("Enter: ").strip())
    assert(s>0 and s<q)        

    print (enc(long_to_bytes(s))
except:
    print ("Bruh why you be like this")
    exit()
    

