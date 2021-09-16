from hashlib import *
from Crypto.Util.number import *
from Crypto.PublicKey import DSA
from random import *

seed([REDACTED])

def tryagain():
  print ("I'm so sorry, please try again :(")
  exit()

def H(msg):
  return sha256(msg).hexdigest()


msg=b"[REDACTED]"

l=1024
n=160
dsa=DSA.generate(1024)
p = dsa.p
q = dsa.q
h=randint(2,p-2)
g=pow(h,(p-1)//q,p)
if g==1:
  tryagain()

print (p)
print (q)
print (g)

x=randint(1,q-1) 
y=pow(g,x,p)
print (y)

xor=0
hash=int(H(msg),16)
for i in range(2):
  k=randint(1,q-1)^xor
  if k==0:
    tryagain()
  r=pow(g,k,p)
  s=(pow(k,q-2,q)*(hash+x*r))%q
  
  if r==0 or s==0:
    tryagain()
  
  print (r)
  print (s)
  xor=k
  
print ("OK, now if you guess my message, I will give you the flag!")
s=input("Enter: ").strip()
if msg.decode('utf-8')==s:
  with open('flag.txt','rb') as g:
    flag = g.read().strip()
  print (flag)
else:
  print ("Better luck next time!")
