import graphene
from graphene import ObjectType

from currency.rates.utils import get_rates
from currency.rates.models import CurrencyRates, Rates


class Query(ObjectType):
    rates = graphene.Field(CurrencyRates,
                           base=graphene.String(required=True),
                           symbols=graphene.List(graphene.String, required=True))

    def resolve_rates(self, info, **kwargs):
        base = kwargs.get('base')
        symbols = kwargs.get('symbols')

        try:
            currency_rates = get_rates(base, symbols)
            rates = []
            for symbol in currency_rates:
                rates.append(Rates().create(base, symbol, currency_rates[symbol]))
            return CurrencyRates().create(base, rates)
        except Exception as ex:
            return ex
