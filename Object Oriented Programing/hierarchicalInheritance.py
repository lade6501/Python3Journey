'''
	In hierarchical inheritance we derive all the properties of one super class 
	into multiple subclasses .
	For e.g VehicleCompany is super class and car, bike, bus, etc are subclasses of super class 
	which get's all properties of vehicle i.e super class.
														  '''

import random
#Defining VehicleCompany class 
class VehicleCompany:
	CarData  = []
	BikeData = []
	BusData  = []

	#initializing the super class constructor
	def __init__(self,vehicle_type,capacity,fule_type):
		self.vehicle_type = vehicle_type
		self.capacity = capacity
		self.fule_type = fule_type
		self.manufacturer_name = manufacturer_name
		generateUniqueId(self)
		#adding vehicle details to database 
		saveVehicle(self)

	#generating unique id
    def generateUniqueId(self):
    	smallChars = 'abcdefghijklmnopqrstuvwxyz'
    	upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    	digits = '0123456789'
    	combination = smallChars + upperChars + digits

    	if (self.vehicle_type).lower() == car:
			uniqueId = ''.join(random.sample(combination,10))
			self.id = '01' + uniqueId
		if (self.vehicle_type).lower() == bike:
			uniqueId = ''.join(random.sample(combination,8))
			self.id = '02' + uniqueId
		if (self.vehicle_type).lower() == bus:
			uniqueId = ''.join(random.sample(combination,7))
			self.id = '03' + uniqueId

	'''
	   In this method in real life we will make database conncetion using 
	   different drivers and save vehicle data in different database according 
	   to the need. But for now I'm using list of objects to save data.
																		'''
	def saveVehicle(self):
		if (self.vehicle_type).lower() == car:
			CarData.append([self])
		if (self.vehicle_type).lower() == bike:
			BikeData.append([self])
		if (self.vehicle_type).lower() == bus:
			BusData.append([self])


#Defining Car class and derving all the properties of VehicleCompany class(Super class)
class Car(VehicleCompany):
	def __init__(self):
		super().__init__(self.vehicle_type,self.capacity,self.fule_type)
		print('I\'m in car subclass')
	def displayCar

#Defining Bike class and derving all the properties of VehicleCompany class(Super class)
class Bike(VehicleCompany):
	
	def __init__(self):
		super().__init__(self.vehicle_type,self.capacity,self.fule_type)
		print('I\'m in bike subclass')

#Defining Bus class and derving all the properties of VehicleCompany class(Super class)
class Bus(VehicleCompany):

	def __init__(self):
		super().__init__(self.vehicle_type,self.capacity,self.fule_type)
		print('I\'m in Bus subclass')

