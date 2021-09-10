import graphene

from currency.rates.query import Query
from currency.rates.mutation import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
