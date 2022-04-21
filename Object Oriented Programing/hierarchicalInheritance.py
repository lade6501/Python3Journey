'''
	In hierarchical inheritance we derive all the properties of one super class 
	into multiple subclasses .
	For e.g Vehicle is super class and car, bike, bus, etc are subclasses of super class 
	which get's all properties of vehicle i.e super class.
'''

#Defining Vehicle class 
class Vehicle:
	#initializing the super class constructor
	def __init__(self):
		print('I\'m super class')

#Defining Car class and derving all the properties of Vehicle class(Super class)
class Car(Vehicle):
	def __init__(self):
		print('I\'m in car subclass')

#Defining Bike class and derving all the properties of Vehicle class(Super class)
class Bike(Vehicle):
	def __init__(self):
		print('I\'m in bike subclass')

#Defining Bus class and derving all the properties of Vehicle class(Super class)
class Bus(Vehicle):
	def __init__(self):
		print('I\'m in Bus subclass')