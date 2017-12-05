''' Módulo que implementa o algoritmo de Ford-Fulkerson para encontrar fluxo máximo '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo
import copy
import re

#pylint: disable=C0103

class FordFulkerson:
    ''' Classe que implementa o algoritmo de Ford-Fulkerson
    para obter fluxo máximo '''
    def __init__(self, grafo=Grafo(), vertice_origem=0, vertice_destino=0):
        self.grafo = copy.deepcopy(grafo)
        self.redeResidual = copy.copy(grafo)
        self.fluxo = {} # Dicionário na forma de: "origem;destino" como chave.
        self.vertice_origem = vertice_origem
        self.vertice_destino = vertice_destino
        self.camAum = []
        self.cor = []

    @staticmethod
    def corNVisitado():
        return 0

    @staticmethod
    def corVisitado():
        return 1

    def visitaCamAum(self, u=0):
        ''' Método que implementa a visita modificadada DFS
        para encontrar caminhos de aumento '''
        self.cor[int(u)] = FordFulkerson.corVisitado()
        if not self.redeResidual.listaAdjVazia(u):
            a = self.redeResidual.primeiroListaAdj(u)
            while a is not None:
                v = a.v2
                if self.cor[v] == FordFulkerson.corNVisitado():
                    try:
                        self.camAum.index(a)
                    except ValueError:
                        self.camAum.append(a)
                        if a.v2 == self.vertice_destino:
                            return True
                        else:
                            if not self.visitaCamAum(v):
                                self.cor[a.v2] = FordFulkerson.corNVisitado()
                                self.camAum.remove(a)
                            else:
                                return True
                a = self.redeResidual.proxAdj(u)
        return False

    def obterCamAum(self):
        ''' Método que realiza a DFS para obter um caminho de aumento '''
        self.camAum = [] # Limpa o último caminho de aumento
        self.cor = [FordFulkerson.corNVisitado() for i in range(self.grafo.numVertices)]
        chegouDestino = self.visitaCamAum(self.vertice_origem)
        return chegouDestino

    def atualizaRedeResidual(self, aresta=Grafo.Aresta(), capRes=0):
        peso = capRes
        # Atualiza aresta do mesmo sentido da Rede Residual
        try:
            aRes = self.redeResidual.retiraAresta(aresta.v1, aresta.v2)
        except IndexError:
            aRes = None
        if aRes is not None:
            peso = aRes.peso - peso
        if peso > 0:
            self.redeResidual.insereAresta(aresta.v1, aresta.v2, peso)
        # Atualiza aresta no sentido oposto da Rede Residual
        peso = capRes
        try:
            aRes = self.redeResidual.retiraAresta(aresta.v2, aresta.v1)
        except IndexError:
            aRes = None
        if aRes is not None:
            peso = peso + aRes.peso
        self.redeResidual.insereAresta(aresta.v2, aresta.v1, peso)

    def obterFluxoMaximo(self):
        self.fluxo = {}
        for v in range(self.grafo.numVertices):
            a = self.grafo.primeiroListaAdj(v)
            while a is not None:
                self.fluxo[str(a.v1)+";"+str(a.v2)] = 0
                a = self.grafo.proxAdj(v)
        it = 1
        while True:
            print("Rede residual da it. "+str(it)+":",)
            self.redeResidual.imprime()
            haCamAum = self.obterCamAum()
            if haCamAum:
                capRes = float("inf")
                for i in range(len(self.camAum)):
                    fluxoAtual = self.camAum[i].peso
                    if fluxoAtual < capRes:
                        capRes = fluxoAtual
                for i in range(len(self.camAum)):
                    aAt = self.camAum[i] # arestaAtual
                    if self.grafo.existeAresta(aAt.v1, aAt.v2):
                        fluxoAt = self.fluxo[str(aAt.v1)+";"+str(aAt.v2)]
                        self.fluxo[str(aAt.v1)+";"+str(aAt.v2)] = fluxoAt + capRes
                        self.atualizaRedeResidual(aAt, capRes)
                    else:
                        fluxoAt = self.fluxo[str(aAt.v2)+";"+str(aAt.v1)]
                        self.fluxo[str(aAt.v2)+";"+str(aAt.v1)] = fluxoAt - capRes
                        self.atualizaRedeResidual(aAt, capRes)
            else:
                break
            it = it + 1
        return self.fluxo

    def imprimeFluxo(self):
        print("Fluxos no formato 'origem;destino': 'valor'")
        print(self.fluxo)
        print("Fluxo máximo: ", end='')
        fMax = 0
        for key, val in self.fluxo.items():
            if re.match(r"\d+;"+str(self.vertice_destino)+"$", key):
                fMax = fMax + float(val)
        print(fMax)

#pylint: enable=C0103
