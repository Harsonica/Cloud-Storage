class Car(object):
    def __init__(self,module,color,company,speed_limit):
        self.color=color
        self.module = module
        self.company=company
        self.speed_limit=speed_limit

    def start (self):
        print("successful!-1")
    
    def stop (self):
        print("stop!")

    def accelarate (self):
        print("accelarate function!")


audi = Car("a6","black", "audi", 80)
print(audi.color)
print(audi.speed_limit)
audi.accelarate()
audi.start()


        

