from Crypto.Util.number import *

with open('flag.txt','r') as f:
    flag = f.read().strip()

m=bytes_to_long(flag)
e=17
n_arr=[]
ct_arr=[]

for t in range(17):
  p=getPrime(256)
  q=getPrime(256)
  n=p*q

  assert (n>m)
  ct=pow(m,e,n)
  n_arr.append(n)
  ct_arr.append(ct)
  

print (n_arr)
print (ct_arr)

