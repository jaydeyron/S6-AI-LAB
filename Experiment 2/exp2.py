# water jug problem

import math
jug1=int(input("Enter capacity of first jug: "))
jug2=int(input("Enter capacity of second jug: "))
target=int(input("Enter the target: "))
steps=[]
if (target>jug1 and target>jug2) or target%(math.gcd(jug1,jug2))!=0:
    print("Not possible to measure")
elif (target==jug2 or target==jug1):
    steps.append((jug1,jug2))
else:
    x,y=0,0
    while x!=target and y!=target:
        if x==0:
            x+=jug1
            steps.append((x,y))
        elif y==jug2:
            y-=jug2
            steps.append((x,y))
        else:
            pour=min(x,jug2-y)
            x-=pour
            y+=pour
            steps.append((x,y))
for i in steps:
    print(i)