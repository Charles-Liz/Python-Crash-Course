from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        for number in range(1,11):
            print(randint(1,self.sides))
die6 = Die(6)
die6.roll_die()
print("10mian")
die10 = Die(10)
die10.roll_die()
die20 = Die(20)
print("20mian")
die20.roll_die()
