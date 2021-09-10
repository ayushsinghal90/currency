import graphene

from currency.rates.mutation import Mutation
from currency.rates.query import Query


class Rates(graphene.ObjectType):
    base = graphene.String()
    symbol = graphene.String()
    rate = graphene.Float()

    def create(self, base, symbol, rate):
        self.base = base
        self.symbol = symbol
        self.rate = rate


class CurrencyRates(graphene.ObjectType):
    base = graphene.String()
    rates = Rates

    def create(self, base, rates):
        self.base = base
        self.rates = rates


schema = graphene.Schema(query=Query, mutation=Mutation)
