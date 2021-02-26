name = input("Hlo Your Good name please: ")
if name == "Lokes":
    print("Hello Lokes welcome")
elif name == "John":
    print("Hello john")
else:
    print("Thanks")

#conditionals in calc
on = True
def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a+b)

def sub():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a-b)

def multi():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a*b)

def div():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a/b)

while on:
    operation = input("Please type +,-,* or / or q : ") # This will be called
    if operation == "+":
        add()
    elif operation == "-":
        sub()
    elif operation == "*":
        milti()
    elif operation == "/":
        div()
    elif operation == "q":
        on = False
    else:
        print("Operation does not match")
