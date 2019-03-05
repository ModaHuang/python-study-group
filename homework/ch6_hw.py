def debug(variable_name, variable):
    print(variable_name, "=", variable, "\n    type =", type(variable))


"""
6.1. 
Make a class called Thing with no contents and print it. 
Then, create an object called example from this class and also print it. 
Are the printed values the same or different?
"""
print("Q6.1")


class Thing():
    pass


example = Thing()

print(Thing)
print(example)


"""
6.2. 
Make a new class called Thing2 and 
assign the value 'abc' to a class attribute called letters. 
Print letters.
"""
print("\nQ6.2")


# class Thing2():
#     def __init__(self, letters):
#         self.letters = 'abc'


class Thing2():
    letters = 'abc'


print(Thing2.letters)


"""
6.3. Make yet another class called, of course, Thing3. 
This time, assign the value 'xyz' to an instance (object) attribute called letters. 
Print letters. Do you need to make an object from the class to do this?
"""
print("\nQ6.3")


class Thing3():
    def __init__(self):
        self.letters = 'xyz'


# class Thing3():
#     def __init__(self, letters):
#         self.letters = letters

letters = Thing3()
# letters = Thing3('xyz')

print(letters.letters)
# print(Thing3.letters)

"""
6.4. Make a class called Element, 
with instance attributes name, symbol, and number. 
Create an object of this class with the values 'Hydrogen', 'H', and 1.
"""
print("\nQ6.4")


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

"""
6.5. Make a dictionary with these keys and values: 
'name': 'Hydrogen', 'symbol': 'H', 'number': 1
Then, create an object called hydrogen from class Element using this dictionary.
"""
print("\nQ6.5")


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


dic = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**dic)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)


"""
6.6. For the Element class, 
define a method called dump() 
that prints the values of the object’s attributes (name, symbol, and number). 
Create the hydrogen object from this new definition and use dump() 
to print its attributes.
"""
print("\nQ6.6")


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("name = %s, symbol = %s, number = %d" % (self.name, self.symbol, self.number))


hydrogen = Element('Hydrogen', 'H', 1)

hydrogen.dump()

"""
6.7. Call print(hydrogen). 
In the definition of Element, change the name of method dump to __str__, 
create a new hydrogen object, and call print(hydrogen) again.
"""
print("\nQ6.7")


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return "name = %s, symbol = %s, number = %d" % (self.name, self.symbol, self.number)


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)

"""
6.8. Modify Element to make the attributes name, symbol, and number private. 
Define a getter property for each to return its value.
"""
print("\nQ6.8")


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.number


hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen.get_name())
print(hydrogen.get_symbol())
print(hydrogen.get_number())

"""
6.9. Define three classes: Bear, Rabbit, and Octothorpe. 
For each, define only one method: eats(). 
This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). 
Create one object from each and print what it eats.
"""
print("\nQ6.9")


class Bear():
    def eat(self):
        return 'berries'


class Rabbit():
    def eat(self):
        return 'clover'


class Octothorpe():
    def eat(self):
        return 'campers'


my_bear = Bear()
my_rabbit = Rabbit()
my_octothorpe = Octothorpe()

print(my_bear.eat())
print(my_rabbit.eat())
print(my_octothorpe.eat())

"""
6.10. Define these classes: 
Laser, Claw, and SmartPhone. 
Each has only one method: does(). 
This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (Smart Phone). 
Then, define the class Robot that has one instance (object) of each of these. 
Define a does() method for the Robot that prints what its component objects do.
"""
print("\nQ6.10")


class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self):
        self.Laser = Laser()
        self.Claw = Claw()
        self.SmartPhone = SmartPhone()

    def does(self):
        print('Laser = %s, Claw = %s, SmartPhone = %s' % (self.Laser.does(), self.Claw.does(), self.SmartPhone.does()))


my_robot = Robot()
my_robot.does()
