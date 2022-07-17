
class car:
    def __init__(self,body,engin,tyre):
        self.body=body
        self.engin=engin
        self.tyre=tyre
    def milage(self):
        print("milage of the car")

c= car('pritam','pawar','satara')

class tata(car):
    pass

t = tata('yash','sahebra','alloys')
print(t)
print(t.milage())

