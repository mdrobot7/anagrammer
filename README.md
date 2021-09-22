# anagrammer
A quick Python program that takes a word or phrase and some parameters and generates an anagram of it.

The word lists are from the SCOWL (and Friends) project, and they can be found here: http://wordlist.aspell.net/ . The main dictionary file is the combination of the English and American English files, with a complexity/frequency of 0-70. They were assembled by me, and sorted alphabetically in Windows Command Prompt. The `dictionary-profane.txt` list is the same as the `dictionary.txt` list, but with all of the words in the profane SCOWL dictionaries.

The dictionaries are completely open, so if the user wants to modify them to exclude certain words, include other ones that aren't already present, or modify them in any way, they can. The program will still work, as long as the two text files `dictionary.txt` and `dictionary-profane.txt` exist (in **any** form) in the directory. The dictionaries *are* case-sensitive, however, they must be all lower-case for the program to work (It will run if this is not the case, but it will not give an output).

## Usage
Run this program using Python 3.x in Terminal/Windows Command Prompt.

Linux: `python3 main.py <input-word> <args>`
Windows: `py main.py <input-word> <args>`

Arguments:
- `-a`: Outputs all anagram results
- `-r`: Outputs a single random result
- `-p`: Profane -- includes the profane words/uses the profane dictionary in addition to the main one
- `-o`: File to output results to. Use in a separate argument. (Usage Ex.: `python3 main.py -a -o output.txt`

If <input-word> ends in `.txt`, the program will search for an input text file with the name <input-word>. It will then use that as the input.
