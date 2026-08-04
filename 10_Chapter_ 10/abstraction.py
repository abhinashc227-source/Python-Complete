class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car Started..")

car1 = Car()
car1.start()