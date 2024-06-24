from collections import deque

def is_valid_state(state, visited, X, Y):
    x, y = state
    return 0 <= x <= X and 0 <= y <= Y and state not in visited

def bfs(X, Y, Z):
    # Initial state (0, 0) - both jugs are empty
    initial_state = (0, 0)
    
    # Queue for BFS, starting with the initial state
    queue = deque([(initial_state, [])])
    
    # Set to keep track of visited states
    visited = set()
    
    while queue:
        (current_x, current_y), path = queue.popleft()
        
        # If we reach the desired amount of water in either jug, return the path
        if current_x == Z or current_y == Z:
            return path + [(current_x, current_y)]
        
        # Mark the current state as visited
        visited.add((current_x, current_y))
        
        # Possible actions to generate new states
        possible_moves = [
            (X, current_y),  # Fill Jug 1
            (current_x, Y),  # Fill Jug 2
            (0, current_y),  # Empty Jug 1
            (current_x, 0),  # Empty Jug 2
            (current_x - min(current_x, Y - current_y), current_y + min(current_x, Y - current_y)),  # Pour Jug 1 -> Jug 2
            (current_x + min(current_y, X - current_x), current_y - min(current_y, X - current_x))   # Pour Jug 2 -> Jug 1
        ]
        
        for new_state in possible_moves:
            if is_valid_state(new_state, visited, X, Y):
                queue.append((new_state, path + [(current_x, current_y)]))
    
    return None  # No solution found

def water_jug_solver(X, Y, Z):
    # Check for invalid cases
    if Z > max(X, Y) or (Z % gcd(X, Y) != 0):
        return None
    
    result = bfs(X, Y, Z)
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

X = int(input("Enter capacity of Jug 1: "))
Y = int(input("Enter capacity of Jug 2: "))
Z = int(input("Enter the target amount: "))

solution = water_jug_solver(X, Y, Z)

if solution:
    print("Steps to achieve the target amount of water:")
    for step in solution:
        print(step)
else:
    print("No solution exists for the given inputs.")