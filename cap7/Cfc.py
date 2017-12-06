''' Módulo que implementa a busca de componentes fortemente conexos '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo
from BuscaEmProfundidade import BuscaEmProfundidade
import copy

#pylint: disable=C0103

class Cfc:
    ''' Classe que implementa a busca por componentes fortemente conexos '''
    class TempoTermino:
        ''' Classe auxiliar para a DFS no grafo transposto '''
        def __init__(self, numVertices=0):
            self.f = [0 for i in range(numVertices)]
            self.restantes = [False for i in range(numVertices)]
            self.numRestantes = numVertices

        def maxTT(self):
            ''' Método que encontra o tempo de término máximo '''
            vMax = 0
            while not self.restantes[vMax]:
                vMax = vMax + 1
            for i in range(len(self.f)):
                if self.restantes[i]:
                    if self.f[i] > self.f[vMax]:
                        vMax = i
            return vMax

    def __init__(self, grafo=Grafo()):
        self.grafo = copy.deepcopy(grafo)
        self.tt = None

    def visitaDfs(self, grafo=Grafo(), u=0):
        ''' Visita DFS modificada para ser executada no
        Grafo Transposto a fim de encontrar os ciclos '''
        self.tt.restantes[u] = False
        self.tt.numRestantes = self.tt.numRestantes - 1
        print("  Vertice: " + str(u))
        if not grafo.listaAdjVazia(u):
            a = grafo.primeiroListaAdj(u)
            while a is not None:
                v = a.v2
                if self.tt.restantes[v]:
                    self.visitaDfs(grafo, v)
                a = grafo.proxAdj(u)

    def obterCfc(self):
        ''' Método que retorna um CFC '''
        dfs = BuscaEmProfundidade(self.grafo)
        dfs.buscaEmProfundidade()
        self.tt = Cfc.TempoTermino(self.grafo.numVertices)
        for u in range(self.grafo.numVertices):
            self.tt.f[u] = dfs.f[u]
            self.tt.restantes[u] = True
        print()
        grafoT = self.grafo.grafoTransposto()
        while self.tt.numRestantes > 0:
            vRaiz = self.tt.maxTT()
            print("Raiz da próxima árvore: " + str(vRaiz))
            self.visitaDfs(grafoT, vRaiz)

#pylint: enable=C0103
