from hashlib import *
from Crypto.Util.number import *
from Crypto.PublicKey import DSA
from secrets import *

def tryagain():
  print ("I'm so sorry, please try again :(")
  exit()

def H(msg):
  return sha256(msg).hexdigest()


msg=b"[REDACTED]"

l=3072
n=256
dsa=DSA.generate(3072)
p = dsa.p
q = dsa.q
h=randbelow(p-1)
if h<2:
  tryagain()
g=pow(h,(p-1)//q,p)
if g==1:
  tryagain()

print (p)
print (q)
print (g)

x=randbelow(q)
if x==0:
  tryagain()
 
y=pow(g,x,p)
print (y)

hash=int(H(msg),16)
num_tries=7

while num_tries>0:
  print ("You can encrypt "+str(num_tries)+" more times.")
  print ("\nDo you want to: ")
  print ("A: Encrypt again (you need to have a positive number of tries left)")
  print ("B: Guess the message")
  op=input().strip()
  if op=="B":
    break
  elif op!="A":
    print ("Bruh :/")
    exit()
  xor=input("Enter what you want to xor, in hex, but note that it must be greater than 2**32: ").strip()
  xor=int(xor,16)
  assert(xor>2**32)

  k=randbelow(q)^xor
  if k==0:
    tryagain()
  r=pow(g,k,p)
  s=(pow(k,q-2,q)*(hash+x*r))%q
  
  if r==0 or s==0:
    tryagain()
  
  print (r)
  print (s)
  num_tries-=1
  
print ("OK, now if you guess my message, I will give you the flag!")
s=input("Enter: ").strip()
if msg.decode('utf-8')==s:
  with open('flag.txt','rb') as g:
    flag = g.read().strip()
  print (flag)
else:
  print ("Better luck next time!")
