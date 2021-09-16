from hashlib import *
from Crypto.Util.number import *
from Crypto.PublicKey import *
from secrets import *

def tryagain():
  print ("I'm so sorry, please try again :(")
  exit()

def H(msg):
  return bytes_to_long(sha256(msg).hexdigest())


msg="[REDACTED]"

l=1024
n=160
dsa=DSA.generate(1024)
p = dsakey.p
q = dsakey.q
h=randbelow(p-1)
  if h<2:
    tryagain()
  g=pow(h,(p-1)/q,p)
  if g!=1:
    return g
  else:
    tryagain()

print (p)
print (q)
print (g)

x=randbelow(q)
if x==0:
  tryagain()
 
y=pow(g,x,p)
print (y)

xor=0
hash=H(msg)
for i in range(2):
  k=randbelow(q)^xor
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
s=input("Enter: ").strip().decode("utf-8") 
if msg==s:
  with open('flag.txt','rb') as g:
    flag = g.read().strip()
  print (flag)
else:
  print ("Better luck next time!")

  
  
