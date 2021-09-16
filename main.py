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

#pseudocode for the algorithm:

#in alpha order first. start with the first letter of word, and start indexing through the dict file. let's call the current line 'line'
#check each line for that char, and stop if it has it.
#if it stops (has the first char): change to checking line against word.
#take the first char of LINE, and check if WORD has it. in anagrams, letters can't be repeated, so if word has the letter, remove it from word temporarily.
#index through the rest of line, and keep checking of word has the letters.

#if it is ever FALSE, that means that the current line has a char that the word doesn't have, so it CAN'T be an anagram.
#reset the temp (letter-removed) word to the original
#go back to the beginning of the loop, grab a new line, and start testing the first char again

#if it is TRUE (meaning that all of the letters in line are in word, so it CAN be a part of the anagram):
#save the line (or at least the line number) in a variable
#rerun the loop, but with the trimmed down word this time (without the letters of the first saved line)

# - if at least one line is saved, BUT the trimmed down 'word' can't make any other words in the dictionary:
#move the original saved line (or line number) to a "do not use" variable
#reset word
#run the entire loop again, but skip over any lines in the "do not use" variable

#if the program takes all of the letters out of 'word' (meaning that it found a complete anagram, and 'word' is now empty):
#print out the saved words in order
#reset the word, run the entire loop over again to find another one (if the user/args specify)












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
