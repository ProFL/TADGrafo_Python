''' Módulo que implementa o algoritmo de Dijkstra para encontrar caminhos mínimos '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo
from FPHeapMinIndireto import FPHeapMinIndireto

#pylint: disable=C0103

class Dijkstra:
    ''' Classe que implementa o algoritmo de Dijkstra
    para obter árvores de caminhos mínimos '''
    def __init__(self, grafo=Grafo()):
        self.antecessor = []
        self.peso = []
        self.grafo = grafo

    def obterArvoreCMC(self, raiz=0):
        ''' Constrói a árvore de caminhos mínimos
        a partir da raiz '''
        n = self.grafo.numVertices
        self.peso = [0.0 for i in range(n)]
        vs = [0 for i in range(n + 1)]
        self.antecessor = [0 for i in range(n)]
        for u in range(n):
            self.antecessor[u] = -1
            self.peso[u] = float("inf")
            vs[u + 1] = u
        self.peso[int(raiz)] = 0
        heap = FPHeapMinIndireto(self.peso, vs)
        heap.constroi()
        while not heap.vazio():
            u = int(heap.retiraMin())
            if not self.grafo.listaAdjVazia(u):
                adj = self.grafo.primeiroListaAdj(u)
                while adj is not None:
                    v = adj.v2
                    if self.peso[v] > (self.peso[u] + adj.peso):
                        self.antecessor[v] = u
                        heap.diminuiChave(v, self.peso[u] + adj.peso)
                    adj = self.grafo.proxAdj(u)

    def imprime(self):
        ''' Imprime a CMC '''
        for u in range(len(self.peso)):
            if self.antecessor[u] != -1:
                print("(" + str(self.antecessor[u]) + "," + str(u) +  ") -- p:" + str(self.peso[u]))

    def imprimeCaminho(self, origem=0, v=0):
        ''' Imprime o caminho, se houver, partindo de origem
        até o destino v '''
        if origem == v:
            print(str(origem))
        elif self.antecessor[int(v)] == -1:
            print("Não existe caminho de " + str(origem) + " até " + str(v))
        else:
            self.imprimeCaminho(origem, self.antecessor[int(v)])
            print(str(v))

#pylint: enable=C0103
