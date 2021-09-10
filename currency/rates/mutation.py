import graphene

from currency.rates.schema import CurrencyRates, Rates
from currency.rates.utils import get_rates


class GetRates(graphene.Mutation):
    class Arguments:
        base = graphene.String(required=True)
        symbols = graphene.List(graphene.String(required=True))

    ok = graphene.Boolean()
    currency_rates = graphene.Field(CurrencyRates)

    @staticmethod
    def mutate(root, info, base, symbols, input=None):
        try:
            currency_rates = get_rates(base, symbols)
            rates = []
            for symbol in rates:
                rates.append(Rates().create(base, symbol, rates[symbol]))
            ok = True
            return GetRates(ok=ok, currency_rates=CurrencyRates().create(base, rates))
        except Exception as ex:
            ok = False
            return GetRates(ok=ok, currency_rates=None)


class Mutation(graphene.ObjectType):
    get_rates = GetRates.Field()
