''' Módulo que contém procedimentos para digitação de um grafo '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo

#pylint: disable=C0103

class EntradaDeGrafo:
    @staticmethod
    def digitarAresta(): #pylint: disable=C0111
        print("Aresta:")
        v1 = int(input("  V1:"))
        v2 = int(input("  V2:"))
        peso = int(input("  Peso:"))
        return Grafo.Aresta(v1, v2, peso)

    @staticmethod
    def converteAresta(u=0, v=0, p=0): #pylint: disable=C0111
        v1 = int(u)
        v2 = int(v)
        peso = int(p)
        return Grafo.Aresta(v1, v2, peso)

    @staticmethod
    def insereArestaS(grafo=Grafo(), v1=0, v2=0, peso=0): #pylint: disable=C0111
        grafo.insereAresta(int(v1), int(v2), int(peso))
        grafo.insereAresta(int(v2), int(v1), int(peso))

    @staticmethod
    def digitarGrafo(): #pylint: disable=C0111
        nVertices = int(input("No. vertices:"))
        nArestas = int(input("No. arestas:"))
        grafo = Grafo(nVertices)
        for i in range(nArestas):
            a = EntradaDeGrafo.digitarAresta()
            EntradaDeGrafo.insereArestaS(grafo, a.v1, a.v2, a.peso)
        return grafo

#pylint: enable=C0103
