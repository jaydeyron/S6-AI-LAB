# travelling salesman problem

# sample test cases
# m[4][4]={ {0,10,15,20},{5,0,9,10},{6,13,0,12},{8,8,9,0} } # ans=35
# m[5][5]={ {0,2,0,12,5},{2,0,4,8,0},{0,4,0,3,3},{12,8,3,0,10},{5,0,3,10,0} } # ans=21

import sys
intmax = sys.maxsize

def get_mat(n):
    m = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated integers): ").split()))
        m.append(row)
    return m

def print_mat(m):
    n = len(m)
    print("\n  ", end="")
    for i in range(n):
        print(f" {chr(65 + i)} ", end="")
    print("\n\n")
    for i in range(n):
        print(f"{chr(65 + i)}  ", end="")
        for j in range(n):
            print(f"{m[i][j]}  ", end="")
        print("\n\n")

def tsp(i, mask, m, memo, path):
    n = len(m)
    if mask == (1 << n) - 1 and m[i][0] != 0:
        return m[i][0]
    if (i, mask) in memo:
        return memo[(i, mask)]
    res = intmax
    for j in range(n):
        if not (mask & (1 << j)) and m[i][j] != 0:
            cost = m[i][j] + tsp(j, mask | (1 << j), m, memo, path)
            if cost < res:
                res = cost
                path[mask] = j
    memo[(i, mask)] = res
    return res

def print_path(path, n):
    print("\nPath:\tA-->", end="")
    mask = 1
    for _ in range(1, n):
        next_city = path[mask]
        print(f"{chr(65 + next_city)}-->", end="")
        mask |= (1 << next_city)
    print("A\n")

n = int(input("Enter the number of cities: "))
m = get_mat(n)
print_mat(m)

memo = {}
path = [-1] * (1 << n)

min_cost = tsp(0, 1, m, memo, path)
print(f"Minimum cost:\t{min_cost}")
print_path(path, n)