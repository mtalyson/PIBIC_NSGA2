from src.algoritmo.NSGA2 import NSGA2
from src.individuo.IndividuoShaffeFactory import IndividuoShaffeFactory


def main():
    individuofactory = IndividuoShaffeFactory()

    nsga2 = NSGA2()
    nsga2.execute(individuofactory, 20, 10000)


if __name__ == "__main__":
    main()
