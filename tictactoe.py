
# Initialising the game board to empty strings
board = {
    '1': '  ', '2': '   ', '3': '  ',
    '4': '  ', '5': '   ', '6': '  ',
    '7': '  ', '8': '   ', '9': '  '
}

# The x for the left and right columns 
LRx = ' X'
# The x for the centre column
Cx = ' X '
# The o for the left and right columns 
LRo = ' O'
# The o for the centre column
Co = ' O '


boardEnd = '------------------------------------'


# Prints the board showing the numbers for the input
print(' 1 | 2 | 3 ')
print('---+---+---')
print(' 4 | 5 | 6 ')
print('---+---+---')
print(' 7 | 8 | 9 ')
print(boardEnd)

# Player 1 starts
player = 1
# Symbol is X for Player 1
symbol = 'X'
# The number of plays (cannot be greater than 9)
moves = 0

# Switch symbol depending on the player (1 = X, 2 = O) 
if player != 1:
    symbol = 'O'

while True:
    
    if moves > 8:
        print('9Moves')
        break

    while player == 1:

        if moves > 8:
                print('9Moves')
                break

        print(board['1'] + ' |' + board['2'] + '|' + board['3'])
        print('---+---+---')
        print(board['4'] + ' |' + board['5'] + '|' + board['6'])
        print('---+---+---')
        print(board['7'] + ' |' + board['8'] + '|' + board['9'])

        # Take input for the number of the square to
        ip = input('Player 1:\n')
        moves += 1

        # Try getting input: if it is between 1 & 9, 
        try:
            if ip in board and board[ip] == '  ' or board[ip] == '   ':

                # Check to see which 'X' to insert (LRx or Cx)
                if ip == '2' or ip == '5' or ip == '8':
                    board[ip] = Cx

                    # Check if the board is full 
                    if moves > 8:
                        break

                    # Change player
                    player = 2 
                    print(boardEnd)
                else:
                    board[ip] = LRx

                    # Check if the board is full 
                    if moves > 8:
                        break

                    # Change player
                    player = 2   
                    print(boardEnd)

            # Check if that box is taken 
            elif board[ip] == ' X' or board[ip] == ' X ' or board[ip] == ' O' or board[ip] == ' O ':
                print('That spot is taken')
                moves -= 1

        # If the input is not from the board (1-9)
        except KeyError as identifier:
            print('INVALID')
            moves -= 1
            break
        
    while player == 2:

        print(board['1'] + ' |' + board['2'] + '|' + board['3'])
        print('---+---+---')
        print(board['4'] + ' |' + board['5'] + '|' + board['6'])
        print('---+---+---')
        print(board['7'] + ' |' + board['8'] + '|' + board['9'])

        # Take input for the number of the square to
        ip = input('Player 2:\n')
        moves += 1



        # Try getting input: if it is between 1 & 9, 
        try:
            # Check if that box is empty
            if ip in board and board[ip] == '  ' or board[ip] == '   ':

                # Check to see which 'O' to insert (LRo or Co)
                if ip == '2' or ip == '5' or ip == '8':
                    board[ip] = Co

                    # Check if the board is full 
                    if moves > 8:
                        break

                    # Change player
                    player = 1 
                    print(boardEnd)
                else:
                    board[ip] = LRo

                    # Check if the board is full 
                    if moves > 8:
                        break

                    # Change player
                    player = 1  
                    print(boardEnd)

            # Check if that box is taken 
            elif board[ip] == ' X' or board[ip] == ' X ' or board[ip] == ' O' or board[ip] == ' O ':
                print('That spot is taken')   
                moves -= 1     


        # If the input is not from the board (1-9)
        except KeyError as identifier:
            print('INVALID')
            moves -= 1
            break


print('TIE')
