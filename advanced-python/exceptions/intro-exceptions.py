# Exception: error in a programm, that stop the programm.
from json import JSONDecodeError

import requests

"""number = input("Enter a number: ")

try:
    print(int(number) * 2)
except LookupError:
    print("Lookup error? This should never happen...")
except ValueError:
    print("You did not enter a base 10 number. Try again.")

print("The programm continue...")
"""

r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'Hello world'})
try:
    label= r.json()['label']
    print(label)
except JSONDecodeError:
    print('We could not decode the JSON response')
except KeyError:
    print('We got JSON back, but without he key label')
