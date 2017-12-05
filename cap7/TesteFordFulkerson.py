''' Módulo que realiza teste do algoritmo de Ford Fulkerson '''

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/listaadj/autoreferencia")
from Grafo import Grafo
from FordFulkerson import FordFulkerson

g = Grafo(6)
arestas = [[0, 1, 5],
           [0, 2, 6],
           [0, 3, 3],
           [1, 3, 1],
           [1, 4, 2],
           [2, 3, 1],
           [2, 5, 3],
           [3, 4, 9],
           [3, 5, 7],
           [4, 5, 5]]
for aresta in arestas:
    g.insereAresta(aresta[0], aresta[1], aresta[2])
ff = FordFulkerson(g, 0, 5)
ff.obterFluxoMaximo()
ff.imprimeFluxo()
