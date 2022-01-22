# Player Script #

import math         # we need to import math library first 
import random       # we need to import random 

from cv2 import dnn_DetectionModel
from numpy import square       


# Based Player class :
class Player:
    def __init__(self, letter):           #  Thism class to difine the name of player in game 
        # letter is x or o
        self.letter = letter
    # we want all players to get their next move
    def get_move(self, game):     # we created the function get_move so we can let player move
         pass 

#init= initionalazation

# Based Random Computer player class
class RandomComputerPlayer(Player):

    def __init__(self, letter) :
        super().__init__(letter)  # call in super class "player"

    def get_move(self, game):
        square = random.choice(game.available_moves()) 
        return square
        

# Based Human Player class :
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):      
        valid_square= False
        val=None
        while not valid_square:
            square= input(self.letter + '\'s turn. Input move(0-8):')
            # we're going to check that tis is correct value by trying to cast
            # it to an int , abd if its not , then we say its invalid 
            # id that spot is not available on the board, we also say its invalid 
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square= True # if these are seccessful , then good...
            except ValueError:
                print('Invalid square. Try again.')
        
        return val 

        
        

     
    
















 



        


