def RE(*args):
    for i in args: #For Loop
         print(i)

RE(250000,175000,200000)

def RoyalEnfiled(**kwargs):
    for a,b in kwargs.items():
        print(a,b) #a key , b value

RoyalEnfiled(StealthBalck = 250000, Red = 175000) # contains key value pair -->dictionary

#For loop
Re =("classic 350", "himalayan", "bullet 350", "bullet 500") #tuple
for Bike in Re:
    print("Which is your Favorite: {}".format(Bike))

for number in range(1,10): #range inbuild in fn. last value will not be considered

    print("Number: {}".format(number))

#explore args
