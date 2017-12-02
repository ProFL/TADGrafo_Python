''' Módulo com implementação de um TAD Grafo por matriz de adjacência '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../cap3/autoreferencia")
from Fila import Fila
from Lista import Lista

#pylint: disable=C0103

class Grafo:
    ''' TAD Grafo por matriz de adjacência '''
    class Aresta:
        ''' Classe que implementa uma aresta com peso '''
        def __init__(self, v1=0, v2=0, peso=1):
            self.v1 = v1
            self.v2 = v2
            self.peso = peso

    def __init__(self, numVertices=0):
        self.mat = [[0 for i in range(numVertices)] for j in range(numVertices)]
        self.pos = [0 for i in range(numVertices)]
        self.numVertices = numVertices
        for i in range(numVertices):
            self.pos[i] = -1

    def insereVertice(self):
        ''' Insere vértice no grafo '''
        x = self.numVertices + 1
        matriz = [[0 for i in range(x)] for j in range(x)]
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                matriz[i][j] = self.mat[i][j]
        self.mat = matriz
        self.numVertices = self.numVertices + 1

    def insereAresta(self, v1=0, v2=0, peso=1):
        ''' Insere a aresta v1->v2 com o peso peso '''
        self.mat[v1][v2] = peso

    def existeAresta(self, v1=0, v2=0):
        ''' Retorna verdadeiro se existir a aresta v1->v2 '''
        return self.mat[v1][v2] > 0

    def listaAdjVazia(self, v=0):
        ''' Retorna verdadeiro se a lista adjunta de
        v for vazia '''
        for i in range(self.numVertices):
            if self.mat[v][i] > 0:
                return False
        return True

    def primeiroListaAdj(self, v=0):
        ''' Retorna e itera para a primeira aresta da
        lista adjunta de v '''
        self.pos[v] = -1
        return self.proxAdj(v)

    def proxAdj(self, v=0):
        ''' Retorna e itera para a próxima aresta da
        lista adjunta v '''
        self.pos[v] = self.pos[v] + 1
        while self.pos[v] < self.numVertices and self.mat[v][self.pos[v]] == 0:
            self.pos[v] = self.pos[v] + 1
        if self.pos[v] == self.numVertices:
            return None
        else:
            return Grafo.Aresta(v, self.pos[v], self.mat[v][self.pos[v]])

    def retiraAresta(self, v1=0, v2=0):
        ''' Retira e retorna a aresta v1->v2 se existir,
        do contrário, retorna None '''
        if self.mat[v1][v2] == 0:
            return None
        else:
            aresta = Grafo.Aresta(v1, v2, self.mat[v1][v2])
            self.mat[v1][v2] = 0
            return aresta

    def imprime(self):
        ''' Imprime o grafo no formato de matriz
        similar a uma tabela com os índices na primeira
        linha e primeira coluna respectivamente '''
        print("   ", end='')
        for i in range(self.numVertices):
            print(str(i) + "   ", end='')
        print()
        for i in range(self.numVertices):
            print(str(i) + "   ", end='')
            for j in range(self.numVertices):
                print(str(self.mat[i][j]) + "   ", end='')
            print()

    def grafoTransposto(self):
        ''' Retorna o grafo transposto '''
        grafoT = Grafo(self.numVertices)
        for v in range(self.numVertices):
            if not self.listaAdjVazia(v):
                adj = self.primeiroListaAdj(v)
                while adj != None:
                    grafoT.insereAresta(adj.v2, adj.v1, adj.peso)
                    adj = self.proxAdj(v)
        return grafoT

#pylint: enable=C0103
