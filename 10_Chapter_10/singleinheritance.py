class Car:
    @staticmethod
    def start():
        print("Car start")
    
    @staticmethod
    def stop():
        print("Car stop")

class Fortuner(Car):
    def __init__(self,Price):
        self.Price = Price

c1 = Fortuner(55000)
print(c1.Price)
print(c1.start())
print(c1.stop())
        