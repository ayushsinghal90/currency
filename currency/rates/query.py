import graphene
from graphene import ObjectType

from currency.rates.schema import CurrencyRates, Rates
from currency.rates.utils import get_rates


class Query(ObjectType):
    rates = graphene.Field(CurrencyRates, base=graphene.String(), symbol=graphene.String())

    def resolve_rates(self, info, **kwargs):
        base = kwargs.get('base')
        symbols = kwargs.get('symbols')

        try:
            currency_rates = get_rates(base, symbols)
            rates = []
            for symbol in currency_rates:
                rates.append(Rates().create(base, symbol, rates[symbol]))
            return CurrencyRates().create(base, rates)
        except Exception as ex:
            return ex
