# Press the green button in the gutter to run the script.
print("Hi this is the leap year test /n");
print("Enter a year to know if it is a leap year")
print("If you wish to quit the program, enter 'quit'")
boolean = True
while boolean:
    userInput = input("Enter the year or quit : ")
    if userInput == "quit":
        boolean = False
    elif userInput.isdigit():
        userInput = int(userInput)
        if (userInput % 4 == 0 or userInput % 400 == 0) and userInput % 100 != 0:
            print("This year is bisextile")
        else:
            print("This year is not bisextile")
    else :
        print("Sorry, you entered a wrong value")