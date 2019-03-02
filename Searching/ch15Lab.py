'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

'''
Write a single program in Python that checks the spelling of the first chapter of “Alice In Wonderland.” 
First use a linear search, then use a binary search. 
Print the line number along with the word that does not exist in the dictionary.
Follow the steps below carefully.
It is necessary to split apart the words in the story so that they may be checked individually. 
It is also necessary to remove extra punctuation and white-space. 
Unfortunately, there is not any good way of doing this with what the book has covered so far.
The code to do this is short, but a full explanation is beyond the scope of this class. 
Include the following function in your program. 
Remember, function definitions should go at the top of your program just after the imports. 
We'll call this function in a later step.
This code uses a regular expression to split the text apart. 
Regular expressions are very powerful and relatively easy to learn. 
To learn more about regular expressions, see: 
http://regexone.com/
Read the file dictionary.txt into an array. 
Go back to the chapter on Searching, or see the searching_example.py for example code on how to do this. This does not have anything to do with the import command, libraries, or modules. Don't call the dictionary word_list or something generic because that will be confusing. Call it dictionary_list or something similar.
Close the file.
Print --- Linear Search ---
Open the file AliceInWonderLand200.txt
We are not going to read the story into a list. 
Do not create a new list here like you did with the dictionary.
Start a for loop to iterate through each line.
Call the split_line function to split apart the line of text in the story that was just read in. 
Store the list that the function returns in a new variable named words. 
Remember, just calling the function won't do anything useful. 
You need to assign a variable equal (words) to the result. 
If you've forgotten now to capture the return value from a function, flip back to the functions chapter to find it.
Start a nested for loop to iterate through each word in the words list. 
This should be inside the for loop that runs through each line in the file. 
(One loop for each line, another loop for each word in the line.)
Using a linear search, check the current word against the words in the dictionary. 
Check the chapter on searching or the searching_example.py for example code on how to do this. 
The linear search is just three lines long. When comparing to the word to the other words in the dictionary, convert the word to uppercase. 
In your while loop just use word.upper() instead of word for the key. 
This linear search will exist inside the for loop created in the prior step. 
We are looping through each word in the dictionary, looking for the current word in the line that we just read in.
If the word was not found, print the word. 
Don't print anything if you do find the word, that would just be annoying.
Close the file.
Make sure the program runs successfully before moving on to the next step.
Create a new variable that will track the line number that you are on. 
Print this line number along with the misspelled from the prior step.
Make sure the program runs successfully before moving on to the next step.
Print --- Binary Search ---
The linear search takes quite a while to run. 
To temporarily disable it, it may be commented out by using three quotes before and after that block of code. 
Ask if you are unsure how to do this.
Repeat the same pattern of code as before, but this time use a binary search. 
Much of the code from the linear search may be copied, and it is only necessary to replace the lines of code that represent the linear search with the binary search.
Note the speed difference between the two searches.
Make sure the linear search is re-enabled, if it was disabled while working on the binary search.
Upload the final program or check in the final program.
'''

file = open('AliceInWonderland200.txt', 'r')

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('AliceInWonderLand200.txt', 'r')

for word in file:
    words = split_line(word.strip())
    for word in words:
        # print(word)

with open('dictionary.txt') as f:
    dictionary_list = [x.strip() for x in f]

file.close()

print("Linear Search")
open('AliceInWonderLand200.txt')
for line in 'AliceInWonderLand200.txt':
    split_line()


'''
# Linear Search
key = "Hitler" # what we are looking for
i = 0 # the index of the loop

while i < len(villain_list) and key != villain_list[i]:
    i += 1 # loop will stop when it finds "THE DEADLY RAVEN"

if i < len(villain_list):
    print("Found", key, "at position", i)
else:
    print("Could not find", key)

# Binary Search  --- he basically just played a game with us to demonstrate this point: https://www.geeksforgeeks.org/binary-search/
villain_list.sort()
print(villain_list)
key = "RENARD THE TORTURER" # "Save big money at Renard's" -Nicky Lerner

lower_bound = 0
upper_bound = len(villain_list) - 1
found = False
loops = 0 # counts the number of tries it too to find things
# with 2^7 loops, you can search 2^7 items in just 7 tries

# loop until we find it
while lower_bound <= upper_bound and not found:
    loops += 1
    middle_pos = (upper_bound + lower_bound) // 2
    if villain_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villain_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True
if found:
    print("\nFound", key, "at position", middle_pos, "with", loops, "loops")
else:
    print("Could not find", key, "after", loops, "loops")
'''