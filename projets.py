#1 --- MADLIBS
#strings concatenation; how to put strings together
#suppose we want to create a sting that says "subscribe to my youtube channel"
'''youtuber = "my youtube channel" # some string variable

# a few ways to do this
print("subscribe to {}".format(youtuber))
print(f"subcribe to {youtuber}")
print("subscribe to " + youtuber)'''

#2 -- GUESS THE NUMBER(computer); where the computer has a secret number for us to guess
'''import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number netween 1 and {x}: '))
        if guess < random_number:
            print('sorry, guess again. Too low')
        elif guess > random_number:
            print('sorry, guess again. Too High')
            
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')'''
        
'''#3 -- GUESS THE NUMBER(USER); where the user has a secret number for the computer to guess
import random
def computer_guess(x):
    low = 1 
    high = x   
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L), correct(C)???').lower()
        if feedback == "h":
            high = guess - 1 
        elif feedback == "l":
            low = guess + 1   
    
    print(f'Yay!!! The computer guessed your number, {guess}, correctly!')     
  
computer_guess(100)'''  
        
        
#4 --- ROCK PAPER SCISSORS:its rather simple but just a step-up of the previous example
'''import random

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return("It's a tie")
    
    #r > s, s > p, p > r
    if is_win(user, computer):
        return("You won")
    
    return "You lost!"

def is_win(player, opponent):
    #return true if player wins
    #r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())'''


'''#5 --- HANGMAN
import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    # getting user input
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        user_letter.add(user_letter)
        if used_letter in word_letters:
            word_letters.remove(user_letter)
            
    elif user_letter in used_letters:
        print('You have already used the character. Please try again later')
    
    
user_input = input('Type something:')
print(user_input)'''


'''#8 --- Binary Search: 
# Implementation of binary search algorithm!!
 
# we will prove that binary search is faster than native search!
 
# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, return 1
import random
import time


def naive_search(l, target):
    
    for i in range(len(l)):
        if l[i] == target:
            return i
        return -1
   
# binary search uses DIVIDE & CONQUER!
# we will leverage the fact that our list is SORTED in order to make our search faster
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    if high < low:
        return -1
    
    # example l = [1,3,5 10, 12] # should return 3
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint 
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high) 
    
if __name__ =='__main__':
    #l = [1, 3, 5, 10, 12]
    #target = 12
    #print(naive_search(l, target))
    #print(binary_search(l, target))
    
    length = 10000
    # build a Random sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list  = sorted(list(sorted_list))
    
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:", (end - start)/length, "seconds")
    
    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:", (end - start)/length, "seconds")'''
    
    
'''#9 -- MINESWEEPER
import random
import re
# lets create a board object to represent the MINESWEEPER game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later on
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # let's create the board
        self.board = self.make_new_board() #plant new bomb
        self.assign_values_to_board()
        
        # initialize a set to keep track of which location we've uncovered
        #we'll save (row,col) tuples into this set
        self.dug = set() #if we dig at 0, 0, then self.dug = (0, 0)
        
    def make_new_board(self):
        # construct a board based on the dim_size and num_bombs
        # we should construct the list of lists here (for whatever representation you prefer,
        # but since we have a 2-0 board, list of lists is most natural)
        
        # generate a new board
        board = [[None for _ in range(self.dim_size) for _ in range(self.dim_size)]]
        #this creates an array like this:
        # [None, None, ..., None],
        # [None, None, ..., None],
        # [...
        # [None, None, ..., None]
        # we can see how this represent a board!
        
        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size # We want the number of times dim_size goes into loc to tell us 
            col = loc % self.dim_size # We want the Remainder to tell us what index in that row to locate 
            
            if board[row][col] == '*':
                # this means that we've actually planted a bomb there already so keep going
                continue
            
            board[row][col] == '*'  # plant the bomb
            bombs_planted += 1
            
        return board
        
    def assign_values_to_board(self):
        # now that we have palnted the bombs, let;s assign a new number 0-8 for all the empty spaces, which 
        # represents how many neighboring bombs are there. we can precompute these and it'll save us some
        # effort checking what's around the board later on:) 
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue 
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
                
    def get_num_neighboring_bombs(self, row, col): 
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)
        
        # make sure to not go out of bounds!
        
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+ 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+ 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
                    
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if succesful dig, false if bomb dig
        
        #a few scenerios
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at the spot/that location with no neighboring bombs -> recursively dig neighbors
        
        self.dug.add(row, col) # keep track that we dug here
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+ 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+ 1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)
                
        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb here        
        return True
                
    def __str__(self):
        # this is a magic function where if you call printon this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player
        
        # first let's create a new array that represents what the user world see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                    
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'
            
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len
        
        return string_rep
    
#Play the  game
def play(dim_size=10, num_bombs=10):
    # step1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    # step 2: show User the board and ask for where they want to play/ Dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location isn't a bomb, dig recursively until each square is at least next to a bomb
    # step 4: repeat step 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        
        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhhh
            break # (game over rip)
        
    # 2 ways to end a loop, let's check which one
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS")
    else:
        print("SORRY GAME OVER: (")
        # let's reveal the whole board:
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
        
if __name__ == '__main__': # good character
    play()'''
    
    
# 10 --- SUDOKU 
def find_next_empty(puzzle):
    #find the next row, col on the puzzle that's not filled yet --> rep. with -1
    #return row, col tuple for (None. None) if there is none
    
    # keep in mind thatr we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is  0,1,2, ... 8
            if puzzle[r] == -1:
                return r, c

    return None, None   
 
def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # return True if its valid, false otherwise
    # 
    
    # let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now the columm
    #col_vals = []
    #for i in range(9):
    #   col_vals.append(puzzle[i][col] 
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False     
    
    # and then the square
    # this is tricky, but we want to get where the 3x3 square starts
    # amd iterate over the 3 values in the row/column
    row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3 
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # if we get here, theses checks pass
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution 
    
    # step1: choose somewhere on the puzzle to take a quess
    row, col = find_next_empty(puzzle)
    
    # step1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    #step2: if there is a place to put a number, then make aguess between 1 to 9
    for guess in range(1, 10):  # range(1, 10) is 1,2,3,... 9
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3: if this is valid, then place the guess on the puzzle!
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to 
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess
        
    # step 6: if none of the numbers that we try work, then this puzzle is unsolvable!!!
    return False

if __name__ == '__main__':
    project_board = [
        [3, 9, -1,  -1, 5, -1   -1, -1, -1],
        [-1, -1, -1,  2, -1, -1   -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,   -1, 8, -1],
        
        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],
        
        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(project_board))
    print(project_board)
    

