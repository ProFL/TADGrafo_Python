''' Módulo com implementação de um TAD Grafo por lista de adjacência '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../cap3/autoreferencia")
from Fila import Fila
from Lista import Lista

#pylint: disable=C0103

class Grafo:
    ''' TAD Grafo por lista de adjacência '''
    class Aresta:
        ''' Classe que implementa uma aresta com peso '''
        def __init__(self, v1=0, v2=0, peso=1):
            self.v1 = int(v1)
            self.v2 = int(v2)
            self.peso = int(peso)

    class Celula:
        ''' Classe que implementa uma celula de aresta '''
        def __init__(self, v=0, p=1):
            self.vertice = int(v)
            self.peso = int(p)

        def __eq__(self, other):
            return self.vertice == other.vertice

    def __init__(self, numVertices=0):
        self.adj = [Lista() for x in range(numVertices)]
        self.numVertices = numVertices

    def insereAresta(self, v1=0, v2=0, peso=1):
        ''' Método de inserção de aresta partindo de
        v1 para v2 com peso peso '''
        item = Grafo.Celula(v2, peso)
        self.adj[int(v1)].insere(item)

    def existeAresta(self, v1=0, v2=0):
        ''' Retorna verdadeiro se a aresta v1->v2 existir
        ou falso se ela não existir '''
        item = Grafo.Celula(v2, 0)
        return self.adj[int(v1)].pesquisa(item) is not None

    def listaAdjVazia(self, v=0):
        ''' Retorna verdadeiro se a lista adjunta de
        v for vazia '''
        return self.adj[int(v)].vazia()

    def primeiroListaAdj(self, v=0):
        ''' Retorna a primeira aresta da lista adjunta
        de v ou None se não houver'''
        item = self.adj[int(v)].getPrimeiro()
        return Grafo.Aresta(v, item.vertice, item.peso) if item is not None else None

    def proxAdj(self, v):
        ''' Retorna o elemento seguinte ao atual da
        última iteração da lista adjunta de v ou
        None se não houver'''
        item = self.adj[int(v)].proximo()
        return Grafo.Aresta(v, item.vertice, item.peso) if item is not None else None

    def retiraAresta(self, v1=0, v2=0):
        ''' Retira a aresta v1->v2 se ela existir e a retorna
        ou retorna None se ela não existir '''
        chave = Grafo.Celula(v2, 0)
        item = self.adj[int(v1)].retira(chave)
        return Grafo.Aresta(v1, v2, item.peso) if item is not None else None

    def imprime(self):
        ''' Imprime o grafo no formato:
        Vertice X:
            Vertice (Peso)
        Vertice X+1:
            Vertice (Peso)
            Vertice (Peso)...'''
        for i in range(self.numVertices):
            print("Vertice " + str(i) + ":")
            item = self.adj[i].getPrimeiro()
            while item is not None:
                print(" " + str(item.vertice) + " (" + str(item.peso) + ")")
                item = self.adj[i].proximo()

    def grafoTransposto(self):
        ''' Retorna o grafo transposto '''
        grafoT = Grafo(self.numVertices)
        for v in range(self.numVertices):
            if not self.listaAdjVazia(v):
                adj = self.primeiroListaAdj(v)
                while adj is not None:
                    grafoT.insereAresta(adj.v2, adj.v1, adj.peso)
                    adj = self.proxAdj(v)
        return grafoT

#pylint: enable=C0103
