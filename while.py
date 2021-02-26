for number in range(1, 10):  # range inbuild in fn. last value will not be considered
    if number == 5:
        print("Skip 5")
        continue
    print("Number {}".format(number))

for nu in range(20,30):
    if nu ==26:
        break
    print(nu)

for nu in range(50,60):
    if nu ==56: #skip the part
        pass
    else:
        print(nu)

"""
bike = [RE, V3, Pulsar]
car = [i10,innova]
bike.append --> To add an item to list
bike.extend(car) --> this will add car list to bike
bike.remove(name) --> to remove an item from list
pop is used to remove item with index value
pop(-1) used to remove the last item when index is not known
sort is used to sort integers
count is used to count the item in list
index is used to display the index of item
"""

bike = ["RE", "V3", "Pulsar"]
#print("RE" in bike)   # in for finding the membership in list --> It will return ture or false

bike.append("Hero")
print(bike)