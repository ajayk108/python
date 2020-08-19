# from IPython.display import clear_output

'''creating the board....''' 
def display_board(board):
    print('\n'*10)
    print(''+board[1]+' | '+board[2]+' | '+board[3])
    print(''+board[4]+' | '+board[5]+' | '+board[6])
    print(''+board[7]+' | '+board[8]+' | '+board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# display_board(test_board)

''' player input '''
def player_input():
    marker = ''
    while not (marker =='X' or marker == 'O'):
        marker = input('Player 1: choose X or O :').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')   

# palyer1_marker, player2_marker =player_input()
# print(palyer1_marker)
# print(player2_marker)

'''positon number 1-9 assigns it to board  for X, O'''
def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board, '@', 8)
# display_board(test_board)

''' win check...........'''
def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark)or#top row
    (board[4] == mark and board[5] == mark and board[6] == mark)or# middle row
    (board[1] == mark and board[2] == mark and board[3] == mark)or#bottom row
    (board[7] == mark and board[4] == mark and board[1] == mark)or#first column
    (board[8] == mark and board[5] == mark and board[2] == mark)or#second column
    (board[9] == mark and board[6] == mark and board[3] == mark)or#third column
    (board[7] == mark and board[5] == mark and board[3] == mark)or#diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))#diagonal  

# display_board(test_board)
# res = win_check(test_board, 'X')
# print('\n')
# print(res)

''' which player goes first '''
import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'


'''wheter space in the board freely available or not.......'''
def space_check(board, position):
    return board[position] == ' '

'''if board is full return boolean value...'''
def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if we return true
    return True

''' players next position..............''' 
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('choose position:(1-9) '))

    return position

'''want to play again ..?? .....'''
def replay():
    choice = input('Play again ?  Enter Yes or No')

    return choice == 'Yes'

'''while loops and function to run the GAME //////////////////////////////////////////////'''
print('welcome to the game......')

while True:
    #play game
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first...')

    play_game = input('Ready to play? y or n ? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    #game play....
    while game_on:
        
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has OWN..!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE Game...!!!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has OWN..!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE Game...!!!')
                    break
                else:
                    turn = 'Player 1'
                
        
    if not replay():
        break
            
            
    
