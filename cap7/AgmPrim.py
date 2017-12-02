''' Módulo com implementação do algoritmo de Primm '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo
from FPHeapMinIndireto import FPHeapMinIndireto

#pylint: disable=C0103

class AgmPrim:
    ''' Classe com implementação do Algoritmo de Primm '''
    def __init__(self, grafo=Grafo()):
        self.antecessor = []
        self.peso = []
        self.grafo = grafo

    def obterAgm(self, raiz=0):
        ''' Gera a MST '''
        n = self.grafo.numVertices
        self.peso = [0.0 for i in range(n)]
        vs = [0 for i in range(n + 1)]
        itensHeap = [False for i in range(n)]
        self.antecessor = [0 for i in range(n)]
        for u in range(n):
            self.antecessor[u] = -1
            self.peso[u] = float("inf")
            vs[u + 1] = u
            itensHeap[u] = True
        self.peso[int(raiz)] = 0
        heap = FPHeapMinIndireto(self.peso, vs)
        heap.constroi()
        while not heap.vazio():
            u = int(heap.retiraMin())
            itensHeap[u] = False
            if not self.grafo.listaAdjVazia(u):
                adj = self.grafo.primeiroListaAdj(u)
                while adj is not None:
                    v = adj.v2
                    if itensHeap[v] and adj.peso < self.peso[v]:
                        self.antecessor[v] = u
                        heap.diminuiChave(v, adj.peso)
                    adj = self.grafo.proxAdj(u)

    def imprime(self):
        ''' Imprime a MST de Primm '''
        for u in range(len(self.peso)):
            if self.antecessor[u] != -1:
                print("(" + str(self.antecessor[u]) + "," + str(u) + ") -- p:" + str(self.peso[u]))

#pylint: enable=C0103
