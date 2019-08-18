class MissingLabelError(KeyError):
    pass

class PageNotFound(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUserNameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass

# Program... user entres wrong username
def login():
    raise IncorrectUserNameError

try:
    login()
except IncorrectUserNameError:
    print("Username incorrect. Have you forgotten it?")
except IncorrectPasswordError:
    print("Incorrect Password. Try again.")