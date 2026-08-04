class Car:
    @staticmethod
    def start():
        print("Car start")
    
    @staticmethod
    def stop():
        print("Car stop")

class Fortuner(Car):
    def value(self):
        print("High range value")
        


class Alto(Fortuner):
    def __init__(self, price):
        self.price = price
        

c1 = Alto(55000)
print(c1.price)
c1.value()
c1.start()
c1.stop()


        