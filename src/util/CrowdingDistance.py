from src.individuo.Individuo import Individuo
from src.problema.ProblemaTeste import ProblemaTeste


class CrowdingDistance:

    def avaliar(self, t):
        s = len(t)

        for ind in t:
            ind.crowdingdistance = 0

        primeiroindividuo = t.__getitem__(0)
        quantidadeobjetivos = len(primeiroindividuo.getObjetivos())

        for m in range(quantidadeobjetivos):
            self.ordenarPorObjetivo(t, m)
            t.__getitem__(0).crowdingdistance = float('inf')
            t.__getitem__(s - 1).crowdingdistance = float('inf')

            for i in range(s - 1):
                aux = (t.__getitem__(i + 1).getObjetivos()[m] - t.__getitem__(i - 1).getObjetivos()[m]) / \
                      (t.__getitem__(s - 1).getObjetivos()[m] - t.__getitem__(0).getObjetivos()[m])

                t.__getitem__(i).crowdingdistance += aux

        self.ordenarPorCrowdingDistance(t)

    def ordenarPorObjetivo(self, t, n):
        for i in range(len(t)-1):
            for j in range(i + 1, len(t)):
                if t.__getitem__(i).getObjetivos()[n] > t.__getitem__(j).getObjetivos()[n]:
                    aux = t.__getitem__(i)
                    t.__setitem__(i, t.__getitem__(j))
                    t.__setitem__(j, aux)

    def ordenarPorCrowdingDistance(self, t):
        for i in range(len(t)-1):
            for j in range(i + 1, len(t)):
                if t.__getitem__(i).crowdingdistance < t.__getitem__(j).crowdingdistance:
                    aux = t.__getitem__(i)
                    t.__setitem__(i, t.__getitem__(j))
                    t.__setitem__(j, aux)

# Testar Crowding Distance (Debugar)
def main():
    fronteiraindividuos = [
        Individuo(ProblemaTeste(), [6]), Individuo(ProblemaTeste(), [7]),
        Individuo(ProblemaTeste(), [8]), Individuo(ProblemaTeste(), [9])
    ]

    cd = CrowdingDistance()
    cd.avaliar(fronteiraindividuos)


if __name__ == "__main__":
    main()
