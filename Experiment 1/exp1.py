# n-queens problem

from itertools import permutations
ans,n = 0,int(input("Enter value of n : "))
for perm in permutations([i for i in range(n)]):
    count=0
    for i,j in enumerate(perm):
        for k,l in enumerate(perm):
            if i+j==k+l or i-j==k-l:
                count+=1
    if count==n:
        ans+=1
        for a in range(n):
            print("[",end="")
            for b in range(n):
                print(" 1 " if perm[a]==b else " 0 ",end="")
            print("]")
        print("\n")
print("No. of possible solutions: ",ans)