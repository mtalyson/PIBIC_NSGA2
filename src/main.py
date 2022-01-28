import numpy as np
from src.individuo.Individuo import Individuo
from src.problema.ProblemaExemplo import ProblemaExemplo
from src.util.FNDS import FNDS


def main():
    pop = [Individuo(ProblemaExemplo(), np.array([0], float)), Individuo(ProblemaExemplo(), np.array([1], float)),
           Individuo(ProblemaExemplo(), np.array([2], float)), Individuo(ProblemaExemplo(), np.array([3], float)),
           Individuo(ProblemaExemplo(), np.array([4], float)), Individuo(ProblemaExemplo(), np.array([5], float))]

    fnds = FNDS()
    fnds.executa(pop)


if __name__ == "__main__":
    main()
