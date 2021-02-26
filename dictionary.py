RE={"name": "classic 350","place":"coimbatore","price":250000}  #dictionary

#dic methods
print(RE.get("name"))   #return value for that key

print(RE.items())  #entire dictionary details  are displayed in order

print(RE.keys()) #returns all keys the dictionary has

print(RE.popitem()) #removes the last item
print(RE)

#setdefault -> prints the value for that specified key
# -> also sets default value for a key which is not present in the dictionary and adds that value to the dictionary
print(RE.setdefault("name"))
print(RE)
print(RE.setdefault("tax",11))
print(RE)

#update frst dic with other dic
new ={"one":1,"two":2}
RE.update(new)
print(RE)

new ={"three":3,"four":4}
RE.update(new)
print(RE)

up_new={"name":"classic 350 RE","piece":4}
RE.update(up_new)
print(RE)

RE.update( name = "xxx")  #add items without using dictionaries
print(RE)

#nested dic