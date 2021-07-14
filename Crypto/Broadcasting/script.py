from Crypto.Util.number import *

with open('flag.txt','r') as f:
    flag = f.read().strip()

m=bytes_to_long(flag)
e=3

for t in range(e):
  p=getPrime(256)
  q=getPrime(256)
  n=p*q

  assert (n>m)
    
  ct=pow(m,e,n)
  print (ct)
  print (n)
