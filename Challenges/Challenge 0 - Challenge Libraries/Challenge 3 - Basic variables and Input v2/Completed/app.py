# Place code in this function:
def requestInformation():
    name = input("What is your name? ")
    age = input("What is your age? ")
    career = input("What is your goal career field? ")
    salary = input("What is your goal salary? ")
    gatheredInformation = "My name is " + name + ". My age is " + age + ". My goal career field is " + career + " and my goal salary is $" + str(salary) + " annually."
    print()
    print(gatheredInformation)

# Main Function - Do not worry about editing:
if __name__ == "__main__":
    requestInformation()
