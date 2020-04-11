import random
import os


def isMovesLeft(board):
    ret = False
    for i in board:
        if ' ' in i:
            ret = True
            break
    return ret


def evaluate(board):
    ret = 0
    flag = False
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == 'X' or board[i][0] == 'O':
                if board[i][0] == 'X':
                    ret = 10
                else:
                    ret = -10
                flag = True
                break
    if flag:
        return ret
    else:
        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] \
                    == board[2][i]:
                if board[0][i] == 'X' or board[0][i] == 'O':
                    if board[0][i] == 'X':
                        ret = 10
                    else:
                        ret = -10
                    flag = True
                    break
        if flag:
            return ret
        else:
            if board[0][0] == board[1][1] and board[1][1] \
                    == board[2][2]:
                if board[0][0] == 'X' or board[0][0] == 'O':
                    if board[0][0] == 'X':
                        ret = 10
                    else:
                        ret = -10
                    flag = True
            if flag:
                return ret
            else:
                if board[0][2] == board[1][1] and board[1][1] \
                        == board[2][0]:
                    if board[0][2] == 'X' or board[0][2] == 'O':
                        if board[0][2] == 'X':
                            ret = 10
                        else:
                            ret = -10
                return ret


def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    else:
        if isMovesLeft(board) == False:
            return 0
        else:
            if isMax:
                best = -1000
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ' ':
                            board[i][j] = 'X'
                            best = max([best, minimax(board, depth + 1,
                                                      not isMax)])
                            board[i][j] = ' '
                return best
            else:
                best = 1000
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ' ':
                            board[i][j] = 'O'
                            best = min([best, minimax(board, depth + 1,
                                                      not isMax)])
                            board[i][j] = ' '
                return best


def findBestMove(board):
    bestVal = -1000
    bestMove = [-1, -1]
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                moveVal = minimax(board, 0, False)
                board[i][j] = ' '
                if moveVal > bestVal:
                    bestMove = [i, j]
                    bestVal = moveVal
    return bestMove


def display(board):
    print(f"""
         {board[0][0]} | {board[0][1]} | {board[0][2]} 
        -----------
         {board[1][0]} | {board[1][1]} | {board[1][2]} 
        -----------
         {board[2][0]} | {board[2][1]} | {board[2][2]} 
    """)
    return None


def clear(os):
    if os.name == 'nt':
        os.system("clc")
    else:
        os.system("clear")
    return None


clear(os)
moves = [i + 1 for i in range(9)]
while True:
    print("""
    Choose difficulty:
    1. Easy.
    2. Medium.
    3. Hard.
    """)
    difficulty = int(input())
    if 1 <= difficulty <= 3:
        clear(os)
        break
    else:
        clear(os)
        print("Bad choice!")
board = [[' '] * 3 for i in range(3)]
toss = random.choice(["Player", "Computer"])
print(f"{toss} goes first! You are O.")
if toss == "Player":
    while True:
        display(board)
        print("Your turn:")
        n = int(input())
        n -= 1
        if 0 <= n <= 8:
            moves.remove(n+1)
            board[n // 3][n % 3] = 'O'
            clear(os)
            break
        else:
            clear(os)
            print("Bad move!")
i = 0
while(isMovesLeft(board) and evaluate(board) != 10 and evaluate(board) != -10):
    if i % 2 == 0:
        if difficulty == 3:
            bestMove = findBestMove(board)
            n = (bestMove[0] * 3) + bestMove[1] + 1
        elif difficulty == 1:
            n = random.choice(moves)
            bestMove = [(n - 1) // 3, (n - 1) % 3]
        elif random.choice([True, False]):
            n = random.choice(moves)
            bestMove = [(n - 1) // 3, (n - 1) % 3]
        else:
            bestMove = findBestMove(board)
            n = (bestMove[0] * 3) + bestMove[1] + 1
        board[bestMove[0]][bestMove[1]] = 'X'
        moves.remove(n)
        print(f"Computer chose {n}.")
    else:
        while True:
            display(board)
            print("Your turn:")
            n = int(input())
            n -= 1
            if 0 <= n <= 8 and board[n // 3][n % 3] == ' ':
                moves.remove(n+1)
                board[n // 3][n % 3] = 'O'
                clear(os)
                break
            else:
                clear(os)
                print("Bad move!")
    i += 1
display(board)
if evaluate(board) == 10:
    print("You lost!")
elif evaluate(board) == -10:
    print("You won!")
else:
    print("Draw!")
