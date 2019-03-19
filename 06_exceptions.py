# Exception
# if the try works, great
# if it doesn't do the except
try:
    val = int(input("Enter a number: "))
except:
    print("You entered an invalid number")

# Error types
# ValueError
try:
    val = float(input("Enter a number: "))
except ValueError:
    print("You entered an invalid number")

# ZeroDivisionError
try:
    y = 5 / 0
except ZeroDivisionError:
    print("Zero Division Error!")

# I/O Errors  - FileNotFoundError
try:
    my_file = open("some_file.txt")
    for line in my_file:
        print(line)
except FileNotFoundError:
    print("File not found")

# Identifying errors
try:
    #y = 1 / 0
    int("A")
except Exception as e:
    print("Error found:", e)

# Multiple error types
try:
    y = 1 / 0
    #int("A")
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("zero division")
finally:
    print("This code always runs.")

# Make an MPG calculator

done = False

while not done:
    try:
        miles = float(input("Miles: "))
        gal = float(input("Gallons: "))
        done = True
    except ValueError:
        print("Please enter valid numbers")

try:
    mpg = miles / gal
    print("MPG:", mpg)
except ZeroDivisionError:
    print("You have infinite mpg.")