''' Módulo para testar o algoritmo de Primm '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from EntradaDeGrafo import EntradaDeGrafo
from Grafo import Grafo
from AgmPrim import AgmPrim

#pylint: disable=C0103

raiz = int(input("Raiz da AGM:"))
# grafo = EntradaDeGrafo.digitarGrafo()
grafo = Grafo(6)
arestas = [[0, 1, 6],
           [0, 2, 100],
           [0, 3, 5],
           [1, 2, 2],
           [1, 4, 5],
           [2, 3, 2],
           [2, 4, 6],
           [2, 5, 4],
           [3, 5, 3],
           [4, 5, 4]]
for aresta in arestas:
    a = EntradaDeGrafo.converteAresta(aresta[0], aresta[1], aresta[2])
    EntradaDeGrafo.insereArestaS(grafo, a.v1, a.v2, a.peso)

agm = AgmPrim(grafo)
agm.obterAgm(raiz)
agm.imprime()

#pylint: enable=C0103
