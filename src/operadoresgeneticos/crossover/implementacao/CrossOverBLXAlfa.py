import random
from src.operadoresgeneticos.crossover.CrossOver import CrossOver
from src.util import RepairSolution


class CrossOverBLXAlfa(CrossOver):
    desviopadrao = 0.0
    inverterrandgenesfilhos = True

    def __init__(self, desviopadrao):
        self.CrossOverBLXAlfa(desviopadrao, True)

    def CrossOverBLXAlfa(self, desviopadrao, inverterrandgenesfilhos):
        self.desviopadrao = desviopadrao
        self.inverterrandgenesfilhos = inverterrandgenesfilhos

    def getOffSpring(self, vars1, vars2, lowerbounds, upperbounds):
        ret = [None, None]

        f1 = [None, None]
        f2 = [None, None]

        for i in range(len(vars1)):
            if self.inverterrandgenesfilhos:
                if random.random() > 0.5:
                    c1 = vars1[i] + (random.gauss(0, 1) * self.desviopadrao) * abs(vars1[i] - vars2[i])
                    c2 = vars2[i] + (random.gauss(0, 1) * self.desviopadrao) * abs(vars1[i] - vars2[i])
                else:
                    c2 = vars1[i] + (random.gauss(0, 1) * self.desviopadrao) * abs(vars1[i] - vars2[i])
                    c1 = vars2[i] + (random.gauss(0, 1) * self.desviopadrao) * abs(vars1[i] - vars2[i])
            else:
                c1 = vars1[i] + (random.gauss(0, 1) * self.desviopadrao) * abs(vars1[i] - vars2[i])
                c2 = vars2[i] + (random.gauss(0, 1) * self.desviopadrao) * abs(vars1[i] - vars2[i])

            c1 = RepairSolution.repairSolutionVariableValue(c1, lowerbounds[i], upperbounds[i])
            c2 = RepairSolution.repairSolutionVariableValue(c2, lowerbounds[i], upperbounds[i])

            f1[i] = c1
            f2[i] = c2

        ret[0] = f1
        ret[1] = f2

        return ret
