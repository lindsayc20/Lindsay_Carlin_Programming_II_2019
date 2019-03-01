import random

# PROBLEM 1 (Fibonacci)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

fibonacci_numbers = []
fibonacci = 0
fibonacci_minus_two = 1
fibonacci_minus_one = 1

while fibonacci < 1000:
    fibonacci = fibonacci_minus_one + fibonacci_minus_two
    fibonacci_numbers.append(fibonacci)
    fibonacci_minus_two = fibonacci_minus_one
    fibonacci_minus_one = fibonacci

print(fibonacci_numbers)

# PROBLEM 2 (Dice Sequence)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

'''
dice_rolls = []
success = 0
failure = 0
for i in range(100):
    dice_roll = []
    for j in range(5):
        die = random.randrange(1, 7)
        dice_roll.append(die)
    dice_rolls.append(dice_roll)
    for k in range(len(dice_rolls)):
        for l in range(len(dice_rolls[k])):
            if dice_roll[k] > dice_roll[k-1]:
                success += 1
            else:
                failure += 1
print(success/(success+failure))

'''



# PROBLEM 3 (Number Puzzler)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.


'''
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                print("abcd")
'''