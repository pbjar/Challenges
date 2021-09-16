from random import *
# DOESN'T WORK
def gen():
  mod=randint(10**9,10**10)
  while (mod%2==0):
    mod=randint(10**9,10**10)
  return mod

mod=gen()
small=mod
while True:
  for i in range(2,(mod+5)**(1/2)):
    if mod%i==0:
      small=i
      break
  if small!=mod:
    mod*=small
    break
  mod=gen()

lst=[]
for i in range(small-1):
  lst.append(1)

r=randint(10,small)
for i in range(r):
  lst.append(0)
  
lst=shuffle(lst)
print ("All right, so the goal is that I will send you a list.")
print ("Then you will send me a list of numbers back with the same size, separated by spaces.")
print ("Now for each number in your list, a, if it satisfies a to the power of "+str(small)+" is congruent to 1 mod "+str(mod)+" I will give you the flag :yayy:")
print (lst)

s=input("Enter: ").strip().split()
s=[int (i) for i in s]
check=len(s)==len(lst)
for i in range(len(s)):
  check=check & s[i]==lst[i]

if check:
  with open('flag.txt','rb') as f:
      flag = f.read().strip()
  print (flag)
else:
  print ("Better luck next time!")
