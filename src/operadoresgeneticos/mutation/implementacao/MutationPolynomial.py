import random
import math
from src.operadoresgeneticos.mutation.Mutation import Mutation
from src.util import RepairSolution


class MutationPolynomial(Mutation):
    mutationprobability = 0.0
    mutationdistributionindex = 0.0

    def MutationPolynomial(self, mutationprobability, mutationdistributionindex):
        self.mutationprobability = mutationprobability
        self.mutationdistributionindex = mutationdistributionindex

    def getMutation(self, x, lowerbound, upperbound):
        for i in range(len(x)):
            if random.random() <= self.mutationprobability:
                y = x[i]
                yl = lowerbound[i]
                yu = upperbound[i]
                if yl == yu:
                    y = yl
                else:
                    delta1 = (y - yl) / (yu - yl)
                    delta2 = (yu - y) / (yu - yl)
                    rnd = random.random()
                    mutpow = 1.0 / (self.mutationdistributionindex + 1.0)

                    if rnd <= 0.5:
                        xy = 1.0 - delta1
                        val = 2.0 * rnd + (1.0 - 2.0 * rnd) * (math.pow(xy, self.mutationdistributionindex + 1.0))
                        deltaq = 1.0 - math.pow(val, mutpow)
                    else:
                        xy = 1.0 - delta2
                        val = 2.0 * (1.0 - rnd) + 2.0 * (rnd - 0.5) * (
                            math.pow(xy, self.mutationdistributionindex + 1.0))
                        deltaq = 1.0 - math.pow(val, mutpow)

                    y = y + deltaq * (yu - yl)
                    y = RepairSolution.repairSolutionVariableValue(y, yl, yu)

                x[i] = y

        return x
