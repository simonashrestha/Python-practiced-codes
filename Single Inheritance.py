# Base class

class Father:

    def function_1(self):
        print ("I am father.")

# Child class

class Children(Father):

    def function_2(self):
        print ("I am son.")

object = Children()
object.function_1()
object.function_2()