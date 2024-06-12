#Defining parent class
class Add:
    # producer
    def result(self, a, b):
        print("Addition: ", a+b)

# Defining a child class
class Multi(Add):
    # Constructor
    def result(self, a, b):
        super().result(2,3)
        print("Multiplication: ", a*b)

m= Multi()
m.result(2,3)

