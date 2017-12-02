''' Módulo que implementa a BFS (Breadth First Search), busca em largura. '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../cap3/autoreferencia")
from Fila import Fila
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo

#pylint: disable=C0103

class BuscaEmLargura:
    ''' Classe que implementa a BFS, busca em largura '''
    @staticmethod
    def branco(): #pylint: disable=C0111
        return 0
    @staticmethod
    def cinza(): #pylint: disable=C0111
        return 1
    @staticmethod
    def preto(): #pylint: disable=C0111
        return 2

    def __init__(self, grafo=Grafo()):
        self.grafo = grafo
        n = self.grafo.numVertices
        self.d = [0 for i in range(n)]
        self.antecessor = [0 for i in range(n)]

    def visitaBfs(self, u=0, cor=[]): #pylint: disable=W0102
        ''' Método que implementa a visita da BFS '''
        cor[int(u)] = BuscaEmLargura.cinza()
        self.d[int(u)] = 0
        fila = Fila()
        fila.insere(int(u))
        # print("Visita origem:" + str(u) + "cor: cinza F:", end='')
        # fila.imprime()
        while not fila.vazia():
            aux = fila.remove()
            u = int(aux)
            if not self.grafo.listaAdjVazia(u):
                a = self.grafo.primeiroListaAdj(u)
                while a != None:
                    v = a.v2
                    if cor[v] == BuscaEmLargura.branco():
                        cor[v] = BuscaEmLargura.cinza()
                        self.d[v] = self.d[u] + 1
                        self.antecessor[v] = u
                        fila.insere(v)
                    a = self.grafo.proxAdj(u)
            cor[u] = BuscaEmLargura.preto()
            # print("Visita " + str(u) + " dist: " + str(self.d[u]) + " cor: preto F:")
            # fila.imprime()

    def buscaEmLargura(self):
        ''' Método que realiza a BFS '''
        cor = [0 for i in range(self.grafo.numVertices)]
        for u in range(self.grafo.numVertices):
            cor[u] = BuscaEmLargura.branco()
            self.d[u] = float("inf")
            self.antecessor[u] = -1
        for u in range(self.grafo.numVertices):
            if cor[u] == BuscaEmLargura.branco():
                self.visitaBfs(u, cor)

    def imprimeCaminho(self, origem=0, v=0):
        if origem == v:
            print(str(origem))
        elif self.antecessor[int(v)] == -1:
            print("Não existe caminho de " + str(origem) + " até " + str(v))
        else:
            self.imprimeCaminho(origem, self.antecessor[int(v)])
            print(str(v))

#pylint: enable=C0103
