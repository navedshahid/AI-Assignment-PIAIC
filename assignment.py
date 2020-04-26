# while True:
print("Assignment by PIAIC121574")
number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
calc = input("Enter calculation sign to be performed example + for addition, - for subtraction, * for multiplication and / for division")
if calc == "+":
    print(number1 + number2)
elif calc == ("*"):
    print(number1 * number2)
elif calc == "-":
    print(number1 - number2)
elif calc == "/":
    if number2 < 0:
        print("Cannot divide by zero‬")
print(number1/number2)
    # program = input("do you want to quit or continue: Y to quit or N to Start Over")
    # if program == "N" or program == "":
    #     continue
    # else:
    #     break