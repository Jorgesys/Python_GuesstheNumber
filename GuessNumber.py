
#created by Jorgesys for any comment write to : tuna.puisor@gmail.com

import simplegui
import random
import math

# "Guess the number game in Python!" 
# based on Binary Search algorithm http://en.wikipedia.org/wiki/Binary_search_algorithm
def new_game(my_range):
    print ("")
    print ("New game. Range is from 0 to ", my_range)
    global secret_number 
    global guesses_total
    global guesses_made
    global current_range
    current_range = my_range
    guesses_made = 0
    guesses_total = math.ceil(math.log(my_range, 2))
    secret_number =  random.randrange(0, my_range)
    print ("You have " + str(guesses_total)  + " guesses")
    
def range10():
    new_game(10)    
    
def range100():
    new_game(100)

def range1000():
    new_game(1000)
    
def input_guess(guess):
    global guesses_made
    guesses_made += 1
    guesses_remaining = guesses_total - guesses_made    
  
    iguess =  int(guess)
    if(secret_number> iguess):
        print ("Higher")
        print ("")
    elif(secret_number< iguess):
        print ("Lower")
        print ("")
    else:
        print ("Correct!")
        print ("Guess was ", secret_number)
        new_game(current_range)
        return
   
    if(guesses_remaining == 0):
       print ("You ran out of guesses.  The number was ", secret_number)
       new_game(current_range)               
       return
    else:
        print ("Number of remaining guesses is ", guesses_remaining)        
        
        
frame = simplegui.create_frame("Guess the number", 300, 300)
frame.add_input("Input Guess!", input_guess, 200)
frame.add_button("Range: 0 - 10" ,range10, 200)
frame.add_button("Range: 0 - 100" ,range100, 200)
frame.add_button("Range: 0 - 1000" ,range1000, 200)
frame.start()


new_game(100)

