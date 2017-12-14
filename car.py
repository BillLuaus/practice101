class Car():

	def __init__(self,make,model,year):
		self.maked = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		self.gas_tank = 60

	def get_descriptive_name(self):
		long_name = str(self.year)+' ' + self.maked + ' '+self.model
		return long_name.title()

	def read_odometer(self):

		print("This car has " + str(self.odometer_reading) + " miles on it")

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cannot roll back an odometer!!!")

	def increment_odometer(self,miles):
		self.odometer_reading+=miles


	def fill_gas_tank(self):
		print("The car's tank is "+str(self.gas_tank))


class Battery():

	#def __init__(self,battery_size=70):
	def __init__(self):
		#self.battery_size=battery_size
		self.battery_size=70

	def describe_battery(self):

		print("This car has a "+str(self.battery_size) + "-kWh Battery")

#这个就是把实例提出来写了个类，直接在下面调用了。

	def get_range(self):

		tell_size=input('Please tell me your battery size ?')

		if int(tell_size) == self.battery_size:
		#if self.battery_size == 70:
			range = 240

		elif int(tell_size) > self.battery_size:
		#elif self.battery_size == 85:
			range =270


		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)



class ElectronicCar(Car):

	def __init__(self,make,model,year):


		super().__init__(make,model,year)

		self.battery1 = Battery()

	def fill_gas_tank(self):
		print("fuck you!")





my_tesla = ElectronicCar('Tesla','model s',2017)

print(my_tesla.get_descriptive_name())
my_tesla.battery1.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery1.get_range()