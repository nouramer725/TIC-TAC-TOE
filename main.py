# It implements a simple game of Tic-Tac-Toe where the computer player uses the minimax algorithm to make its moves.
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


# This printBoard function takes a dictionary board as input and prints the current state of the Tic-Tac-Toe board.
# It uses string concatenation and formatting to display the board structure.
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


# spaceIsFree(position): This function checks if a space on the board is free ('X' or 'O').
# It takes a position as input, which represents a key in the board dictionary.
# If the space is free, it returns True; otherwise, it returns False.
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


# checkForWin(): This function checks if there is a winning combination on the board.
# It checks all possible winning combinations by comparing the values of the corresponding board positions.
# If any winning condition is met, it returns True; otherwise, it returns False.
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


# checkDraw(): This function checks if the game has ended in a draw.
# It iterates over all positions on the board and checks if any space is still empty (' ').
# If there is an empty space, it returns False; otherwise, it returns True to indicate a draw.
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

# insertLetter(letter, position): This function inserts a letter ('X' or 'O') into a specified position on the board.
# It first checks if the space is free by calling the spaceIsFree(position) function.
# If the space is free, it updates the board with the given letter at the specified position and then calls printBoard(board) to display the updated board.
# It also checks for a draw or win condition by calling checkDraw() and checkForWin() functions, respectively.
# If a draw or win is detected, it prints the corresponding message and exits the program.
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("entet new position "))
        insertLetter(letter, position)
        return

# checkWhichMarkWon(mark): This function is similar to checkForWin(), but it checks if a specific mark ('X' or 'O') has won the game.
# It takes a mark as input and returns True if the mark has won; otherwise, it returns False.
def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


# playerMove(): This function prompts the player to enter a position where they want to place their 'O' mark.
# It takes input from the user and calls the insertLetter(player, position) function to update the board.
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


# compMove(): This function represents the computer's move.
# It uses the minimax algorithm to determine the best move for the computer.
# It iterates over all possible moves on the board, simulating each move and evaluating the score using the minimax() function.
# It then selects the move with the highest score and calls insertLetter(bot, bestMove) to update the board.
def compMove():
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

# minimax(board, depth, isMaximizing): This is the main function implementing the minimax algorithm.
# It recursively evaluates all possible moves and assigns scores to them.
#It considers three possible outcomes: the computer wins (returns 1), the player wins (returns -1), or it's a draw (returns 0).
# The function alternates between maximizing and minimizing the scores based on the isMaximizing parameter.
# The depth parameter is used to keep track of the recursion depth.
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


# board: This is a dictionary representing the Tic-Tac-Toe board.
# The keys are the positions on the board, and the values are the corresponding marks ('X', 'O', or ' ') representing the current state of the board.
printBoard(board)
player = 'O'
bot = 'X'
while not checkForWin():
    compMove()
    playerMove()