# main
#Author: Michael Drobot
#https://github.com/mdrobot7

#Args: -p = profane; -a = all; -l = alphabetical order; -r = random order; -c = grammatically correct;

#Biggest challenge: Making a grammatically correct phrase.

import time
import sys
import random

if len(sys.argv) > 2):
  print("Please put all arguments in one term. Press Ctrl+C to exit.")

try:
    dict = open(dict.txt, 'r')
    prof = open(prof.txt, 'r') #combine the dict and prof files into one large file
except FileNotFoundError:
    print("Dictionary files not found!")
  
word = sys.argv[1] #the word to be anagrammed
word = word.replace(" ", "") #get rid of all of the spaces

#dict.readlines() #this might be bad, since it loads all lines of the file into a list (memory). That would be a lot of RAM...

if sys.argv[2].find("r") >= 0:
    while True:
        startLetterPos = random.randint(0, len(sys.argv[1]))
        startLetter = sys.argv[1][startLetterPos]
        line = dict.readline()
        if line.find(startLetter) == 0:
            #pseudocode:
            #take the current dict word/line, and see if the next letter in the line is present in word. repeat until you get a no, and then increment the word/line.
            while True:
                for i in word:
                    if line.find(word[i]) >= 0:
                        word = word[0:i] + word[i + 1:]
                        
        else:
            continue
