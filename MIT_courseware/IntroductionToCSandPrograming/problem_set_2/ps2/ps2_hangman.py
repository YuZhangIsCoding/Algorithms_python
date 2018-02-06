# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def hangman(myword, letters, myguess, count):
    '''hangman(myword, letters, myguess, count)
    myword:             string
    letters, myguess:   list of letters
    count:              int
    '''
    print '-'*10
    if count == 0:
        print 'You\'ve run out all of guesses, you lose!'
        return None
    elif count == 1:
        print 'You have 1 guess left.'
    else:
        print 'You have %d guesses left.' %count
    print 'Available letters: %s' %(''.join(letters))
    guess = raw_input('Please guess a letter:')
    if guess not in letters:
        print 'You\'ve used %s before, please select another letter' %guess
    letters.remove(guess)
    if guess in myword:
        for i, item in enumerate(myword):
            if guess == item:
                myguess[i] = item
        print 'good guess: %s' %(''.join(myguess))
    else:
        count -= 1
        print 'Oops! That letter is not in my word: %s' %(''.join(myguess))
    if ''.join(myguess) == myword:
        print '_'*10
        print 'Congratulations, you won!'
    else:
        hangman(myword, letters, myguess, count)
myword = choose_word(wordlist)
print 'Welcome to the game Hangman!'
print 'I am thinking of a word that is %d letters long' %len(myword)

count = 8
myguess = [' _' for row in range(len(myword))]
letters = map(chr, range(97, 123))
hangman(myword, letters, myguess, count)
        

