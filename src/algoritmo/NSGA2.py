import random
from src.individuo.IndividuoShaffeFactory import IndividuoShaffeFactory
from src.util.CrowdingDistance import CrowdingDistance
from src.util.FNDS import FNDS


class NSGA2:

    def execute(self, individuofactory, tamanhopopulacao, quantidadeepocas):
        populacaoinicial = []

        for i in range(tamanhopopulacao):
            populacaoinicial.append(individuofactory.getIndividuo())

        epoca = 1

        while epoca <= quantidadeepocas:
            filhos = []

            makeOffspring(filhos, populacaoinicial)
            uniaopaifilhos = []
            uniaopaifilhos.extend(populacaoinicial)
            uniaopaifilhos.extend(filhos)

            fnds = FNDS()
            listafronteiras = fnds.executa(uniaopaifilhos)
            novapopulacao = []

            i = 0
            while len(novapopulacao) + len(listafronteiras.__getitem__(i)) <= tamanhopopulacao:
                novapopulacao.extend(listafronteiras.__getitem__(i))
                i += 1

            ultimafronteira = listafronteiras.__getitem__(i)
            if len(novapopulacao) < tamanhopopulacao:
                crowdingdistance = CrowdingDistance()
                crowdingdistance.avaliar(ultimafronteira)

                novapopulacaotamanhooriginal = len(novapopulacao)
                for j in range(tamanhopopulacao - novapopulacaotamanhooriginal):
                    novapopulacao.append(ultimafronteira.__getitem__(j))

            populacaoinicial = novapopulacao
            if epoca % 20 == 0 or epoca == 1:
                print("--> Epoca = %d" % epoca + "\n")
                imprimirPopulacao(novapopulacao)
                print("\n")

            epoca += 1


def imprimirPopulacao(novapopulacao):
    for i in range(len(novapopulacao)):
        individuo = novapopulacao.__getitem__(i)

        print("(", end='')
        objetivos = individuo.getObjetivos()
        for j in range(len(objetivos)):
            if j == len(objetivos) - 1:
                print("%f" % objetivos[j] + ") ", end='')
            else:
                print("%f" % objetivos[j] + ";", end='')


def makeOffspring(listafilhos, populacaoinicial):
    populacaoauxiliar = []
    populacaoauxiliar.extend(populacaoinicial)

    while len(populacaoauxiliar) > 1:
        idxr1 = random.randint(0, len(populacaoauxiliar) - 1)
        pai1 = populacaoauxiliar.pop(idxr1)

        idxr2 = random.randint(0, len(populacaoauxiliar) - 1)
        pai2 = populacaoauxiliar.pop(idxr2)

        filhos = pai1.recombinar(pai2)

        filho1 = filhos.__getitem__(0)
        if random.random() > 0.9:
            filho1.mutar()

        filho2 = filhos.__getitem__(1)
        if random.random() > 0.9:
            filho2.mutar()

        listafilhos.extend(filhos)


def main():
    individuofactory = IndividuoShaffeFactory()

    nsga2 = NSGA2()
    nsga2.execute(individuofactory, 20, 100)


if __name__ == "__main__":
    main()
