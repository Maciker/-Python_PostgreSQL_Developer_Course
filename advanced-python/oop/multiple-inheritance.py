# Not many use.
class SuperBaseClass:
    def hi(self):
        print("Hola desde la Super Clase")

class ClassA(SuperBaseClass):
    pass

class ClassB:
    def hi(self):
        print("Kaixo")

    def bye(self):
        print("Agur")

# If the methos exist in ClassA, we use that. If not we use ClassB method
class ClassC(ClassA, ClassB):
    pass

c = ClassC()
c.hi()
c.bye()