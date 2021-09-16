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
print ("All right, so the goal is that I will send you a list. Then for each corresponding number, you will output a number back to me, a, such that it satisfies that there exists a b such that a is congruent to b to the "+str(mod/small)+" modulo mod"


