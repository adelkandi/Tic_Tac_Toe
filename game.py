##### Define game ####
import time
#import player file :
from Player import HumanPlayer,RandomComputerPlayer
#difine class TicTacToe:

from numpy import diagonal, square

from Tic_Tac_Toe_Game.Player import HumanPlayer


class TicTacToe:
    def __init__(self) :   #we need a board 
        self.board = [' ' for _ in range(9)]    #we make a Board and we will use single list to rep 3x3 board
        self.current_winner= None   # keep track winner 

    def print_board(self):     #Priniting the board graph:
        # this is just getting row 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: 
            print('| '+'|'.join(row)+' |')
    

    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc (tell  us what number correspond to what box)
        numb_board=[[str(i) for i in range(j*3 , (j+1)*3)] for j in range(3)]  # the number need to be string so we will not have any error, we make too an row j
        for row in numb_board:
            print('| '+'|'.join(row)+' |')
    #we need to know the availble moves so we will creat def to control moves 


    def available_moves(self):
        return[ i for i, spot in enumerate(self.board) if spot == ' ']
        #return[] expend this out another methode ... but we will use the fastes way 
        #moves = []   this is the classic way :

        #for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2,'o')] we will use this tuples
            #if spot == ' ':
                #moves.append(i)  # we gona have index of that spot to move 
            #return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ') # count how many spots we have 

    def make_move(self, square, letter):
        # if valid move, then make the move ( assign square to letter)
        # then return true . if invalid, return false
        if self.board[square]== ' ' :
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square , letter):
        # winner of 3 in a line " row anywhere ..." we have to check all of these
        # first lets check the row 
        row_ind = square // 3  
        row= self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot==letter for spot in row ]):
            return True
        # check the column 
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range (3)]
        if all([spot== letter for spot in column]):
            return True
        
        # check diagonals
        # but only if the square is an even number (0, 2, 4, 8)
        # these are only moves possible o win diagonal
        if square % 2==0:
            diagonal1= [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot== letter for spot in diagonal1]):
                return True
            diagonal2= [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot== letter for spot in diagonal2]):
                return True
        
        # if all of this fail
        return False








#lets define a function called play :

def play(game, x_player, o_player, print_game=True):
    #return the winnner of the game( the letter) or None for a tie 
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # staring letter 
    # interate while the game still has empty squares
    # we dont have to worry about winner because we will just return that 
    # which breaks the loop

    while game.empty_squares():
        #get the move from the appropriate player 
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game) 

        # lets define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to a square {square} ')
                game.print_board()
                print('') # just empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!!!')
                return letter

                
            #after we made our move we need to alternative letters
            letter = 'O' if letter == 'X' else 'X' # switches player

        # tiny break to make things little bit easier to read
        time.sleep(0.8)

    if print_game:
        print('Its a tie')

        
########################################################
if __name__=='__main__':
    x_player = HumanPlayer('X') # import humanplayer from player file 
    o_player = RandomComputerPlayer('O') # import RandomComputerPlayer
    t= TicTacToe()
    play(t, x_player, o_player, print_game=True)
    







    








            







        
