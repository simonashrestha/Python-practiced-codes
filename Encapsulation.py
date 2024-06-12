class Super:
    def __init__(self):
        self._value1= 100 #protected number
        self.__value2= 200  #private number

    def display(self):
        print (self._value1)
        print (self.__value2)
class Sub(Super):
    def show(self):
        print(self._value1)
        print(self.__value2)

ob1= Super()
ob1.display()

