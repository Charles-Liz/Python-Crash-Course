class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_describe_name(self):
        print(self.model+self.make+self.year)
    def read_odometer(self):
        print(self.odometer_reading)
    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you can not do this')
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class Battery():

    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a "+str(self.battery_size)+" -kwh battery")

    def get_range(self):
        if self.battery_size ==70:
            range = 270
        elif self.battery_size ==85:
            range = 900
        message = "this car can go approximately "+str(range)
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        return  self.battery_size
class ElectricCar(Car):

    def __init__(self,make,model,year):
        '''chushihuafuleishuxing'''
        super().__init__(make,model,year)
        self.battery = Battery()
ecar = ElectricCar('audi', 'a3', 2014)
ecar.battery.get_range()
ecar.battery.upgrade_battery()
ecar.battery.get_range()
