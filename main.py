# main
#Args: -p = profane; -a = all; -l = alphabetical order; -r = random order; -c = grammatically correct;

#Biggest challenge: Making a grammatically correct phrase.

import time
import sys
import random

if len(sys.argv) > 2):
  print("Please put all arguments in one term. Press Ctrl+C to exit.")

try:
  dict = open(dict.txt, 'r')
  prof = open(prof.txt, 'r')
except FileNotFoundError:
  print("Dictionary files not found!")
  
word = sys.argv[1] #the word to be anagrammed

#dict.readlines() #this might be bad, since it loads all lines of the file into a list (memory). That would be a lot of RAM...

if sys.argv[2].find("r") > 0:
    startLetter = sys.argv[1][random.randint(0, len(sys.argv[1]))]
    
