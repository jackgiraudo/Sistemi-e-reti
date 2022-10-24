import math
num = int(input("Inserire un numero"))
num=int(num)

ver = True
i=2

while i<math.sqrt(num) and ver==True:
   if num%i == 0: 
       ver=False
   if num%i == 1: 
       ver=True
   i=i+1

if ver==True:
    print("e primo")
else:
    print("NON e primo")
