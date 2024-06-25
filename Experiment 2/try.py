import math

jug1=int(input("Enter the capacity of jug 1: "))
jug2=int(input("Enter the capacity of jug 2: "))
target=int(input("Enter the target: "))
steps=[]

if (target>jug1 and target>jug2) or target%(math.gcd(jug1,jug2))!=0:
    print("Not possible")
elif target==jug1 or target==jug2:
    steps.append((jug1,0) if target==jug1 else (0,jug2))
else:
    x,y=0,0
    while x!=target and y!=target:
        if x==0:
            x+=jug1
        elif y==jug2:
            y-=jug2
        else:
            pour=min(x,jug2-y)
            x-=pour
            y+=pour
        steps.append((x,y))
for i in steps:
    print(i)
print("No. of steps: ", len(steps)-1)