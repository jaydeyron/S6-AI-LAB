import sys
intmax = sys.maxsize

def get_mat(n):
    m = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated integers): ").split()))
        m.append(row)
    return m

def tsp(i, mask, m, path):
    n = len(m)
    if mask == (1 << n) - 1 and m[i][0] != 0:
        return m[i][0]
    res = intmax
    for j in range(n):
        if not (mask & (1 << j)) and m[i][j] != 0:
            cost = m[i][j] + tsp(j, mask | (1 << j), m, path)
            if cost < res:
                res = cost
                path[mask] = j
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
path = [-1] * (1 << n)

min_cost = tsp(0, 1, m, path)
print(f"Minimum cost:\t{min_cost}")
print_path(path, n)