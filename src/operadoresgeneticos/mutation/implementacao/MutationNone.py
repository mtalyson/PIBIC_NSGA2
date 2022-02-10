from src.operadoresgeneticos.mutation.Mutation import Mutation


class MutationNone(Mutation):

    def __init__(self):
        pass

    def getMutation(self, x, lowerbound, upperbound):
        return x
