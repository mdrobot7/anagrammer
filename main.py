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
    print("Please put all arguments in one term. Exiting...")
    raise SystemExit
elif len(sys.argv) < 3:
    print("""Not enough arguments. Make sure to specify the string to anagram and the parameters,
or the string to anagram and a hyphen [-] if there are no parameters. Exiting...""")
    raise SystemExit

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
    lastWord = [_word] #lastword list

result = [] #words that are part of the anagram
c = [0] #a list of counter variables
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



#OPTIMIZATION NOTES/PSEUDOCODE:

#try file.readlines() instead of readline(), loading the entire thing into a list might make it faster
#after loading the file into a list, do a "rough cut" pass and list.pop() any elements that have "bad letters" (letters that are in the dict, but not in the anagram word)
#list.pop() any words that are longer than the anagram word

#after getting rid of as many extraneous words as possible, start with the first word, remove its chars from the anagram word, and anagram what is left
#i.e. if the word was "conversation" and the first word in the list was "ace", the result would be "onvrstion". then that would be anagrammed with the rest of the list.
#repeat, going down the list until it reaches the end

#I think the slowest parts of the code are the constant checking of letters in bad words, reading the data off of the drive instead of out of RAM, and the super large dict data set.
#the first two are solved by doing the "rough cut" and using file.readlines() into a list, but the last one would require deleting stuff from the dict.

#PROBLEM: As the dict is iterated over, every word will be slowly excluded from it. This is because if the word 'conversation' is the input, and the first two words are
#'ace' and 'son', but the remaining 'word' cannot form an anagram, the word 'son' will be excluded because it was second. the problem is that then, it will never be used
#as a first word. FIX THIS.

lines = dict.readlines() #read all lines into a list

while True: #"rough cut" of the dictionary - remove any dict words with "bad" letters
    if c[0] >= len(lines):
        break
    lines[c[0]] = lines[c[0]].strip("\n")
    if len(lines[c[0]]) == 1: #get rid of 1 character words
        lines.pop(c[0])
        continue
    for i in range(len(lines[c[0]])):
        if word.find(lines[c[0]][i]) < 0: #if the ii'th letter of the current line isn't in the word, delete the line from the dict and break the loop
            lines.pop(c[0])
            break
    else: #only increments the index if the for loop runs successfully
        c[0] += 1
c[0] = 0            
while True: #"fine cut" of the dictionary - remove any remaining dict words that don't work for other reasons (duplicate letters, etc)
    if c[0] >= len(lines):
        break
    for i in range(len(lines[c[0]])):
        if word.find(lines[c[0]][i]) >= 0:
            word = word[0:word.find(lines[c[0]][i])] + word[word.find(lines[c[0]][i]) + 1:] #if the letter is found, remove it.
        else:
            lines.pop(c[0])
            word = lastWord[0] #reset the word
            break
    else:
        c[0] += 1

#at this point, all words in 'lines' should work as a first word in the anagram.

print(lines)
print("")
print(len(lines))
print("")


c[0] = 0

while True:
    try:
        x = len(lines[c[len(result)]])
    except IndexError:
        print("EXCEPTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #print(len(lines[c[len(result)]]))
        #print(lines[c[len(result)]])
        print(c[len(result)])
        print(len(result))
        print(result)
        print(c)
        print(lastWord)
        print(failedFlag)
        print(c[len(result)] >= len(lines) - 1)
        raise SystemExit
    else:
        for i in range(len(lines[c[len(result)]])):
            if word.find(lines[c[len(result)]][i]) >= 0:
                word = word[0:word.find(lines[c[len(result)]][i])] + word[word.find(lines[c[len(result)]][i]) + 1:] #if the letter is found, remove it.
            else:
                failFlag = True
                break
        if failFlag:
            failedFlag = True
            failFlag = False
            if c[len(result)] >= len(lines) - 1: #if the counter reached the end of lines, aka reached the end of the dict (-1 offset because the ++ hasn't happened yet, in else)
                if len(result) > 0: #if a result can be removed, then remove it
                    while c[len(result)] >= len(lines) - 1: #go back to a counter that has space to count up
                        if len(result) > 0: result.pop()
                        else:
                            print("Complete.")
                            raise SystemExit
                        c[len(result)] += 1
                        c[len(result) + 1] = 0 #clear the now-vacated counter
                else:
                    print("No anagrams could be found, sorry!")
                    raise SystemExit
            else:
                c[len(result)] += 1
            word = lastWord[len(result)]
        elif not failFlag:
            failedFlag = False
            result.append(lines[c[len(result)]])
            if len(c) == len(result): c.append(0) #add another index to the counter list
            else: c[len(result)] = 0 #if the index exists, reset it.
            if len(lastWord) == len(result): lastWord.append(word)
            else: lastWord[len(result)] = word #if the index exists, use it
        if word == "": #if word is empty, meaning all of the letters have been taken out of it (used)
            print(result, end = " " )
            print(c)
            #print("")
            failFlag = False
            if "a" in sys.argv[2]:
                result.pop() #remove the last result to give space in the word
                lastWord.pop() #get rid of the empty string in the last index of lastWord
                word = lastWord[len(result)]
                c[len(result)] += 1 #move on to the next word
                if c[len(result)] >= len(lines): #if increasing the counter hits the end of the dict
                    result.pop() #get rid of the next result back in the list
                    lastWord.pop()
                    word = lastWord[len(result)]
                    c[len(result)] += 1
            else: #if the args don't specify to print all, then exit the program
                raise SystemExit