'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

char_list = []
with open('dictionary.txt') as f:
    word_list = [x.strip() for x in f]

for word in word_list:
    char_list.append(len(word))
max_letters = max(char_list)
for i in word_list:
    if len(i) == 28:
        print("The longest word in the dictionary is", i + ". It has", max_letters, "letters.")

#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


alice_in_wonderland = open("AliceInWonderLand.txt")

word_list = []
for word in alice_in_wonderland:
    words = split_line(word.strip())
    for word in words:
        word_list.append(word)
lens_words = []
for word in word_list:
    lens_words.append(len(word))

print("There are", len(word_list), "words in 'Alice in Wonderland'. The average word in 'Alice in Wonderland is", sum(lens_words)/len(lens_words), "letters long.")

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

cheshire_counter = 0
cat_counter = 0
cheshire_cat_counter = 0
for i in range(len(word_list)):
    if word_list[i].upper() == "CHESHIRE":
        cheshire_counter += 1
    if word_list[i].upper() == "CAT":
        cat_counter += 1
    if word_list[i].upper() == "CHESHIRE" and word_list[i + 1].upper() == "CAT":
        cheshire_cat_counter += 1

print("The word 'cheshire' appears", cheshire_counter, "times.")
print("The word 'cat' appears", cat_counter, "times.")
print("The phrase 'cheshire cat' appears", cheshire_cat_counter, "times.")

#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



