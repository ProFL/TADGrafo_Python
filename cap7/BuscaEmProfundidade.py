''' Módulo que implementa a DFS (Depth First Search), busca em profundidade '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo

#pylint: disable=C0103

class BuscaEmProfundidade:
    ''' Classe que implementa a DFS, busca em profundidade '''
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
        self.f = [0 for i in range(n)]
        self.antecessor = [-1 for i in range(n)]

    def visitaDfs(self, u=0, tempo=0, cor=[]): #pylint: disable=W0102
        ''' Método que implementa a visita da DFS '''
        cor[int(u)] = BuscaEmProfundidade.cinza()
        tempo = tempo + 1
        self.d[int(u)] = tempo
        # print("Visita " + str(u) + " Descoberta:" + str(self.d[int(u)]) + " cinza")
        if not self.grafo.listaAdjVazia(u):
            a = self.grafo.primeiroListaAdj(u)
            while a != None:
                v = a.v2
                if cor[v] == BuscaEmProfundidade.branco():
                    self.antecessor[v] = int(u)
                    tempo = self.visitaDfs(v, tempo, cor)
                a = self.grafo.proxAdj(u)
        cor[u] = BuscaEmProfundidade.preto()
        tempo = tempo + 1
        self.f[u] = int(tempo)
        # print("Visita: " + str(u) + " Termino:" + str(self.t[int(u)]) + " preto")
        return tempo

    def buscaEmProfundidade(self):
        ''' Método que realiza a DFS '''
        tempo = 0
        cor = [BuscaEmProfundidade.branco() for i in range(self.grafo.numVertices)]
        self.antecessor = [-1 for i in range(self.grafo.numVertices)]
        for u in range(self.grafo.numVertices):
            if cor[u] == BuscaEmProfundidade.branco():
                tempo = self.visitaDfs(u, tempo, cor)

#pylint: enable=C0103
