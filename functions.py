def math():
    a = int(input("Enter a number = "))
    b = int(input("Enter a next number = "))
    print(a*b)
math()

def fn(name):
   # print("Welcome" +" "+name)
    print("Welcome {}".format(name))
fn("Loki") #passing arguments

#Positional Arguments
def royal(name1, age, State):
#def royal(name1, age=22, State="TamilNadu") --> if arguments are not declared keyword arguments works by default
    print("{} is {} yeras old and he is from {}".format(name1,age,city))

royal(Loki,Tn) # Throws error by seeing the position

#why int - input will return str