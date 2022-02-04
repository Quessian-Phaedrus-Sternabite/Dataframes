# Functions are a great way to set up things you want to happen repeatedly.

def print_basic(text):
    print(text)
    print("\nNice!")


# All functions use whatever argument you give them and run an operation.
print_basic("Hello World")

# You can use return too to update variables!
a = 0
print(a)


# This function simply sets the argument give it to 3!

def x_update(arg1):
    arg1 = 3

    # Return simply updates the value of arg1, passing information back to the argument.
    return arg1


y = x_update(a)
print(y)

# Functions can be used for anything!

# Here is an example hangman guess program.

correct_word = "dog"
output = ['_', '_', '_']


# this function takes two arguments: a guess, and the actual answer

def guess_function(letter, answer):
    # x is set to zero to give a number to refer to that iterates with the loop
    x = 0

    # This for loop simply checks each letter of the answer argument, and if it is correct, changes the output at that
    # point to be that letter. If it is not correct, it does nothing.
    for i in answer:
        if letter == i:
            output[x] = letter
        x += 1

    # Using ''.join() can allow you to take a list and convert it to a string.
    display = "".join(output)

    # Print the display
    print(display)

    # This return probably isn't needed, as you're not updating the argument, but rather a preexisting 'global' variable
    return display


# This just calls the guessing function with letter and answer being their guess and the correct word.
guess_function(input("Enter a letter: "), correct_word)
