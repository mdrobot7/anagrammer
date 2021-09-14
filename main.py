# main
#Author: Michael Drobot
#https://github.com/mdrobot7

#Args: -p = profane; -a = all; -l = alphabetical order; -r = random order; -c = grammatically correct;

#Biggest challenge: Making a grammatically correct phrase.

#todo: if an anagram is a fail, clear the input word and retry, but with DIFFERENT dict words. So, find some way to track the dict words already used.

import time
import sys
import random

if len(sys.argv) > 2):
  print("Please put all arguments in one term. Press Ctrl+C to exit.")
  while True:
        time.sleep(0.5)

try:
    dict = open(dict.txt, 'r')
    prof = open(prof.txt, 'r') #combine the dict and prof files into one large file
except FileNotFoundError:
    print("Dictionary files not found!")
    raise SystemExit
  
word = sys.argv[1] #the word to be anagrammed
word = word.replace(" ", "") #get rid of all of the spaces














#======================================================================================================================================#

#lastWord = word #tracks the last instance of 'word' used

#result = [] #append values to the end of these to set stuff.
#usedWords = []
#lineCounter = -1

#if sys.argv[2].find("r") >= 0:
#    startLetterPos = random.randint(0, len(sys.argv[1]))
#else:
#    startLetterPos = 0
#startLetter = sys.argv[1][startLetterPos]

#while True:
#    lineCounter += 1
#    line = dict.readline()
#    if usedWords.index(lineCounter) >= 0: #if the current word/line is in the usedWords list, then skip it.
#        continue
#    if line.find(startLetter) == 0:
#        for i in line:
#            if word.find(line[i]) >= 0: #searches for the current letter of the dict file in the input word. the word should have all of the letters of the dict word.
#                word = word[0:word.find(line[i])] + word[word.find(line[i]) + 1:]
#            else:
#                word = lastWord
#                break
#        else: #will only run if the for loop finishes correctly
#            result.append(line)
#            dict.seek(0) #reset the readline at 0
#    if not word:
#        break
