#  Challenge Two: Basic Strings and Input
# 
#   The goal of this challege is to create two variables. One named name and one named greeting.
#   Use the input method with the name variable to ask the user what their name is.
#   Use the greeting variable to concatenate strings with the name variable to say:
#   Hello, user.
#   Use the print method to print the greeting to the terminal.

def requestName():
    name = input("What is your name? ")
    greeting = print(f"Hello, {name}.")
# fill out challenge code here

# main method -- do not worry about editing
if __name__ == "__main__":
    requestName()