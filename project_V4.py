# final project - mud monster game
import random
import time
win=False
#Version 4
# first we define some functions that we will use in this program
#Four of these are already coded. They are choosesecretword(wordlist), getprintversion(secretword,lettersguessed), getguess(lettersguessed) and printrules(). 

# choose the secret word
def choosesecretword(wordlist):

    secretelement=random.choice(wordlist)
    return secretelement

# check if argument is a valid character

# getguess will ask the user to guess a letter 
# the argument lettersguessed contains all the letters guessed so far
letters=[]
# if the user guesses a letter that they have already guessed or guesses something that is
# not a valid character, they are prompted to guess again
def getguess():
#    while True:
    guess=input("Are you ready? Enter a single letter")
    guess=guess.lower()
#        lettersguessed=guess
    if guess in letters:
        print("Already guessed")
#           continue
#        letters=[]
        letters.append(guess)
    return guess
# getprintversion will get the print version of the secret word.  
# If a letter in the word is already guessed, that letter will be printed
# If a letter in the word is not guessed, a * will be printed in that place
def getprintversion(secretword):
    display=""
    for letter in secretword:
        if letter in secretword:
            display=display+guess
        else:
            display=display+"*"
    return display
    # printrules will print the rules of the game
"""def printrules():
    print("Helow! Welcome to the word guessing game! I am the mud monster!")
    time.sleep(0.5)
    print("I've chosen a random word. You'll have to enter a single character")
    time.sleep(0.5)
    print("I will tell you  the number of characters that word contains by replacing each character with a *. ")
    time.sleep(0.5)
    print("If your guess is correct, I'll replace * with that letter and print it for you. ")
    time.sleep(0.5)
    print("You will get 6 chances to guess my secret word. ")
    time.sleep(0.5)
    print("If you guess a wrong character, I will cover a part of your body with mud! If you lose all chances, you'll be fully covered with mud!")"""

# print error message
def printmud():
    pass
    
# start of the main program
#printrules()

#initializations
#wordlist1 = ['independence','freedom','fighters','holiday','flag','india','august','british','nation','july','celebration']
file=open("movies.txt")
wordlist=file.read().split("\n")
print(wordlist)

#getguess()
word=choosesecretword(wordlist)
#start your code here
#input()

def hint():
    pass
userword=""
def error_message():
    playerChoice=getguess()
    while win==False:
        if playerChoice in word:
#            pass
            userword+=playerChoice
        else:
            print("Sorry, the letter you chose is not in the chosen word.")
        if userword==word:


error_message()
#Also need to change getprintversion so that it prints the word partially
#HW for PRanav: Read up on sets, any function