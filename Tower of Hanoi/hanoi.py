# tower of hanoi

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

n=int(input("Enter value for n: "))
print("\nNumber of moves needed: ",pow(2,n)-1,"\n")
tower_of_hanoi(n, 'A', 'C', 'B')