import graphene

from currency.rates.models import CurrencyRates, Rates
from currency.rates.utils import fetch_and_save_rate


class UpdateRates(graphene.Mutation):
    class Arguments:
        base = graphene.String(required=True)
        symbols = graphene.List(graphene.String, required=True)

    ok = graphene.Boolean()
    currency_rates = graphene.Field(CurrencyRates)

    @staticmethod
    def mutate(root, info, base, symbols, input=None):
        currency_rates, ok = fetch_and_save_rate(base, symbols)
        if ok:
            rates = []
            for symbol in currency_rates:
                rates.append(Rates().create(base, symbol, currency_rates[symbol]))
            return UpdateRates(ok=ok, currency_rates=CurrencyRates().create(base, rates))
        return UpdateRates(ok=ok, currency_rates=None)


class Mutation(graphene.ObjectType):
    update_rates = UpdateRates.Field()
