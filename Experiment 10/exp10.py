# connect-four

def check_win(matrix, i, j, s):
    try:
        if all(matrix[i + k][j] == s for k in range(4)):
            return True
    except:
        pass
    try:
        if all(matrix[i][j + k] == s for k in range(4)):
            return True
    except:
        pass
    try:
        if all(matrix[i + k][j - k] == s for k in range(4)):
            return True
    except:
        pass
    try:
        if all(matrix[i + k][j + k] == s for k in range(4)):
            return True
    except:
        pass
    return False

def display_board(matrix):
    for i in matrix:
        print(" ".join(i))
from random import randint
list1=[6]*7
matrix=[[" . "]*7 for _ in range(6)]
player_positions=[]
computer_positions=[]
flag=1
while flag==1:
    try:
        pos=int(input("Enter the column : "))  
        list1[pos]-=1
        matrix[list1[pos]][pos]=" P "
        print(" ",'   '.join(f"{i}" for i in range(7)),sep="") #This is to display the top 0 1 2 3... numbering
        display_board(matrix)
        player_positions.append((list1[pos],pos))
        for i,j in player_positions[::-1]:
            if check_win(matrix,i,j," P "):
                print("You win ")
                print(f"Position : row {i} column {j}")
                flag=0
                exit()
        print("Computer move : ")
        while True:
            num=randint(0,6)
            if list1[num]-1>=0:
                break
        list1[num]-=1
        matrix[list1[num]][num]=" C "
        print(" ",'   '.join(f"{i}" for i in range(7)),sep="") #This is to display the top 0 1 2 3... numbering
        display_board(matrix)
        computer_positions.append((list1[num],num))
        for i,j in computer_positions[::-1]:
            if check_win(matrix,i,j," C "):
                print("Computer Win ")
                print(f"Position : row {i} column {j}")

                flag=0
                exit()
    except:
        print("Game over")
        break