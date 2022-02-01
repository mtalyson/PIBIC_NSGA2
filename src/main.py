from src.individuo.Individuo import Individuo
from src.problema.ProblemaExemplo import ProblemaExemplo
from src.util.FNDS import FNDS


def main():
    pop = [Individuo(ProblemaExemplo(), [0]), Individuo(ProblemaExemplo(), [1]),
           Individuo(ProblemaExemplo(), [2]), Individuo(ProblemaExemplo(), [3]),
           Individuo(ProblemaExemplo(), [4]), Individuo(ProblemaExemplo(), [5])]

    fnds = FNDS()
    fnds.executa(pop)


if __name__ == "__main__":
    main()
