"""class-> grp variables and fucntions in a single organized unit
->inheritance - child class inherits attributes and methods of parent class
-> multiple inheritance - child class inherits attributes and methods from one or more class
-> polymorphism - child class can override class methods of parent class

class variables -> scope within the class
instance variables -> scope  within method

init_method -> sets attributes for the object
self -> ref to obj
"""
class Person:

   def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname #initialize
        self.lastname = lastname
        self.health = health
        self.status = status
   def introduce(self):
    print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

   def status_change(self):
    if self.health == 100:
       print("{} is totally healthy!".format(self.firstname))

    elif self.health >=76:
       print("{} is a little tired today.".format(self.firstname))

    elif self.health >= 51:
       print("{} feels unwell.".format(self.firstname))

    elif self.health >= 40:
       print("{} goes to the doctor".format(self.firstname))
    else:
        print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 95, status=True) #object creation
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

#-------------------------------------

class Enemy(Person):
    def __init__(self,weapon,firstname,lastname,health,status):
       super().__init__(firstname,lastname,health,status) #super() cl parent attri
       self.weapon=weapon

    def hurt(self,other):
     if self.weapon=='rock':
      other.health-=10
     elif self.weapon =='stick':
      other.health-=5
     print(other.health)

    def insult(self, other):
     if other.health <= 80:
       print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
       print("ha ha ha, {}, I have your stuff!".format(other.firstname))
       if other.status == True:
        other.status = False

    def introduce(self): #Overriding
        print("You are my mortal enemy!!!")

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Rey)


Maria.introduce()
Rey.introduce()
Alex.introduce()