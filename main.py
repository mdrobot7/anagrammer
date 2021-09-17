# main
#Author: Michael Drobot
#https://github.com/mdrobot7

#Args: -p = profane; -a = all; -l = alphabetical order; -r = random order; -c = grammatically correct;

#Biggest challenge: Making a grammatically correct phrase.

#todo: if an anagram is a fail, clear the input word and retry, but with DIFFERENT dict words. So, find some way to track the dict words already used.

import time
import sys
import random

if len(sys.argv) > 3:
  print("Please put all arguments in one term. Press Ctrl+C to exit.")
  while True:
        time.sleep(0.5)

try:
    dict = open("dictionary.txt", 'r')
    #prof = open(profane.txt, 'r') #combine the dict and prof files into one large file
except FileNotFoundError:
    print("Dictionary files not found!")
    raise SystemExit
  
_word = sys.argv[1] #the word to be anagrammed
if _word[-4:] == ".txt": #if the last 4 chars are .txt
    try:
        _word = open(_word, 'r') #implement this later
    except FileNotFoundError:
        print("Text file not found!")
        raise SystemExit
else:
    _word = _word.replace(" ", "") #get rid of all of the spaces
    word = _word
    lastWord = _word

result = [] #words that are part of the anagram
excluded = [] #words that can't be part of the anagram (because if they are chosen, then the anagram can't be finished)
failFlag = False

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


while True:
    failFlag = False
    line = dict.readline()
    line = line.strip() #remove newlines and spaces
    if line == "": #if line is an empty string, meaning it reached the end of the file
        if len(result) > 0:
            excluded.append(result.pop()) #removes the last value (the most recent value can't be used, because it prevents the next part of the anagram from being made), excludes it
            word = lastWord + excluded[-1] #concatenates the lastWord and the newly excluded word to "undo" the subtraction of the excluded word (since it doesn't work)
            lastWord = word #reset lastWord
        else:
            print("No anagrams could be found. Sorry!")
            break
        dict.seek(0) #bring the seek back to the beginning
        print("asdfasdf")
        failFlag = True
        continue
    for i in range(0, len(excluded)): #check that the current line isn't in the excluded list
        if line == excluded[i]:
            failFlag = True
            break
    if line.find(word[0]) >= 0 and not failFlag and len(line) > 1: #can also use if word[0] in line
        for i in range(len(line)):
            if word.find(line[i]) >= 0:
                word = word[0:word.find(line[i])] + word[word.find(line[i]) + 1:] #if the letter is found, remove it.
            else:
                failFlag = True
                break
        if failFlag:
            word = lastWord #reset the word
        elif not failFlag: #if the for loop finished correctly, and the current 'line' can be part of the anagram
            lastWord = word
            result.append(line) #add the current word to the results array
            dict.seek(0)
            print("Word successful!")
            print(line)
            print(word)
            print("")
        if word == "": #if word is empty, meaning all of the letters have been taken out of it (used)
            print(result)
            break
