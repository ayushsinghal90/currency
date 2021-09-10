import graphene

from currency.rates.mutation import Mutation
from currency.rates.query import Query


schema = graphene.Schema(query=Query, mutation=Mutation)
