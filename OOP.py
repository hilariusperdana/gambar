class Sepeda:
    def __init__(self,gear,speed):
        self.gear = gear
        self.speed = speed
    def melaju(self):
        print("kecepatan sepeda saat ini:" + self.speed)

sepeda=Sepeda(2,50)

print(sepeda.gear)
print(sepeda.speed)
#https://ilmucoding.com/tutorial-python-15-class-object/