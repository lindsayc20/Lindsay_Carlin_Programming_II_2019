'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

file = open('AliceInWonderland200.txt', 'r')

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

with open('dictionary.txt') as dictionary:
    dictionary_list = [x.strip() for x in dictionary]

def linear_search(key, dictionary):
    i = 0
    while i < (len(dictionary_list)) and key!= dictionary_list[i]:
        i += 1
    if i >= len(dictionary_list):
        print(key, "is not in the dictionary. It is in line", line_number)

def binary_search(key, dictionary):
   lower_bound = 0
   upper_bound = len(dictionary_list) - 1
   found = False
   while lower_bound <= upper_bound and not found:
       middle_pos = (lower_bound + upper_bound) // 2
       if dictionary_list[middle_pos] < key:
           lower_bound = middle_pos + 1
       elif dictionary_list[middle_pos] > key:
           upper_bound = middle_pos - 1
       else:
           found = True
   if not found:
       print(key, "is not in the dictionary. It is in line", line_number)

print("Linear Search")

words = []

line_number = 0
file = open('AliceInWonderLand200.txt')
for line in file:
    line_number += 1
    line_text = line.strip().upper()
    line_words = split_line(line_text)
    for word in line_words:
        words.append(word)
        linear_search(word.upper(), dictionary_list)
file.close()

file = open('AliceInWonderland200.txt', 'r')
print("")
print("Binary Search")
line_number = 0
for line in file:
    line_number += 1
    line_text = line.strip().upper()
    line_words = split_line(line_text)
    for word in line_words:
        words.append(word)
        binary_search(word.upper(), dictionary_list)

file.close()