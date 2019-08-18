class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number

# All Decimal can do, Currency can do too.
class Currency(Decimal):
    def __init__(self, symbol, number, places):
        # Call in the init method of the superclass
        super().__init__(number, places)
        self.symbol = symbol

    def __repr__(self):
        # Using the super __repr__ method and addin the symbol
        return "{} {}".format(super().__repr__(), self.symbol)
    
print(Currency("€", 10.981612,3))