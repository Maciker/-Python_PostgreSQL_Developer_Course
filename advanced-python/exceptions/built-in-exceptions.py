# https://docs.python.org/3/library/exceptions.html
# Resumen de errores tipicos
# AttributeError

class MyClass:
    def __init__(self):
        self.my_property = 5

x = MyClass()
print(x.my_property)

# ImportError

# import my_awesome_module

# Key error

#mydict = {'x':5, 'y':10}
#print(mydict['z'])

#RuntimeError

#Type Error

#int([])

# ValueError
#int('cinco')

# IOError
#open('my_file.txt', 'r')