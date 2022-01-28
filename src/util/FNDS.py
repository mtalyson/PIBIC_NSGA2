import gc
from src.util.Ponto import Ponto


class FNDS:

    def executa(self, listadeindividuos):
        listadepontos = []

        for i in range(len(listadeindividuos)):
            individuo = listadeindividuos.__getitem__(i)
            ponto1 = Ponto(individuo)
            listadepontos.append(ponto1)

        listadetodasasfronteiras = []
        fronteira1 = []

        # Parte 1 - Calculando a Primeira Fronteira
        for i in range(len(listadepontos)):
            ponto1 = listadepontos.__getitem__(i)
            ponto1.listaPontosDominados = []
            ponto1.numeroDeVezesPontoDominado = 0

            for j in range(len(listadepontos)):
                if i != j:
                    ponto2 = listadepontos.__getitem__(j)

                    if self.domina(ponto1, ponto2):
                        ponto1.listaPontosDominados.append(ponto2)
                    elif self.domina(ponto2, ponto1):
                        ponto1.numeroDeVezesPontoDominado += 1

            if not ponto1.numeroDeVezesPontoDominado:
                ponto1.rank = 1
                fronteira1.append(ponto1)

        del i, j, ponto1, ponto2, individuo
        gc.collect()

        listadetodasasfronteiras.append(fronteira1)

        # Parte 2 - Calculando as Fronteiras Restantes
        i = 0
        fronteira_i = listadetodasasfronteiras.__getitem__(i)

        while len(fronteira_i) != 0:
            proximafronteira = []

            for p in fronteira_i:
                listadetodosospontosdominados_p = p.listaPontosDominados

                for q in listadetodosospontosdominados_p:
                    q.numeroDeVezesPontoDominado -= 1

                    if not q.numeroDeVezesPontoDominado:
                        q.rank = i + 1
                        proximafronteira.append(q)

            i += 1
            listadetodasasfronteiras.append(proximafronteira)
            fronteira_i = proximafronteira

        del p, q, listadetodosospontosdominados_p, proximafronteira
        gc.collect()

        # Transformando Retorno de Lista de Pontos para Lista de Individuos
        retornoindividuos = []

        for i in range(len(listadetodasasfronteiras)):
            fronteira_i = listadetodasasfronteiras.__getitem__(i)

            if len(fronteira_i) > 0:
                fronteiradeindividuos = []

                for j in range(len(fronteira_i)):
                    ponto = fronteira_i.__getitem__(j)
                    individuo = ponto.getIndividuo()

                    fronteiradeindividuos.append(individuo)

                retornoindividuos.append(fronteiradeindividuos)

        del i, j, individuo, ponto, fronteiradeindividuos
        gc.collect()
        return None

    def domina(self, p1, p2):
        objetivo1 = p1.objetivos
        objetivo2 = p2.objetivos

        for i in range(len(objetivo1)):
            if objetivo2[i] < objetivo1[i]:
                return bool(False)

        resultado = bool(False)
        for i in range(len(objetivo1)):
            if objetivo1[i] < objetivo2[i]:
                resultado = bool(True)
                break

        return resultado
