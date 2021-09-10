import graphene


class Rates(graphene.ObjectType):
    base = graphene.String()
    symbol = graphene.String()
    rate = graphene.Float()

    def create(self, base, symbol, rate):
        self.base = base
        self.symbol = symbol
        self.rate = rate
        return self


class CurrencyRates(graphene.ObjectType):
    base = graphene.String()
    rates = graphene.List(Rates)

    def create(self, base, rates):
        self.base = base
        self.rates = rates
        return self
