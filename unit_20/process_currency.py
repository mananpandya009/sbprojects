from forex_python.converter import CurrencyRates, CurrencyCodes

currency_convert = CurrencyRates()
currency_code = CurrencyCodes()


class ConvertAPIHelper():
    def __init__(self, from_currency, to_currency, amount):
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
        self.amount = float(amount)

    def validate_currency(self):
        symbol_from = currency_code.get_symbol(self.from_currency)
        symbol_to = currency_code.get_symbol(self.to_currency)
        if symbol_to and symbol_from:
            return True, symbol_from, symbol_to
        else:
            return False, symbol_from, symbol_from

    def get_conversion(self):
        if self.amount:
            if self.amount > 0:
                if self.from_currency == self.to_currency:
                    return self.amount
                else:
                    rate = currency_convert.convert(self.from_currency, self.to_currency, self.amount)
                    return rate
            else:
                return 0
        else:
            return None


validity = ConvertAPIHelper('usd', 'inr', 10)
v = validity.validate_currency()
v2 = validity.get_conversion()

print(v)
print(v2)
