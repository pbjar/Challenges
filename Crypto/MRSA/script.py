from Crypto.Util.number import *


with open('flag.txt','rb') as f:
    flag = f.read().strip()
    
e=getPrime(100)
p=getPrime(256)
q=getPrime(128)
n=p*q
m=bytes_to_long(flag)
ct=pow(m,e,n)

print (n)
print (e)
print (ct)

def enc(msg):
  print ((p*pow(m,e,q))%q)

while True:
  br="#"
  print (br*70)
  print ("Now here's the More part!!!")
  print ("Enter some message, and I will encrypt it for you")
  print (br*70)
  s=input("Enter: ").strip()
  
  print (enc(long_to_bytes(s))

