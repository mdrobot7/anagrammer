# main
#Author: Michael Drobot
#https://github.com/mdrobot7

#Args: -p = profane; -a = all; -r = random order; -c = grammatically correct; -f = file to output results to

#Biggest challenge: Making a grammatically correct phrase.

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

if "r" in sys.argv[2] and "a" in sys.argv[2]:
    print("Random and All arguments are mutually exclusive. Exiting...")
    raise SystemExit

try:
    dict = open("dictionary.txt", 'r')
    if "p" in sys.argv[2]: #if profane is in the args
        dict = open(profane.txt, 'r') #combine the dict and prof files into one large file
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

c[0] = 0
if "r" in sys.argv[2]:
    c[0] = random.randint(0, len(lines))

while True:
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
        if "r" in sys.argv[2]: c[len(result)] = random.randint(0, len(lines)) #if a random anagram is specified, randomize the indexer
        if len(lastWord) == len(result): lastWord.append(word)
        else: lastWord[len(result)] = word #if the index exists, use it
    if word == "": #if word is empty, meaning all of the letters have been taken out of it (used)
        print(result)
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
