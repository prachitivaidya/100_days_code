logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print (logo)

#Add
def add(n1, n2):
    return n1+n2

#substract
def sub(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide (n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("Input the first number: "))

    for key in operations:
        print(key)

    flag = True
    while flag:
        opr = input("Choose one symbol : ")
        calculation_func = operations[opr]
        num2 = float(input("Input the another number : "))

        ans = calculation_func(num1, num2)
        print(f"{num1} {opr} {num2} = {ans}")

        selection = input("Type 'y' to continuce with calculations or 'n' to exit or 's' to start new calculation: ")
        if selection == "y":
            num1= ans
        elif selection == "s":
            calculator()
        else :
            flag = False    

calculator()
print("Bye!!")