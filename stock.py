r=float(input("Enter returns: "))
c=float(input("Enter capital: "))
n=int(input("Enter number of days: "))
for i in range(n):
    c=c+(c*r)
    print(f"Day {i+1} capital: {c}")