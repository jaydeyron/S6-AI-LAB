n = int(input("Enter the value for n: "))
mat=[[0]*n for _ in range(n)]
i,j=0,n//2

for num in range(1,n*n+1):
    mat[i][j]=num
    i,j=(i-1)%n,(j+1)%n
    if mat[i][j]!=0:
        i,j=(i+2)%n,(j-1)%n
[print(i) for i in mat]