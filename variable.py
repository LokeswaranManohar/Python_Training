Bike ="Royal Enfield"
Age = 22
print(Bike)
print(type(Bike))
print(type(Age))

#String Format

name = "Hi, This is Lokeswaran Manohar"
work = "Associate Software Engineer"
print(name + work)
print(name + " " + work)
print("{} works as an {} in Atmecs".format(name, work)) #Formatting in print by declaring variable name

# 2nd method

na = "{} Welcome to {}"
print(na.format("Hi Lokes", "Atmecs")) #declaring values inside variable

# 3rd method
s = "{0} Welcome to {1} I am {2} project head."
print(s.format("Hi lokes", "Chownow", "Madhu")) #Calling the variables using index


