"""
Name: Sara Johnson
lab10.py

Problem: Use Python's built-in list functions to create a tic-tac-toe game

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def board():
    board_num_list = [1,2,3,4,5,6,7,8,9]
    return board_num_list

def board_draw(board):

    line1nums = board[0:3]
    line1nums.insert(1, " | ")
    line1nums.insert(3, " | ")
    line1list = line1nums
    line1str = ''.join([str(num) for num in line1list])
    print(line1str)

    sep = ('---------')
    print(sep)

    line2nums = board[3:6]
    line2nums.insert(1, " | ")
    line2nums.insert(3, " | ")
    line2list = line2nums
    line2str = ''.join([str(num) for num in line2list])
    print(line2str)

    print(sep)
    line3nums = board[6:9]
    line3nums.insert(1, " | ")
    line3nums.insert(3, " | ")
    line3list = line3nums
    line3str = ''.join([str(num) for num in line3list])
    print(line3str)

def valid(board, position):
    if str(board[position]).isnumeric():
        return True
    elif():
        return False

def mark_space(board,position,character):
    if valid(board, position) == True:
        board[position] = character.upper


def won_game(board):
    for x in board(0, 10, 3):
        line = board[x-3, x]
        if line.count('X') == 3:
            print("Player X won!")
            return True
        if line.count('Y') == 3:
            print("Player Y won!")
            return True




def game_over(board):
    if won_game(board):
        return True
    num_y = board.count('Y')
    num_x = board.count('X')
    if num_x + num_y == 9:
        return True



def instructions():
    print("Let's play Tic-Tac-Toe!")
    print("First, decide who is 'x' and who is 'o' and who will go first.")
    print("Pick a position, based on the numbered board below.")
    print("To make your move, type the numbered position with your lowercase character")
    print("Example of input: 2x")

def game():
    instructions()
    board()
    board_draw(board())
    move_input = eval(input("Player pick your position: "))
    move = move_input.split()

    while game_over(board()) == False:
        move_input = eval(input("Player pick your position: "))
        move = move_input.split()




def main():
    game()

    pass


main()
