class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    # Not necessary but interesting. in python we can do pounds.amount = 15
    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        to_convert = amount if amount is not None else self.amount
        return to_convert * self.exchange_to_usd

    # Build-in-method: Greater than
    # others: lt: less than, le: less than or equal... etc
    def __eq__(self, other):
        return self.to_usd() == other.to_usd()

    def __gt__(self, other):
        return self.to_usd() > other.to_usd()

    def __lt__(self, other):
        return self.to_usd() < other.to_usd()

    def __le__(self, other):
        return self.to_usd() <= other.to_usd()

    def __ge__(self, other):
        return self.to_usd() >= other.to_usd()

def _get_currency_resourse(resource, transform =(lambda x: x)):
    # requests.get(blablabla) .... json()
    # we retrieving this from a API
    data={
        'items':[
            {'code': 'usd', 'amount_to_usd': 1.00},
            {'code': 'gbp', 'amount_to_usd': 1.21},
            {'code': 'eur', 'amount_to_usd': 1.07},
            {'code': 'jpy', 'amount_to_usd': 0.14}
        ]
    }
    my_resource = data[resource]
    # == to return list(map(transform, my_resource))
    return [transform(x) for x in my_resource]

def get_currency_codes():
   return _get_currency_resourse('items', lambda x: x['code'].upper())

def get_currencies():
    return _get_currency_resourse('items', lambda x: Currency(x['code'],x['amount_to_usd']))

def calculate_in_all_currencies(usd_amount):
    print("-- {} USD in all currencies --".format(usd_amount))
    for currency in get_currencies():
        print("In {}: {:.2f}".format(currency.code, currency.in_currency(usd_amount)))

print(get_currency_codes())
print(get_currencies())
calculate_in_all_currencies(1000)